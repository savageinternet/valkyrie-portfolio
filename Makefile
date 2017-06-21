all: npm copy pyth build/css/style.css

npm: package.json
	npm install

pyth: htmlize.py
	python htmlize.py

copy: pyth build/css/style.css
	cp -r favicon.ico fonts img js robots.txt build

build/css/style.css: less/style.less
	mkdir -p build/css
	./node_modules/less/bin/lessc less/style.less build/css/style.css

run:
	cd build && python -m http.server

clean:
	rm -r build
