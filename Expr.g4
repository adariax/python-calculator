grammar Expr;

start:  expr NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/'|'+'|'-') expr      # arithmetic
    |   '-' expr                    # negative
    |   INT                         # int
    |   '(' expr ')'                # parens
    ;

ADD :   '+' ;
SUB :   '-' ;
MUL :   '*' ;
DIV :   '/' ;
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS : [ \t\n\r]+ -> skip ;