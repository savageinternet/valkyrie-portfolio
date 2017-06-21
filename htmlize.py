import pystache

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.realpath(__file__))
IN_DIR = os.path.join(ROOT, 'content')
PROJECTS_FILENAME = os.path.join(IN_DIR, 'projects.json')
RESEARCH_FILENAME = os.path.join(IN_DIR, 'research.json')
OUT_DIR = os.path.join(ROOT, 'build')

RENDERER = pystache.Renderer(search_dirs=[IN_DIR])
TEMPLATE_CACHE = {}


def render(template_name, data):
    if template_name not in TEMPLATE_CACHE:
        template_path = os.path.join(IN_DIR, template_name + '.mustache')
        with open(template_path) as template_file:
            template_str = template_file.read()
            TEMPLATE_CACHE[template_name] = pystache.parse(template_str)
    return RENDERER.render(TEMPLATE_CACHE[template_name], data)


def is_image(f):
    return f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')


def images_in_dir(dir_name):
    dir_path = os.path.join(ROOT, 'img', dir_name)
    images = []
    for f in os.listdir(dir_path):
        if is_image(f):
            src = '/img/' + dir_name + '/' + f
            images.append({'src': src})
    return images


def make_page(filename, html):
    path = os.path.join(OUT_DIR, filename)
    print('Generating {0}...'.format(path))
    with open(path, 'w+') as f:
        f.write(html)


def make_index_page(projects, research):
    html = render('index', {
      'pageTitle': 'Valkyrie Savage - Designer',
      'projects': projects,
      'research': research
    })
    make_page('index.html', html)


def get_project_filename(project):
    title = project['title'].lower()
    title = re.sub('[!@#$\' ,:]', '', title)
    return title + '.html'


def make_project_page(project):
    page_title = project['title'] + ' - Valkyrie Savage\'s Portfolio'
    html = render('projectPage', {
        'pageTitle': page_title,
        'project': project
    })
    filename = get_project_filename(project)
    make_page(filename, html)


def make_project_pages(projects):
    for project in projects:
        make_project_page(project)


"""
def make_research_pages(researchPages):
    for researchPage in researchPages['researchpages']:
        base = copy.copy(HTML_RESEARCH_PAGE)
        researchPage['links'] = format_links(researchPage['links'])
        researchPage['thumbnail'] = format_thumbnail(researchPage['thumb'])
        researchPage['abstract'] = researchPage['abstract'].replace('\n', HTML_BR)
        if researchPage['video'] is not '':
            researchPage['video'] = format_youtube(researchPage['video'])
        formatted = base % researchPage
        f = OUT_DIR + re.sub('[!@#$\' ,:]', '', researchPage['title'].lower()) + '.html'
        f = open(f, 'w+')
        f.write(formatted)
        f.close()
"""


def load_json(fname):
    with open(fname) as jsonFile:
        return json.load(jsonFile)


def main():
    projects = load_json(PROJECTS_FILENAME)
    research = load_json(RESEARCH_FILENAME)
    make_index_page(projects, research)
    make_project_pages(projects)
    #make_research_pages(research)


if __name__ == '__main__':
    main()
