# Generated from C:/Users/dkmak/Desktop/genetic_programming_project/Language/gramatyka.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,5,0,27,8,0,
        10,0,12,0,30,9,0,3,0,32,8,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,
        5,0,41,8,0,10,0,12,0,44,9,0,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,66,8,1,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,83,
        8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,93,8,8,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,101,8,9,1,9,1,9,1,9,5,9,106,8,9,10,9,12,9,109,9,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,118,8,10,1,10,1,10,1,10,5,10,
        123,8,10,10,10,12,10,126,9,10,1,11,1,11,5,11,130,8,11,10,11,12,11,
        133,9,11,1,11,1,11,5,11,137,8,11,10,11,12,11,140,9,11,1,11,1,11,
        1,11,0,2,18,20,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,1,0,9,14,1,
        0,17,18,1,0,15,16,1,0,21,24,150,0,31,1,0,0,0,2,65,1,0,0,0,4,67,1,
        0,0,0,6,69,1,0,0,0,8,72,1,0,0,0,10,74,1,0,0,0,12,77,1,0,0,0,14,84,
        1,0,0,0,16,88,1,0,0,0,18,100,1,0,0,0,20,117,1,0,0,0,22,127,1,0,0,
        0,24,32,3,2,1,0,25,27,5,29,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,
        1,0,0,0,28,29,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,31,24,1,0,0,0,
        31,28,1,0,0,0,32,42,1,0,0,0,33,35,5,29,0,0,34,33,1,0,0,0,35,38,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,
        41,3,2,1,0,40,36,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,48,1,0,0,0,44,42,1,0,0,0,45,47,5,29,0,0,46,45,1,0,0,0,47,50,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,1,1,0,0,0,50,48,1,0,0,0,51,
        52,3,6,3,0,52,53,5,1,0,0,53,66,1,0,0,0,54,55,3,8,4,0,55,56,5,1,0,
        0,56,66,1,0,0,0,57,58,3,10,5,0,58,59,5,1,0,0,59,66,1,0,0,0,60,66,
        3,12,6,0,61,66,3,14,7,0,62,63,3,16,8,0,63,64,5,1,0,0,64,66,1,0,0,
        0,65,51,1,0,0,0,65,54,1,0,0,0,65,57,1,0,0,0,65,60,1,0,0,0,65,61,
        1,0,0,0,65,62,1,0,0,0,66,3,1,0,0,0,67,68,5,28,0,0,68,5,1,0,0,0,69,
        70,5,2,0,0,70,71,3,20,10,0,71,7,1,0,0,0,72,73,5,3,0,0,73,9,1,0,0,
        0,74,75,5,4,0,0,75,76,3,20,10,0,76,11,1,0,0,0,77,78,5,5,0,0,78,79,
        3,18,9,0,79,82,3,22,11,0,80,81,5,6,0,0,81,83,3,22,11,0,82,80,1,0,
        0,0,82,83,1,0,0,0,83,13,1,0,0,0,84,85,5,7,0,0,85,86,3,18,9,0,86,
        87,3,22,11,0,87,15,1,0,0,0,88,89,3,4,2,0,89,92,5,8,0,0,90,93,3,20,
        10,0,91,93,3,8,4,0,92,90,1,0,0,0,92,91,1,0,0,0,93,17,1,0,0,0,94,
        95,6,9,-1,0,95,96,3,20,10,0,96,97,7,0,0,0,97,98,3,20,10,0,98,101,
        1,0,0,0,99,101,7,1,0,0,100,94,1,0,0,0,100,99,1,0,0,0,101,107,1,0,
        0,0,102,103,10,2,0,0,103,104,7,2,0,0,104,106,3,18,9,3,105,102,1,
        0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,19,1,0,
        0,0,109,107,1,0,0,0,110,111,6,10,-1,0,111,118,5,27,0,0,112,118,3,
        4,2,0,113,114,5,19,0,0,114,115,3,20,10,0,115,116,5,20,0,0,116,118,
        1,0,0,0,117,110,1,0,0,0,117,112,1,0,0,0,117,113,1,0,0,0,118,124,
        1,0,0,0,119,120,10,1,0,0,120,121,7,3,0,0,121,123,3,20,10,2,122,119,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,21,1,
        0,0,0,126,124,1,0,0,0,127,131,5,25,0,0,128,130,5,29,0,0,129,128,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,
        1,0,0,0,133,131,1,0,0,0,134,138,3,0,0,0,135,137,5,29,0,0,136,135,
        1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,141,
        1,0,0,0,140,138,1,0,0,0,141,142,5,26,0,0,142,23,1,0,0,0,14,28,31,
        36,42,48,65,82,92,100,107,117,124,131,138
    ]

