grammar Expr;

stat:   expr NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

expr:   '(' expr ')'                # parens
    |   '-' expr                    # negative
    |   expr op=('*'|'/') expr      # arithmeticMulDiv
    |   expr op=('+'|'-') expr      # arithmeticAddSub
    |   INT                         # int
    ;

ADD :   '+' ;
SUB :   '-' ;
MUL :   '*' ;
DIV :   '/' ;
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS : [ \t\n\r]+ -> skip ;