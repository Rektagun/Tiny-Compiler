import sys
from lexer import *

# Parser object keeps track of current token and checks if the code matches the grammar.
# Parser Class
class Parser:
    def __init__(self, lexer):
        pass

# Return true if the current token matches.
    def checkToken(self, kind):
        pass

# Return true if the next token matches.
    def peekToken(self, kind):
        pass

# Try to match current token. If not, error. Advances the current token.
    def matchToken(self, kind):
        pass

# Advances the current token.
    def nextToken(self):
        pass

# Error message.
    def abort(self, message):
        sys.exit("Error:" + message)
