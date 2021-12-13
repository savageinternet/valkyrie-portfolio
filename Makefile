all: npm less pyth copy

npm: package.json
	npm install

less: npm
	mkdir -p build/css
	./node_modules/less/bin/lessc less/style.less build/css/style.css
	./node_modules/less/bin/lessc less/projectPage.less build/css/projectPage.css
	./node_modules/less/bin/lessc less/researchPage.less build/css/researchPage.css

pyth: requirements.txt htmlize.py
	pip3 install -r requirements.txt
	mkdir -p img/none/
	python3 htmlize.py

copy: pyth less
	cp -r google2ef4f2b4bcd33bf5.html favicon.ico fonts img js papers robots.txt build

run:
	cd build && python3 -m http.server

clean:
	rm -r build
