DOCS=doc

.PHONY: docs clean

docs:
	cd $(DOCS) && $(MAKE) clean && $(MAKE) html

docs-online: docs
	ghp-import -np $(DOCS)/_build/html -r origin

sdist:
	python3 setup.py sdist

clean:
	rm -rf dist

release: docs-online
	python3 setup.py sdist upload
	$(MAKE) clean
