# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .muListener import muListener
    from .muVisitor import muVisitor
else:
    from muListener import muListener
    from muVisitor import muVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"&\u0085\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\3\2\3\2\3\2\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\5\4+\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\7\6\67\n\6\f\6\16\6:\13\6\3\6\3\6\5\6")
        buf.write(u">\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bH\n\b\3\t\3")
        buf.write(u"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\5\f^\n\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\7\fu\n\f\f\f\16\fx\13\f\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\5\r\u0083\n\r\3\r\2\3\26\16\2\4")
        buf.write(u"\6\b\n\f\16\20\22\24\26\30\2\b\3\2\r\17\3\2\13\f\3\2")
        buf.write(u"\7\n\3\2\5\6\3\2!\"\3\2\30\31\u008f\2\32\3\2\2\2\4 \3")
        buf.write(u"\2\2\2\6*\3\2\2\2\b,\3\2\2\2\n\61\3\2\2\2\f?\3\2\2\2")
        buf.write(u"\16G\3\2\2\2\20I\3\2\2\2\22M\3\2\2\2\24S\3\2\2\2\26]")
        buf.write(u"\3\2\2\2\30\u0082\3\2\2\2\32\33\5\4\3\2\33\34\7\2\2\3")
        buf.write(u"\34\3\3\2\2\2\35\37\5\6\4\2\36\35\3\2\2\2\37\"\3\2\2")
        buf.write(u"\2 \36\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\" \3\2\2\2#+\5\b")
        buf.write(u"\5\2$+\5\n\6\2%+\5\20\t\2&+\5\22\n\2\'+\5\24\13\2()\7")
        buf.write(u"&\2\2)+\b\4\1\2*#\3\2\2\2*$\3\2\2\2*%\3\2\2\2*&\3\2\2")
        buf.write(u"\2*\'\3\2\2\2*(\3\2\2\2+\7\3\2\2\2,-\7 \2\2-.\7\23\2")
        buf.write(u"\2./\5\26\f\2/\60\7\22\2\2\60\t\3\2\2\2\61\62\7\33\2")
        buf.write(u"\2\628\5\f\7\2\63\64\7\34\2\2\64\65\7\33\2\2\65\67\5")
        buf.write(u"\f\7\2\66\63\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write(u"\29=\3\2\2\2:8\3\2\2\2;<\7\34\2\2<>\5\16\b\2=;\3\2\2")
        buf.write(u"\2=>\3\2\2\2>\13\3\2\2\2?@\5\26\f\2@A\5\16\b\2A\r\3\2")
        buf.write(u"\2\2BC\7\26\2\2CD\5\4\3\2DE\7\27\2\2EH\3\2\2\2FH\5\6")
        buf.write(u"\4\2GB\3\2\2\2GF\3\2\2\2H\17\3\2\2\2IJ\7\35\2\2JK\5\26")
        buf.write(u"\f\2KL\5\16\b\2L\21\3\2\2\2MN\7\26\2\2NO\5\4\3\2OP\7")
        buf.write(u"\27\2\2PQ\7\37\2\2QR\5\26\f\2R\23\3\2\2\2ST\7\36\2\2")
        buf.write(u"TU\5\26\f\2UV\7\22\2\2V\25\3\2\2\2WX\b\f\1\2XY\7\f\2")
        buf.write(u"\2Y^\5\26\f\13Z[\7\21\2\2[^\5\26\f\n\\^\5\30\r\2]W\3")
        buf.write(u"\2\2\2]Z\3\2\2\2]\\\3\2\2\2^v\3\2\2\2_`\f\f\2\2`a\7\20")
        buf.write(u"\2\2au\5\26\f\rbc\f\t\2\2cd\t\2\2\2du\5\26\f\nef\f\b")
        buf.write(u"\2\2fg\t\3\2\2gu\5\26\f\thi\f\7\2\2ij\t\4\2\2ju\5\26")
        buf.write(u"\f\bkl\f\6\2\2lm\t\5\2\2mu\5\26\f\7no\f\5\2\2op\7\4\2")
        buf.write(u"\2pu\5\26\f\6qr\f\4\2\2rs\7\3\2\2su\5\26\f\5t_\3\2\2")
        buf.write(u"\2tb\3\2\2\2te\3\2\2\2th\3\2\2\2tk\3\2\2\2tn\3\2\2\2")
        buf.write(u"tq\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\27\3\2\2\2")
        buf.write(u"xv\3\2\2\2yz\7\24\2\2z{\5\26\f\2{|\7\25\2\2|\u0083\3")
        buf.write(u"\2\2\2}\u0083\t\6\2\2~\u0083\t\7\2\2\177\u0083\7 \2\2")
        buf.write(u"\u0080\u0083\7#\2\2\u0081\u0083\7\32\2\2\u0082y\3\2\2")
        buf.write(u"\2\u0082}\3\2\2\2\u0082~\3\2\2\2\u0082\177\3\2\2\2\u0082")
        buf.write(u"\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\31\3\2\2\2\13")
        buf.write(u" *8=G]tv\u0082")
        return buf.getvalue()
		

class muParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'||'", u"'&&'", u"'=='", u"'!='", u"'>'", 
                     u"'<'", u"'>='", u"'<='", u"'+'", u"'-'", u"'*'", u"'/'", 
                     u"'%'", u"'^'", u"'!'", u"';'", u"'='", u"'('", u"')'", 
                     u"'{'", u"'}'", u"'true'", u"'false'", u"'nil'", u"'if'", 
                     u"'else'", u"'while'", u"'log'", u"'until'" ]

    symbolicNames = [ u"<INVALID>", u"OR", u"AND", u"EQ", u"NEQ", u"GT", 
                      u"LT", u"GTEQ", u"LTEQ", u"PLUS", u"MINUS", u"MULT", 
                      u"DIV", u"MOD", u"POW", u"NOT", u"SCOL", u"ASSIGN", 
                      u"OPAR", u"CPAR", u"OBRACE", u"CBRACE", u"TRUE", u"FALSE", 
                      u"NIL", u"IF", u"ELSE", u"WHILE", u"LOG", u"UNTIL", 
                      u"ID", u"INT", u"FLOAT", u"STRING", u"COMMENT", u"SPACE", 
                      u"OTHER" ]

    RULE_parse = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_assignment = 3
    RULE_if_stat = 4
    RULE_condition_block = 5
    RULE_stat_block = 6
    RULE_while_stat = 7
    RULE_until_stat = 8
    RULE_log = 9
    RULE_expr = 10
    RULE_atom = 11

    ruleNames =  [ u"parse", u"block", u"stat", u"assignment", u"if_stat", 
                   u"condition_block", u"stat_block", u"while_stat", u"until_stat", 
                   u"log", u"expr", u"atom" ]

    EOF = Token.EOF
    OR=1
    AND=2
    EQ=3
    NEQ=4
    GT=5
    LT=6
    GTEQ=7
    LTEQ=8
    PLUS=9
    MINUS=10
    MULT=11
    DIV=12
    MOD=13
    POW=14
    NOT=15
    SCOL=16
    ASSIGN=17
    OPAR=18
    CPAR=19
    OBRACE=20
    CBRACE=21
    TRUE=22
    FALSE=23
    NIL=24
    IF=25
    ELSE=26
    WHILE=27
    LOG=28
    UNTIL=29
    ID=30
    INT=31
    FLOAT=32
    STRING=33
    COMMENT=34
    SPACE=35
    OTHER=36

    def __init__(self, input):
        super(muParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.ParseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(muParser.BlockContext,0)


        def EOF(self):
            return self.getToken(muParser.EOF, 0)

        def getRuleIndex(self):
            return muParser.RULE_parse

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterParse(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitParse(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = muParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self.block()
            self.state = 25
            self.match(muParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.StatContext)
            else:
                return self.getTypedRuleContext(muParser.StatContext,i)


        def getRuleIndex(self):
            return muParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = muParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << muParser.OBRACE) | (1 << muParser.IF) | (1 << muParser.WHILE) | (1 << muParser.LOG) | (1 << muParser.ID) | (1 << muParser.OTHER))) != 0):
                self.state = 27 
                self.stat()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._OTHER = None # Token

        def assignment(self):
            return self.getTypedRuleContext(muParser.AssignmentContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(muParser.If_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(muParser.While_statContext,0)


        def until_stat(self):
            return self.getTypedRuleContext(muParser.Until_statContext,0)


        def log(self):
            return self.getTypedRuleContext(muParser.LogContext,0)


        def OTHER(self):
            return self.getToken(muParser.OTHER, 0)

        def getRuleIndex(self):
            return muParser.RULE_stat

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterStat(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitStat(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = muParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 40
            token = self._input.LA(1)
            if token in [muParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33 
                self.assignment()

            elif token in [muParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34 
                self.if_stat()

            elif token in [muParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35 
                self.while_stat()

            elif token in [muParser.OBRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36 
                self.until_stat()

            elif token in [muParser.LOG]:
                self.enterOuterAlt(localctx, 5)
                self.state = 37 
                self.log()

            elif token in [muParser.OTHER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                localctx._OTHER = self.match(muParser.OTHER)
                System.err.println("unknown char: " + (None if localctx._OTHER is None else localctx._OTHER.text));

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(muParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(muParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def SCOL(self):
            return self.getToken(muParser.SCOL, 0)

        def getRuleIndex(self):
            return muParser.RULE_assignment

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitAssignment(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = muParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(muParser.ID)
            self.state = 43
            self.match(muParser.ASSIGN)
            self.state = 44 
            self.expr(0)
            self.state = 45
            self.match(muParser.SCOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.If_statContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i=None):
            if i is None:
                return self.getTokens(muParser.IF)
            else:
                return self.getToken(muParser.IF, i)

        def condition_block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.Condition_blockContext)
            else:
                return self.getTypedRuleContext(muParser.Condition_blockContext,i)


        def ELSE(self, i=None):
            if i is None:
                return self.getTokens(muParser.ELSE)
            else:
                return self.getToken(muParser.ELSE, i)

        def stat_block(self):
            return self.getTypedRuleContext(muParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return muParser.RULE_if_stat

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterIf_stat(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitIf_stat(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = muParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(muParser.IF)
            self.state = 48 
            self.condition_block()
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.match(muParser.ELSE)
                    self.state = 50
                    self.match(muParser.IF)
                    self.state = 51 
                    self.condition_block() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 59
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 57
                self.match(muParser.ELSE)
                self.state = 58 
                self.stat_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Condition_blockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.Condition_blockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def stat_block(self):
            return self.getTypedRuleContext(muParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return muParser.RULE_condition_block

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterCondition_block(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitCondition_block(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitCondition_block(self)
            else:
                return visitor.visitChildren(self)




    def condition_block(self):

        localctx = muParser.Condition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self.expr(0)
            self.state = 62 
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stat_blockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.Stat_blockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OBRACE(self):
            return self.getToken(muParser.OBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(muParser.BlockContext,0)


        def CBRACE(self):
            return self.getToken(muParser.CBRACE, 0)

        def stat(self):
            return self.getTypedRuleContext(muParser.StatContext,0)


        def getRuleIndex(self):
            return muParser.RULE_stat_block

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterStat_block(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitStat_block(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitStat_block(self)
            else:
                return visitor.visitChildren(self)




    def stat_block(self):

        localctx = muParser.Stat_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stat_block)
        try:
            self.state = 69
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(muParser.OBRACE)
                self.state = 65 
                self.block()
                self.state = 66
                self.match(muParser.CBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68 
                self.stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.While_statContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(muParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def stat_block(self):
            return self.getTypedRuleContext(muParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return muParser.RULE_while_stat

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitWhile_stat(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitWhile_stat(self)
            else:
                return visitor.visitChildren(self)




    def while_stat(self):

        localctx = muParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(muParser.WHILE)
            self.state = 72 
            self.expr(0)
            self.state = 73 
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Until_statContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.Until_statContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OBRACE(self):
            return self.getToken(muParser.OBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(muParser.BlockContext,0)


        def CBRACE(self):
            return self.getToken(muParser.CBRACE, 0)

        def UNTIL(self):
            return self.getToken(muParser.UNTIL, 0)

        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def getRuleIndex(self):
            return muParser.RULE_until_stat

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterUntil_stat(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitUntil_stat(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitUntil_stat(self)
            else:
                return visitor.visitChildren(self)




    def until_stat(self):

        localctx = muParser.Until_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_until_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(muParser.OBRACE)
            self.state = 76 
            self.block()
            self.state = 77
            self.match(muParser.CBRACE)
            self.state = 78
            self.match(muParser.UNTIL)
            self.state = 79 
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.LogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(muParser.LOG, 0)

        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def SCOL(self):
            return self.getToken(muParser.SCOL, 0)

        def getRuleIndex(self):
            return muParser.RULE_log

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterLog(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitLog(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitLog(self)
            else:
                return visitor.visitChildren(self)




    def log(self):

        localctx = muParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(muParser.LOG)
            self.state = 82 
            self.expr(0)
            self.state = 83
            self.match(muParser.SCOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return muParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(muParser.ExprContext, self).copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.AndExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def AND(self):
            return self.getToken(muParser.AND, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterAndExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitAndExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.UnaryMinusExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(muParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.RelationalExprContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def LTEQ(self):
            return self.getToken(muParser.LTEQ, 0)
        def GTEQ(self):
            return self.getToken(muParser.GTEQ, 0)
        def LT(self):
            return self.getToken(muParser.LT, 0)
        def GT(self):
            return self.getToken(muParser.GT, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.AtomExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(muParser.AtomContext,0)


        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitAtomExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.AdditiveExprContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(muParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(muParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.EqualityExprContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def EQ(self):
            return self.getToken(muParser.EQ, 0)
        def NEQ(self):
            return self.getToken(muParser.NEQ, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.MultiplicationExprContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def MULT(self):
            return self.getToken(muParser.MULT, 0)
        def DIV(self):
            return self.getToken(muParser.DIV, 0)
        def MOD(self):
            return self.getToken(muParser.MOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitMultiplicationExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitMultiplicationExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.NotExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(muParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterNotExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitNotExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.PowExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def POW(self):
            return self.getToken(muParser.POW, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterPowExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitPowExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a muParser.ExprContext)
            super(muParser.OrExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(muParser.ExprContext)
            else:
                return self.getTypedRuleContext(muParser.ExprContext,i)

        def OR(self):
            return self.getToken(muParser.OR, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterOrExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitOrExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = muParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            token = self._input.LA(1)
            if token in [muParser.MINUS]:
                localctx = muParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 86
                self.match(muParser.MINUS)
                self.state = 87 
                self.expr(9)

            elif token in [muParser.NOT]:
                localctx = muParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(muParser.NOT)
                self.state = 89 
                self.expr(8)

            elif token in [muParser.OPAR, muParser.TRUE, muParser.FALSE, muParser.NIL, muParser.ID, muParser.INT, muParser.FLOAT, muParser.STRING]:
                localctx = muParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90 
                self.atom()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = muParser.PowExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 94
                        self.match(muParser.POW)
                        self.state = 95 
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = muParser.MultiplicationExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 97
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << muParser.MULT) | (1 << muParser.DIV) | (1 << muParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 98 
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = muParser.AdditiveExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 100
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==muParser.PLUS or _la==muParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 101 
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = muParser.RelationalExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 103
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << muParser.GT) | (1 << muParser.LT) | (1 << muParser.GTEQ) | (1 << muParser.LTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 104 
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = muParser.EqualityExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 106
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==muParser.EQ or _la==muParser.NEQ):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 107 
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = muParser.AndExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 109
                        self.match(muParser.AND)
                        self.state = 110 
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = muParser.OrExprContext(self, muParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 112
                        self.match(muParser.OR)
                        self.state = 113 
                        self.expr(3)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(muParser.AtomContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return muParser.RULE_atom

     
        def copyFrom(self, ctx):
            super(muParser.AtomContext, self).copyFrom(ctx)



    class ParExprContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.ParExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(muParser.OPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(muParser.ExprContext,0)

        def CPAR(self):
            return self.getToken(muParser.CPAR, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterParExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitParExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitParExpr(self)
            else:
                return visitor.visitChildren(self)


    class NilAtomContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.NilAtomContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NIL(self):
            return self.getToken(muParser.NIL, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterNilAtom(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitNilAtom(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitNilAtom(self)
            else:
                return visitor.visitChildren(self)


    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.IdAtomContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(muParser.ID, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterIdAtom(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitIdAtom(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringAtomContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.StringAtomContext, self).__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(muParser.STRING, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterStringAtom(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitStringAtom(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitStringAtom(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.NumberAtomContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(muParser.INT, 0)
        def FLOAT(self):
            return self.getToken(muParser.FLOAT, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitNumberAtom(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)


    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx): # actually a muParser.AtomContext)
            super(muParser.BooleanAtomContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(muParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(muParser.FALSE, 0)

        def enterRule(self, listener):
            if isinstance( listener, muListener ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener):
            if isinstance( listener, muListener ):
                listener.exitBooleanAtom(self)

        def accept(self, visitor):
            if isinstance( visitor, muVisitor ):
                return visitor.visitBooleanAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = muParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 128
            token = self._input.LA(1)
            if token in [muParser.OPAR]:
                localctx = muParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(muParser.OPAR)
                self.state = 120 
                self.expr(0)
                self.state = 121
                self.match(muParser.CPAR)

            elif token in [muParser.INT, muParser.FLOAT]:
                localctx = muParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                _la = self._input.LA(1)
                if not(_la==muParser.INT or _la==muParser.FLOAT):
                    self._errHandler.recoverInline(self)
                self.consume()

            elif token in [muParser.TRUE, muParser.FALSE]:
                localctx = muParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==muParser.TRUE or _la==muParser.FALSE):
                    self._errHandler.recoverInline(self)
                self.consume()

            elif token in [muParser.ID]:
                localctx = muParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(muParser.ID)

            elif token in [muParser.STRING]:
                localctx = muParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(muParser.STRING)

            elif token in [muParser.NIL]:
                localctx = muParser.NilAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.match(muParser.NIL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         



