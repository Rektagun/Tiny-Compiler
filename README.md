the main lexer rules for the Teeny Tiny language:

Operator. One or two consecutive characters that matches: + - * / = == != > < >= <=
String. Double quotation followed by zero or more characters and a double quotation. Such as: "hello, world!" and ""
Number. One or more numeric characters followed by an optional decimal point and one or more numeric characters. Such as: 15 and 3.14
Identifier. An alphabetical character followed by zero or more alphanumeric characters.
Keyword. Exact text match of: LABEL, GOTO, PRINT, INPUT, LET, IF, THEN, ENDIF, WHILE, REPEAT, ENDWHILE
