<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Valkyrie Savage - Designer</title>
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
      <div id="hero">
        <img src="img/header.jpg">
        <div id="name">Valkyrie A. Savage</div>
      </div>
      <div id="about" class="dark-bg">
        <div class="header">ABOUT</div>
        <div class="bodytext">I craft delightful experiences. With a proven track record in research, visual design, physical design and fabrication, teaching, game design, electronics, and coding, I enjoy projects which let me interlink multiple areas of practice.</div>
        <div class="left">Education: PhD, Human Computer Interaction, UC Berkeley</div>
        <div class="right">Current Work: CEO, Co-founder, and Designer at <a href="https://savageinter.net">Savage Internet</a></div>
        <div class="center">Personal: <a href="/personal.html">Blogroll and Travel Timeline</a></div>
      </div>
      <div id="portfolio" class="light-bg">
        <div class="header">PORTFOLIO</div>
        <div id="tags">
          <span class="tag">Digital</span>
          <span class="tag">Physical</span>
          <span class="tag">Visual</span>
          <span class="tag">Gameful</span>
          <span class="tag">Educational</span>
          <span class="tag">Mobile</span>
          <span class="tag">Web</span>
        </div>
        <div id="projects">
          {PROJECTS}
        </div>
        <div id="project_details" class="hide">
          <div id="project_details_wrapper">
            <div id="project_details_title"></div>
            <div id="project_details_description"></div>
          </div>
        </div>
      </div>
      <div id="research" class="dark-bg">
        <div class="header">RESEARCH</div>
        <div class="bodytext">My thesis research, supervised by Björn Hartmann, focused on digital  fabrication and how we can leverage its potential to make prototyping input devices a faster and easier process: this culminated in my dissertation, entitled <a href="/papers/thesis.pdf">“Fabbed to Sense: Integrated Design of Geometry and Sensing for Interactive Objects.”</a> <a href="https://www.youtube.com/watch?v=SgZUxloEo4s">A video of my thesis presentation</a> is also available online.<br/><br/>

        In the course of doing my own research, I supervised research projects for Masters students and undergraduates. I also taught UC Berkeley’s <a href="cs160.valkyriesavage.com">Introduction to User Interface Design</a> course in Summer 2015 and redesigned the curriculum to incorporate a new technology, replace roughly half the lectures with a studio component, and fit with the summer session.
        </div>
        <div id="research">
          {RESEARCH}
        </div>
      </div>
      <div id="contact" class="light-bg">
        <div class="header">CONTACT</div>
        <img src="img/map.jpg">
        <div id="card">
          <div class="center">Have a project idea? Just want to talk? Get in touch!</div>
          <div class="left">digital coordinates:</div>
          <div class="right">
            <a href="mailto:valkyrie@savageinter.net">valkyrie@savageinter.net</a><br/>
            <a href="https://facebook.com/valkyrie">facebook.com/valkyrie</a><br/>
	    <a href="https://linkedin.com/in/valkyrie">linkedin.com/in/valkyrie</a><br/>
	    <a href="https://github.com/valkyriesavage">github.com/valkyriesavage</a><br/>
          </div>
          <div class="left">physical coordinates:</div>
          <div class="right">860 St. Clarens Ave.<br/>Toronto, ON M6H 3X6<br/>Canada</div>
      </div>
    </div>
  </div>
</div>
<script src="/js/index.js"></script>
</body>
</html>
