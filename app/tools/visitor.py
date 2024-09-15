from typing_extensions import assert_never

from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class Visitor(ExprVisitor):
    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx: ExprParser.PrintExprContext):
        # takes some expressoion as context, visit it and then print its value
        value = self.visit(ctx.expr())
        print(value)

    # visit #blank just the same as in the codegen

    # Visit a parse tree produced by ExprParser#negative.
    def visitNegative(self, ctx: ExprParser.NegativeContext):
        return -self.visit(ctx.expr())

    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx: ExprParser.ParensContext):
        # just visit + parse expression inside
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ExprParser#arithmeticMulDiv.
    def visitArithmeticMulDiv(self, ctx: ExprParser.ArithmeticMulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        match ctx.op.type:  # type: ignore
            case ExprParser.MUL:
                return left * right
            case ExprParser.DIV:
                return left / right
            case _:
                assert_never(ctx.op.type)  # type: ignore

    # Visit a parse tree produced by ExprParser#arithmeticAddSub.
    def visitArithmeticAddSub(self, ctx: ExprParser.ArithmeticAddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        match ctx.op.type:  # type: ignore
            case ExprParser.ADD:
                return left + right
            case ExprParser.SUB:
                return left - right
            case _:
                assert_never(ctx.op.type)  # type: ignore

    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx: ExprParser.IntContext):
        # return context parsed to int
        return int(ctx.INT().getText())
