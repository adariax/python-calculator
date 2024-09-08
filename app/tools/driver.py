import sys

from antlr4 import CommonTokenStream, InputStream

from ExprLexer import ExprLexer
from ExprParser import ExprParser

from .ast import ASTBuilderVisitor
from .visitor import Visitor


def driver():
    while True:
        input_stream = InputStream(sys.stdin.readline())

        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.start()

        visitor = Visitor()
        visitor.visit(tree)

        ast = ASTBuilderVisitor()
        print(ast.visit(tree))
