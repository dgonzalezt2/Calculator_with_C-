#Tokens del programa

INTEGER, PLUS, MINUS, MUL, DIV, POW, SQRT, MOD, SIN, COS, SMLL, BIGG, EQL,LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV','POW', 'SQRT', 'MOD', 'SIN', 'COS', '<', '>','=','(', ')', 'EOF'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
