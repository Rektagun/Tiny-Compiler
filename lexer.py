import enum
import sys

class Lexer:
    def __init__(self, source):

        # Source code to lex as a string. 
        # Append a newline to simplify lexing/parsing the last token/statement.
        self.source = source + '\n' 

        # Current character in the string.
        self.curChar = ''

        # Current position in the string.
        self.curPos = -1

        self.nextChar()

    # Process the next character.
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source): # If the length is bigger of equal
            # to the current position, that will be the end of that file (EOF).

            self.curChar = '\0' #EOF

        else: # If the length in not small, there is something to work with.

            self.curChar = self.source[self.curPos] # Like an arrays index,
            # it's setting the current char to the current position in of the 
            # source code.


    # Process lookahead character.
    # This increments the lexer's current position and updates the 
    # current character. 
    # If we reach the end of the input, set the character to the 
    # end-of-file marker. 
    # This is the only place we will modify curPos and curChar.
    # But sometimes we want to look ahead to the next character 
    # without updating curPos:

    def lookAhead(self):
        if self.curPos >= len(self.source):
            return '\0'
        else:
            return self.source[self.curPos+1]


    # Invalid token found, return message and exit.
    def invToken(self, error):
        sys.exit("Lexing error: "+ error)

    # Skip whitespaces excepte newlines, which indicate EOL.
    def skipSpace(self):

        while self.curChar == " " or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

        pass

    # Skip comments in the code.
    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

    # Id and Return the next token
    def tokenId(self):

        self.skipSpace()
        self.skipComment()

        token = None

        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '=':

            if self.lookAhead == '=':
                lastChar = self.curChar
                self.nextChar();
                token = Token(lastChar + self.curChar, TokenType.EQEQ)

            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)

        elif self.curChar == '>':

            if self.lookAhead == '=':
                lastChar = self.curChar
                self.nextChar();
                token = Token(lastChar + self.curChar, TokenType.GTEQ)

            else:
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '<':

            if self.lookAhead == '=':
                lastChar = self.curChar
                self.nextChar();
                token = Token(lastChar + self.curChar, TokenType.LTEQ)

            else:
                token = Token(self.curChar, TokenType.LT)

        elif self.curChar == '!':
            if self.lookAhead() == '=':
                lastChar = self.curChar
                self.nextChar();
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.invToken("Expected !=, got !" + self.lookAhead())

        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.invToken("Invalid string token!")
                self.nextChar()

            tokText = self.source[startPos : self.curPos]
            token = Token(tokText, TokenType.STRING)

            ##################################
            #  NUMBERS IDENTIFY
            ##################################

        elif self.curChar.isdigit():
            # Leading character is a digit, so this must be a number.
            # Get all consecutive digits and decimal if there is one.
            startPos = self.curPos
            while self.lookAhead().isdigit():
                self.nextChar()
            if self.lookAhead() == '.': # Decimal!
                self.nextChar()

                # Must have at least one digit after decimal.
                if not self.lookAhead().isdigit():
                    self.invToken("Not proper number!: " + self.curChar)
                # Error!
                while self.lookAhead().isdigit():
                    self.nextChar()

            tokText = self.source[startPos : self.curPos + 1]
            token = Token(tokText, TokenType.NUMBER)



        elif self.curChar.isalpha():
            # Leading character is a letter, so this must be an identifier or a keyword.
            # Get all consecutive alpha numeric characters.
            startPos = self.curPos
            while self.lookAhead().isalnum():
                self.nextChar()

            # Check if the token is in the list of keywords.
            tokText = self.source[startPos : self.curPos + 1] # Get the substring.
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None: # Identifier
                token = Token(tokText, TokenType.IDENT)
            else:   # Keyword
                token = Token(tokText, keyword)




        elif self.curChar == '\0':
            token = Token('', TokenType.EOF)

        else:
            self.invToken('Uknown token: '+ self.curChar)
        self.nextChar()

        return token


# For now:

# Token contains the original text and the type of token.
class Token:   

    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None




# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # Operators.
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211


