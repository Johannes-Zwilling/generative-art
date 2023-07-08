activate_venv: # Activate the virtual environment for python
	source .venv/bin/activate

install:
	pip install -r requirements.txt; \
	pip install -e .