from typing_extensions import assert_never

from ExprParser import ExprParser

INDENT = "  "


class BaseNode:
    def evaluate(self): ...

    def __repr__(self, indent: int = 0) -> str:
        return indent * INDENT + self.__class__.__name__


class Statement(BaseNode): ...


class Expr(BaseNode): ...


class PrintExprStatement(Statement):
    expr: Expr

    def evaluate(self):
        return self.expr.evaluate()

    def __init__(self, expr: Expr):
        self.expr = expr

    def __repr__(self, indent: int = 0) -> str:
        indent_str = indent * INDENT
        _repr = [self.__class__.__name__, self.expr.__repr__(indent + 1)]

        _str = "\n".join(map(lambda x: indent_str + x, _repr))
        return _str


class BlankStatement(Statement):
    def evaluate(self):
        return None


class ArithmeticMulDiv(Expr):
    lhs_child: Expr
    rhs_child: Expr

    def evaluate(self):
        # TODO: process them separately
        match self.op_type:
            case ExprParser.MUL:
                return self.lhs_child.evaluate() * self.rhs_child.evaluate()
            case ExprParser.DIV:
                return self.lhs_child.evaluate() / self.rhs_child.evaluate()

    def __init__(self, lhs_child: Expr, rhs_child: Expr, op_type):
        self.lhs_child = lhs_child
        self.rhs_child = rhs_child
        self.op_type = op_type

    def __repr__(self, indent: int = 0) -> str:
        indent_str = indent * INDENT
        _repr = [self.__class__.__name__]

        _repr.append(self.lhs_child.__repr__(indent + 1))
        _repr.append(self.rhs_child.__repr__(indent + 1))

        _str = "\n".join(map(lambda x: indent_str + x, _repr))
        return _str


class ArithmeticAddSub(Expr):
    lhs_child: Expr
    rhs_child: Expr

    def evaluate(self):
        match self.op_type:
            case ExprParser.ADD:
                return self.lhs_child.evaluate() + self.rhs_child.evaluate()
            case ExprParser.SUB:
                return self.lhs_child.evaluate() - self.rhs_child.evaluate()

    def __init__(self, lhs_child: Expr, rhs_child: Expr, op_type):
        self.lhs_child = lhs_child
        self.rhs_child = rhs_child
        self.op_type = op_type

    def __repr__(self, indent: int = 0) -> str:
        indent_str = indent * INDENT
        _repr = [f"{self.__class__.__name__}({self.op_type})"]

        _repr.append(self.lhs_child.__repr__(indent + 1))
        _repr.append(self.rhs_child.__repr__(indent + 1))

        _str = "\n".join(map(lambda x: indent_str + x, _repr))
        return _str


class Negative(Expr):
    child: Expr

    def evaluate(self):
        return -self.child.evaluate()

    def __init__(self, child: Expr):
        self.child = child

    def __repr__(self, indent: int = 0) -> str:
        indent_str = indent * INDENT
        _repr = [self.__class__.__name__, self.child.__repr__(indent + 1)]

        _str = "\n".join(map(lambda x: indent_str + x, _repr))
        return _str


class Int(Expr):
    value: int

    def evaluate(self):
        return self.value

    def __init__(self, value: int):
        self.value = value

    def __repr__(self, indent: int = 0) -> str:
        return f"{indent * INDENT}{self.__class__.__name__}({self.value})"


class AST(BaseNode):
    statement: Statement

    def evaluate(self):
        return self.statement.evaluate()

    def __init__(self, statement: Statement):
        self.statement = statement

    def __repr__(self, indent: int = 0) -> str:
        return self.statement.__repr__(indent)


def build_expr(ctx):
    match type(ctx):
        case ExprParser.ParensContext:
            return build_expr(ctx.expr())
        case ExprParser.NegativeContext:
            return Negative(build_expr(ctx.expr()))
        case ExprParser.ArithmeticMulDivContext:
            return ArithmeticMulDiv(
                lhs_child=build_expr(ctx.expr(0)),
                rhs_child=build_expr(ctx.expr(1)),
                op_type=ctx.op.type,
            )
        case ExprParser.ArithmeticAddSubContext:
            return ArithmeticAddSub(
                lhs_child=build_expr(ctx.expr(0)),
                rhs_child=build_expr(ctx.expr(1)),
                op_type=ctx.op.type,
            )
        case ExprParser.IntContext:
            return Int(value=int(ctx.INT().getText()))
        case _:
            assert_never(ctx.op.type)


def build_statement(ctx):
    match type(ctx):
        case ExprParser.PrintExprContext:
            return PrintExprStatement(expr=build_expr(ctx.expr()))
        case ExprParser.BlankContext:
            return BlankStatement()
        case _:
            assert_never(ctx)


def build(ctx):
    return AST(statement=build_statement(ctx))
