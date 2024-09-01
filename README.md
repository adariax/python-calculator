# python-calculator
manual implementation - part of diploma

[REFERENCE](https://github.com/jszheng/py3antlr4book/tree/master/04-Calc)

## Calculator
process `+`, `*`, `-`, `/` (without handling "division by zero")

## Make

### `make init`
- setup for work: creates `venv` + installs all dependencies in it

### `make prepare`
- build: antlr4 tool generates parser and other files using grammar in `Expr.g4` file

### `make run`
- runs line-by-line REPL calculator (ends with `Ctrl+C`)
