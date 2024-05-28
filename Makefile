fix:
	ruff format  src videomaker manage.py
	ruff check --fix --show-fixes  src videomaker manage.py

check:
	ruff format --check  src videomaker manage.py
	ruff check  src videomaker manage.py
	mypy  src videomaker manage.py
