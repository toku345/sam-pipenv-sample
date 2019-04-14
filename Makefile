DEPLOY_DIR=./package

prepare-package:
	$(eval VENV = $(shell pipenv --venv))
	cp -r ${VENV}/lib/python3.7/site-packages/* ${DEPLOY_DIR}/
	cp -r proverb/* ${DEPLOY_DIR}/

clean-package:
	rm -rf ${DEPLOY_DIR}/*
