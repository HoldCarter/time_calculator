install:
	poetry install
build:
	poetry build
package-install:
	pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 time_calc
