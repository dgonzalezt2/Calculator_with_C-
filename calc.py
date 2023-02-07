from Token import *
from Scanner import *
from Parser import *
import math

class NodeVisitor(object):

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__ 
        visitor = getattr(self, method_name)
        return visitor(node)
        
class Interpreter(NodeVisitor):
    
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
            
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

        elif node.op.type == POW:
            return self.visit(node.left) ** self.visit(node.right)

        elif node.op.type == SQRT:
            return self.visit(node.right) ** (1/2)

        elif node.op.type == MOD:
            return self.visit(node.left) % self.visit(node.right)

        elif node.op.type == SIN:
            return math.sin(self.visit(node.right))

        elif node.op.type == COS:
            return math.cos(self.visit(node.right))

        elif node.op.type == BIGG:
            if(self.visit(node.left) > self.visit(node.right)):
                return 1
            else:
                return 0

        elif node.op.type == SMLL:
            if(self.visit(node.left) < self.visit(node.right)):
                return 1
            else:
                return 0

        elif node.op.type == EQL:
            if(self.visit(node.left) == self.visit(node.right)):
                return 1
            else:
                return 0

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit_BinOp(tree)


def Calc():

    txt = input('Escriba una expresion -> ')

    lexer = Lexer(txt)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print('Resultado de la expresion -> ',result)


if __name__ == '__main__':
    Calc()