.DEFAULT_GOAL := help

# Generates a help message. Borrowed from https://github.com/pydanny/cookiecutter-djangopackage.
help: ## Display this help message
	@echo "Please use \`make <target>' where <target> is one of the following tasks:"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

include Makefiles/*.mk

# Tasks to be run in developer shell
## Python requirements
compile-requirements: ## Compile Python requirements without upgrading
	docker-compose run --rm app make pip-compile

upgrade-requirements: ## Compile and upgrade Python requirements
	docker-compose run --rm app make pip-compile-upgrade

## Docker
dev-build: ## Build development images
	docker-compose build --pull

dev-up: ## Start development environment
	docker-compose up -d

dev-down: ## Destroy development environment
	docker-compose down

dev-ps: ## View development environment containers
	docker-compose ps

dev-restart: dev-down dev-up dev-ps ## Restart development environment

# TODO
# dev-setup: dev-docker-pull dev-build dev-up dev-db-restore dev-sync-media dev-ps
