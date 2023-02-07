from Token import *

class Lexer(object):
    
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  
        else:
            self.current_char = self.text[self.pos]

    def space(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.space()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '!':
                self.advance()
                return Token(POW, '!')

            if self.current_char == '#':
                self.advance()
                return Token(SQRT, '#')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            if self.current_char == '%':
                self.advance()
                return Token(MOD, '%')
                
            if self.current_char == 'º':
                self.advance()
                return Token(SIN, 'º')

            if self.current_char == 'ª':
                self.advance()
                return Token(COS, 'ª')

            if self.current_char == '<':
                self.advance()
                return Token(SMLL, '<')

            if self.current_char == '>':
                self.advance()
                return Token(BIGG, '>')

            if self.current_char == '=':
                self.advance()
                return Token(EQL, '=')

            else: 
                raise Exception('Error')

        return Token(EOF, None)