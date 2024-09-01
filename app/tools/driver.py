import sys

from antlr4 import CommonTokenStream, InputStream

from ExprLexer import ExprLexer
from ExprParser import ExprParser

from .visitor import Visitor


def driver():
    while True:
        input_stream = InputStream(sys.stdin.readline())

        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.start()

        # lisp_tree_str = tree.toStringTree(recog=parser)
        # print(lisp_tree_str)

        visitor = Visitor()
        visitor.visit(tree)
