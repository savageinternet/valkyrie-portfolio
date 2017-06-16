import copy, os, sys, json, re
from html_templates import *

IN_DIR = 'content/'
OUT_DIR = 'build/content/'

def format_several(formatString, formattables):
    allThingies = ''
    for formattable in formattables:
        allThingies = allThingies + format_one(formatString, formattable)
    return allThingies

def format_one(formatString, formattable):
    return formatString % formattable

def format_links(links):
    return format_several(HTML_LINK, links)

def format_images(images):
    return format_several(HTML_IMG, images)

def format_image(image):
    return format_one(HTML_IMG, image)

def format_thumbnail(thumbnail):
    return format_one(HTML_IMG, {'src':'/img/'+thumbnail})

def format_youtube(video):
    return format_one(HTML_YOUTUBE, {'video':video})

def images_in_dir(dir):
    dir = os.path.join(os.getcwd(), dir)
    images = [{'src' : '/img/' + f} for f in os.listdir(dir) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]
    return images

def project_pages(projectPages):
    for projectPage in projectPages['projectpages']:
        base = copy.copy(HTML_PROJECT_PAGE)
        projectPage['links'] = format_links(projectPage['links'])
        projectPage['thumbnail'] = format_thumbnail(projectPage['thumb'])
        projectPage['images'] = format_images(images_in_dir(projectPage['imagedir']))
        projectPage['description'] = projectPage['description'].replace('\n',HTML_BR)
        formatted = base % projectPage
        f = OUT_DIR + re.sub('[!@#$\' ,:]', '', projectPage['title'].lower()) + '.html'
        f = open(f,'w+')
        f.write(formatted)
        f.close()

def research_pages(researchPages):
    for researchPage in researchPages['researchpages']:
        base = copy.copy(HTML_RESEARCH_PAGE)
        researchPage['links'] = format_links(researchPage['links'])
        researchPage['thumbnail'] = format_thumbnail(researchPage['thumb'])
        researchPage['abstract'] = researchPage['abstract'].replace('\n',HTML_BR)
        if researchPage['video'] is not '':
            researchPage['video'] = format_youtube(researchPage['video'])
        formatted = base % researchPage
        f = OUT_DIR + re.sub('[!@#$\' ,:]', '', researchPage['title'].lower()) + '.html'
        f = open(f,'w+')
        f.write(formatted)
        f.close()

def load_json(fname):
    f = open(fname)
    jsonz = ''.join(f.readlines())
    jsonz = json.loads(jsonz)
    return jsonz

def main():
    projectPages = load_json('content/projectpages.json')
    project_pages(projectPages)
    researchPages = load_json('content/researchpages.json')
    research_pages(researchPages)
