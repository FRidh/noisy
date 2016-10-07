DOCS=doc

.PHONY: docs

docs:
	cd $(DOCS) && $(MAKE) clean && $(MAKE) html

docs-online: docs
	ghp-import -np $(DOCS)/_build/html -r origin

sdist:
	python3 setup.py sdist

release: sdist docs-online
	python3 setup.py upload
