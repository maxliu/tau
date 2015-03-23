import sys
from antlr4 import *
from muLexer import muLexer as Lexer
from muParser import muParser as Parser
from visitor_exe import visitorExe as Visitor
import pdb

def main(argv):
    input = FileStream(argv[1])
    lexer = Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.parse()
    visitor = Visitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
