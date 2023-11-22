grammar gramatyka;

INT     :   '-'? [0-9]+ ;
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
    |   forStatement
    |   variableDeclaration';'
    |   variableAssignment';'
    |   functionDefinition
    |   functionCall
    ;

printStatement
    :   'print ' STRING
    ;

inputStatement
    :   'input ' STRING
    ;

outputStatement
    :   'output ' STRING
    ;

ifStatement
    :   'if ' expression codeBlock
    (   ' else ' codeBlock )?
    ;

forStatement
    :   'for ' STRING ' in ' expression codeBlock
    ;

variableDeclaration
    :   'final '?'var ' STRING '=' expression
    ;

variableAssignment
    :   STRING '=' expression
    ;

functionDefinition
    :   'function ' STRING '(' parameterList? ')' codeBlock
    ;
functionCall
    :   STRING '(' parameterList? ');'
    ;
parameterList
    :   STRING (',' STRING)*
    ;

expression
    :   INT
    |   STRING
    |   '(' expression ')'
    |   expression ('*'|'/'|'+'|'-'|'=='|'!='|'<'|'>'|'<='|'>=') expression
    ;

codeBlock
    :   '{' NEWLINE* prog NEWLINE* '}'
    ;


