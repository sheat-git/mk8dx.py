.PHONY: deploy
deploy:
	twine upload dist/*

.PHONY: test-deploy
test-deploy:
	twine upload -r testpypi dist/*

.PHONY: build
build:
	python setup.py bdist_wheel

.PHONY: clean
clean:
	rm -r dist/* build/* mk8dx.egg-info/*
