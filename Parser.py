from Token import *
from Scanner import *

class AST(object):
    pass 
    
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def nxt(self, token_type):

        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else: 
            raise Exception('Invalid character')

    def FIN(self):
        token = self.current_token
        if token.type == INTEGER:
            self.nxt(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.nxt(LPAREN)
            node = self.expr()
            self.nxt(RPAREN)
            return node

    def expr(self):
        node = self.FIN()

        while self.current_token.type in (PLUS, MINUS, POW, MUL, DIV, SQRT, MOD, SIN, COS, BIGG, SMLL, EQL):
            token = self.current_token
            if token.type == PLUS:
                self.nxt(PLUS)
            elif token.type == MINUS:
                self.nxt(MINUS)
            elif token.type == MUL:
                self.nxt(MUL)
            elif token.type == DIV:
                self.nxt(DIV)
            elif token.type == POW:
                self.nxt(POW)     
            elif token.type == SQRT:
                self.nxt(SQRT)        
            elif token.type == MOD:
                self.nxt(MOD)  
            elif token.type == SIN:
                self.nxt(SIN)
            elif token.type == COS:
                self.nxt(COS)  
            elif token.type == SMLL:
                self.nxt(SMLL)
            elif token.type == BIGG:
                self.nxt(BIGG)  
            elif token.type == EQL:
                self.nxt(EQL) 

            node = BinOp(left=node, op=token, right=self.FIN())

        return node

    def parse(self):
        return self.expr()