class gramatykaParser ( Parser ):

    grammarFileName = "gramatyka.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print '", "'input'", "'output '", 
                     "'if '", "' else '", "'while '", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "' and '", "' or '", 
                     "'True'", "'False'", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "STRING", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_name = 2
    RULE_printStatement = 3
    RULE_inputStatement = 4
    RULE_outputStatement = 5
    RULE_ifStatement = 6
    RULE_while = 7
    RULE_variableAssignment = 8
    RULE_comparison = 9
    RULE_expression = 10
    RULE_codeBlock = 11

    ruleNames =  [ "prog", "statement", "name", "printStatement", "inputStatement", 
                   "outputStatement", "ifStatement", "while", "variableAssignment", 
                   "comparison", "expression", "codeBlock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    INT=27
    STRING=28
    NEWLINE=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramatykaParser.NEWLINE)
            else:
                return self.getToken(gramatykaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramatykaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = gramatykaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 24
                self.statement()
                pass

            elif la_ == 2:
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 25
                        self.match(gramatykaParser.NEWLINE) 
                    self.state = 30
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass


            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==29:
                        self.state = 33
                        self.match(gramatykaParser.NEWLINE)
                        self.state = 38
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 39
                    self.statement() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 45
                    self.match(gramatykaParser.NEWLINE) 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStatement(self):
            return self.getTypedRuleContext(gramatykaParser.PrintStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def outputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.OutputStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(gramatykaParser.IfStatementContext,0)


        def while_(self):
            return self.getTypedRuleContext(gramatykaParser.WhileContext,0)


        def variableAssignment(self):
            return self.getTypedRuleContext(gramatykaParser.VariableAssignmentContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatykaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.printStatement()
                self.state = 52
                self.match(gramatykaParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.inputStatement()
                self.state = 55
                self.match(gramatykaParser.T__0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.outputStatement()
                self.state = 58
                self.match(gramatykaParser.T__0)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.while_()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 6)
                self.state = 62
                self.variableAssignment()
                self.state = 63
                self.match(gramatykaParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def getRuleIndex(self):
            return gramatykaParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = gramatykaParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(gramatykaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = gramatykaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramatykaParser.T__1)

            self.state = 70
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatykaParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = gramatykaParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(gramatykaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_outputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStatement" ):
                listener.enterOutputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStatement" ):
                listener.exitOutputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStatement" ):
                return visitor.visitOutputStatement(self)
            else:
                return visitor.visitChildren(self)




    def outputStatement(self):

        localctx = gramatykaParser.OutputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_outputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(gramatykaParser.T__3)
            self.state = 75
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(gramatykaParser.ComparisonContext,0)


        def codeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.CodeBlockContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatykaParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(gramatykaParser.T__4)
            self.state = 78
            self.comparison(0)
            self.state = 79
            self.codeBlock()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 80
                self.match(gramatykaParser.T__5)
                self.state = 81
                self.codeBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(gramatykaParser.ComparisonContext,0)


        def codeBlock(self):
            return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = gramatykaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(gramatykaParser.T__6)
            self.state = 85
            self.comparison(0)
            self.state = 86
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(gramatykaParser.NameContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_variableAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignment" ):
                listener.enterVariableAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignment" ):
                listener.exitVariableAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssignment" ):
                return visitor.visitVariableAssignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAssignment(self):

        localctx = gramatykaParser.VariableAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.name()
            self.state = 89
            self.match(gramatykaParser.T__7)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 27, 28]:
                self.state = 90
                self.expression(0)
                pass
            elif token in [3]:
                self.state = 91
                self.inputStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ExpressionContext,i)


        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ComparisonContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatykaParser.ComparisonContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_comparison, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 27, 28]:
                self.state = 95
                self.expression(0)
                self.state = 96
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 97
                self.expression(0)
                pass
            elif token in [17, 18]:
                self.state = 99
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.ComparisonContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparison)
                    self.state = 102
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 103
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 104
                    self.comparison(3) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(gramatykaParser.INT, 0)

        def name(self):
            return self.getTypedRuleContext(gramatykaParser.NameContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatykaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 111
                self.match(gramatykaParser.INT)
                pass
            elif token in [28]:
                self.state = 112
                self.name()
                pass
            elif token in [19]:
                self.state = 113
                self.match(gramatykaParser.T__18)
                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(gramatykaParser.T__19)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 119
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 120
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 121
                    self.expression(2) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CodeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(gramatykaParser.ProgContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramatykaParser.NEWLINE)
            else:
                return self.getToken(gramatykaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramatykaParser.RULE_codeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeBlock" ):
                listener.enterCodeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeBlock" ):
                listener.exitCodeBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeBlock" ):
                return visitor.visitCodeBlock(self)
            else:
                return visitor.visitChildren(self)




    def codeBlock(self):

        localctx = gramatykaParser.CodeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_codeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(gramatykaParser.T__24)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 128
                    self.match(gramatykaParser.NEWLINE) 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 134
            self.prog()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 135
                self.match(gramatykaParser.NEWLINE)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(gramatykaParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.comparison_sempred
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def comparison_sempred(self, localctx:ComparisonContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




