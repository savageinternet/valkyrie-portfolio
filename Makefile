all: npm less pyth copy

npm: package.json
	npm install

less: npm
	mkdir -p build/css
	./node_modules/less/bin/lessc less/style.less build/css/style.css
	./node_modules/less/bin/lessc less/projectPage.less build/css/projectPage.css
	./node_modules/less/bin/lessc less/researchPage.less build/css/researchPage.css

pyth: htmlize.py
	python htmlize.py

copy: pyth less
	cp -r favicon.ico fonts img js robots.txt build

run:
	cd build && python -m http.server

clean:
	rm -r build
