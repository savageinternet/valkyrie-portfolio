HTML_LINK = '''<a href="%(href)s">%(title)s</a>'''
HTML_IMG = '''<img src="%(src)s" />'''
HTML_BR = '''<br/>'''
HTML_YOUTUBE = '''<iframe width="560" height="315" src="%(video)s" frameborder="0" allowfullscreen></iframe>'''

HTML_PROJECT_PAGE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>%(title)s - Valkyrie Savage's Portfolio</title>
<meta name="description" content="Valkyrie Savage works in physical, digital, visual, gameful, and educational prototyping and design." />
<meta name="robots" content="index, follow">
<link rel="stylesheet" type="text/css" href="/css/style.css" />
</head>
<body>
<div id="root">
  <div id="header">
    <div id="logo">
      <a href="/"><img src="/img/logo.svg" /></a>
      <div id="topbar-text">Valkyrie A. Savage</div>
    </div>
    <div id="nav">
      <a href="/#about">About</a>
      <a href="/#portfolio">Portfolio</a>
      <a href="/#research">Research</a>
      <a href="/#contact">Contact</a>
    </div>
  </div>
  <div id="body">
    <div id="main">
      <div id="thumbnail">
        %(thumbnail)s
      </div>
      <div id="info">
        <div id="title">%(title)s</div>
        <div id="deliverable">%(deliverable)s</div>
        <div id="client">%(client)s</div>
        <div id="links">%(links)s</div>
      </div>
      <div id="description" class="dark-bg">
        %(description)s
      </div>
      <div id="images">
        %(images)s
      </div>
    </div>
  </div>
</div>
</body>
</html>'''

HTML_RESEARCH_PAGE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>%(title)s - Valkyrie Savage's Research</title>
<meta name="description" content="Valkyrie Savage works in physical, digital, visual, gameful, and educational prototyping and design." />
<meta name="robots" content="index, follow">
<link rel="stylesheet" type="text/css" href="/css/style.css" />
</head>
<body>
<div id="root">
  <div id="header">
    <div id="logo">
      <a href="/"><img src="/img/logo.svg" /></a>
      <div id="topbar-text">Valkyrie A. Savage</div>
    </div>
    <div id="nav">
      <a href="/#about">About</a>
      <a href="/#portfolio">Portfolio</a>
      <a href="/#research">Research</a>
      <a href="/#contact">Contact</a>
    </div>
  </div>
  <div id="body">
    <div id="main">
      <div id="thumbnail">
        %(thumbnail)s
      </div>
      <div id="info">
        <div id="title">%(title)s</div>
        <div id="authors">%(authors)s</div>
        <div id="venue">%(venue)s</div>
        <div id="links">%(links)s</div>
      </div>
      <div id="abstract" class="dark-bg">
        %(abstract)s
      </div>
      <div id="video">
        %(video)s
      </div>
    </div>
  </div>
</div>
</body>
</html>'''
