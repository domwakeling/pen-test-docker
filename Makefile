help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

update: ## Run apt update
	sudo apt update

makeenv: ## Make a local Python environment in the env folder
	python3 -m venv env

docker-build: ## Re-build container
	docker build -t domwakeling/pen-test .

docker-run: ## Start container
	docker run -it domwakeling/pen-test