install:
	poetry install

build:
	poetry build	

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

check:
	poetry run flake8 gendiff
	poetry run pytest