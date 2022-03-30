.PHONY: run clean venv build zip run
.DEFAULT_GOAL := help
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

help:  ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

venv: ## Creates virtual enviroment (if it does not exist) and installs requirements.
	if [ ! -d  $(VENV) ]; then python3 -m venv $(VENV); fi
	. $(VENV)/bin/activate
	$(PIP) install --upgrade -r requirements.txt

run: build zip ## Runs command that produces the manifest file and zips it with the templates.

build:  ## Runs command that produces the manifest file in the output directory ans zips it.
	. $(VENV)/bin/activate
	$(PIP) list | grep aws-control-tower-manifest-builder
	if $(VENV)/bin/aws_control_tower_manifest_builder --default-region us-east-2 --input-cf input-cf-templates --input-scp input-scps --abort-if-error TRUE --output . ; then \
		echo "Manifest produced succesfully"; \
	else \
		echo "Failed to produce manifest"; \
		exit 1; \
	fi

zip: ## Zips the contents in custom-control-tower-configuration.zip 
	zip -r custom-control-tower-configuration.zip manifest.yaml input-cf-templates input-scps

clean: ## Removes __pycache and virtual environment 
	rm -rf __pycache__
	rm -rf $(VENV)