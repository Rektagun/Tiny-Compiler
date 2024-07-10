from lexer import *

def main ():
    # Test String
    source = 'IF+-123 foo*THEN l'

    lexer = Lexer(source)

    token = lexer.tokenId()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.tokenId()

main()

