from abc import abstractmethod
from typing import Optional

from typing_extensions import assert_never

from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class BaseNode:
    @abstractmethod
    def evaluate(self): ...

    def __repr__(self, indent: int = 0) -> str:
        return indent * "  " + self.__class__.__name__


class Node(BaseNode):
    lhs_child: Optional[BaseNode] = None
    rhs_child: Optional[BaseNode] = None

    def __repr__(self, indent: int = 0) -> str:
        indent_str = indent * "  "
        _repr = [self.__class__.__name__]
        if self.lhs_child is not None:
            _repr.append(self.lhs_child.__repr__(indent + 1))
        if self.rhs_child is not None:
            _repr.append(self.rhs_child.__repr__(indent + 1))

        _str = "\n".join(map(lambda x: indent_str + x, _repr))
        return _str


class NumberNode(Node):
    value: float

    def __init__(self, value: float):
        self.value = value

    def evaluate(self):
        return self.value

    def __repr__(self, indent: int = 0) -> str:
        return f"{indent * '  '}{self.__class__.__name__}({self.value})"


class OperatorNode(Node):
    def __init__(self, lhs_child: BaseNode, rhs_child: Optional[BaseNode] = None):
        self.lhs_child = lhs_child
        self.rhs_child = rhs_child

    @abstractmethod
    def apply_operation(self, lhs, rhs):
        pass

    def evaluate(self):
        rhs = self.rhs_child.evaluate() if self.rhs_child else None
        return self.apply_operation(self.lhs_child.evaluate(), rhs)


class AddOperationNode(OperatorNode):
    def apply_operation(self, lhs, rhs):
        return lhs + rhs


class SubOperationNode(OperatorNode):
    def apply_operation(self, lhs, rhs):
        return lhs - rhs


class MulOperationNode(OperatorNode):
    def apply_operation(self, lhs, rhs):
        return lhs * rhs


class DivOperationNode(OperatorNode):
    def apply_operation(self, lhs, rhs):
        return lhs / rhs


class NegativeOperationNode(OperatorNode):
    def apply_operation(self, lhs, rhs):
        return -lhs


class ASTBuilderVisitor(ExprVisitor):
    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx: ExprParser.PrintExprContext):
        # takes some expressoion as context, visit it and then print its value
        node = self.visit(ctx.expr())
        return node

    # visit #blank just the same as in the codegen

    # Visit a parse tree produced by ExprParser#negative.
    def visitNegative(self, ctx: ExprParser.NegativeContext):
        child = self.visit(ctx.expr())
        node = NegativeOperationNode(lhs_child=child)
        return node

    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx: ExprParser.ParensContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ExprParser#arithmetic.
    def visitArithmetic(self, ctx: ExprParser.ArithmeticContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        match ctx.op.type:  # type: ignore
            case ExprParser.ADD:
                return AddOperationNode(left, right)
            case ExprParser.SUB:
                return SubOperationNode(left, right)
            case ExprParser.MUL:
                return MulOperationNode(left, right)
            case ExprParser.DIV:
                return DivOperationNode(left, right)
            case _:
                assert_never(ctx.op.type)  # type: ignore

    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx: ExprParser.IntContext):
        return NumberNode(value=float(ctx.INT().getText()))
