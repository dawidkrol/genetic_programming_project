grammar gramatyka;

INT     :   '-'? [0-9]+'.'? [0-9]* ;
STRING  :   [a-zA-Z][a-zA-Z0-9_]* ;
NEWLINE :   [\r\n]+ ;
WS      :   [ \t]+ -> skip ;

prog
    :   (statement|NEWLINE*) (NEWLINE* statement)* NEWLINE*
    ;

statement
    :   printStatement';'
    |   inputStatement';'
    |   outputStatement';'
    |   ifStatement
    |   while
    |   variableAssignment';'
    ;
name
    :   STRING
    ;

printStatement
    :   'print ' (expression)
    ;

inputStatement
    :   'input ' STRING
    ;

outputStatement
    :   'output ' expression
    ;

ifStatement
    :   'if ' comparison codeBlock
    (   ' else ' codeBlock )?
    ;

while
    :   'while ' comparison codeBlock
    ;

variableAssignment
    :   name '=' expression
    ;

comparison
    :   expression ('=='|'!='|'<'|'>'|'<='|'>=') expression
    |   comparison (' and '|' or ') comparison
    ;
expression
    :   INT
    |   name
    |   '(' expression ')'
    |   expression ('*'|'/'|'+'|'-') expression
    ;

codeBlock
    :   '{' NEWLINE* prog NEWLINE* '}'
    ;


