.PHONY: help run docker update

help:
	@echo "Help"
	@echo "  help   - Displays this message"
	@echo "  docker - Builds and run docker"
	@echo "  run    - Runs locally"
	@echo "  update - Updates songs list"

run:
	python main.py

docker:
	docker build -t python:test .
	docker run -p 80:3000 --rm -it -v $PWD:/src python:test

update:
	git pull
	python support/md2csv.py < support/favorites.md
	git add favorites.csv support/favorites.md
	git commit -m "Update songs"
	git push
