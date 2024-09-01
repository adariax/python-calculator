init:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt
	@echo "\n\033[0;32mYour dev environment is ready!\033[0m\n"

prepare:
	. venv/bin/activate; antlr4 -visitor -no-listener -Dlanguage=Python3 Expr.g4

run:
	. venv/bin/activate; PYTHONPATH=. python app/main.py

format:
	( \
		. venv/bin/activate; \
		isort app; \
		black app; \
	)

lint-check:
	. venv/bin/activate; flake8 app; pylint app; refurb --enable-all app

typecheck:
	. venv/bin/activate; pyright app