from lexer import *
from parser import *
import sys

def main ():

    print("TTC")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument")

    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()


    lexer = Lexer(source)
    parser = Parser(lexer)

    # token = lexer.tokenId()
    parser.program()
    print("Parsing completed")

    # while token.kind != TokenType.EOF:
    #     print(token.kind)
    #     token = lexer.tokenId()

main()

