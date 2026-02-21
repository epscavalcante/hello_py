format:
	uv run black .

lint:
	uv run flake8 .

type:
	uv run mypy .

test:
	uv run pytest

quality: format lint type test