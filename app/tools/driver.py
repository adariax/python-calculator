import sys

from antlr4 import CommonTokenStream, InputStream

from ExprLexer import ExprLexer
from ExprParser import ExprParser

from .ast import build
from .visitor import Visitor


def driver():
    while True:
        input_stream = InputStream(sys.stdin.readline())

        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.stat()

        visitor = Visitor()
        visitor.visit(tree)

        ast = build(tree)
        print(ast)
        print(ast.evaluate())
