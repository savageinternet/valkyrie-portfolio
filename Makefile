all: npm copy pyth

npm: package.json
	npm install

pyth:
	python htmlize.py

copy: build/css/style.css build/content/projects.html build/index.html
	cp -r favicon.ico fonts img js robots.txt build

build/css/style.css: less/style.less
	mkdir -p build/css
	./node_modules/less/bin/lessc less/style.less build/css/style.css

build/content/projects.html: content/projects.json content/projects.mustache
	mkdir -p build/content
	./node_modules/mustache/bin/mustache content/projects.json content/projects.mustache > build/content/projects.html

build/index.html: index.html.tpl build/content/projects.html
	sed -e '/{PROJECTS}/{r build/content/projects.html' -e 'd}' index.html.tpl > build/index.html

run:
	cd build && python -m http.server

clean:
	rm -r build
