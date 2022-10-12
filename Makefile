PYTHON := ${shell whereis -b python | cut -d " " -f2}

update:
		@git pull

run:	update
		@$(PYTHON) main.py
