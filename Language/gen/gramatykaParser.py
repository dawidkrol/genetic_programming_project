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
        4,1,32,168,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,3,0,36,8,0,1,0,5,0,39,8,0,10,
        0,12,0,42,9,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,5,0,51,8,0,10,
        0,12,0,54,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,91,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,3,7,100,8,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,3,9,115,8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,123,8,10,1,10,1,10,
        1,11,1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,142,8,12,1,12,1,12,1,12,5,12,147,8,12,10,
        12,12,12,150,9,12,1,13,1,13,5,13,154,8,13,10,13,12,13,157,9,13,1,
        13,1,13,5,13,161,8,13,10,13,12,13,164,9,13,1,13,1,13,1,13,0,1,24,
        14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,1,1,0,17,26,176,0,35,1,
        0,0,0,2,74,1,0,0,0,4,76,1,0,0,0,6,79,1,0,0,0,8,82,1,0,0,0,10,85,
        1,0,0,0,12,92,1,0,0,0,14,99,1,0,0,0,16,106,1,0,0,0,18,110,1,0,0,
        0,20,119,1,0,0,0,22,126,1,0,0,0,24,141,1,0,0,0,26,151,1,0,0,0,28,
        36,3,2,1,0,29,31,5,31,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,
        0,0,32,33,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,35,28,1,0,0,0,35,32,
        1,0,0,0,36,46,1,0,0,0,37,39,5,31,0,0,38,37,1,0,0,0,39,42,1,0,0,0,
        40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,45,3,
        2,1,0,44,40,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        52,1,0,0,0,48,46,1,0,0,0,49,51,5,31,0,0,50,49,1,0,0,0,51,54,1,0,
        0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,1,1,0,0,0,54,52,1,0,0,0,55,56,
        3,4,2,0,56,57,5,1,0,0,57,75,1,0,0,0,58,59,3,6,3,0,59,60,5,1,0,0,
        60,75,1,0,0,0,61,62,3,8,4,0,62,63,5,1,0,0,63,75,1,0,0,0,64,75,3,
        10,5,0,65,75,3,12,6,0,66,67,3,14,7,0,67,68,5,1,0,0,68,75,1,0,0,0,
        69,70,3,16,8,0,70,71,5,1,0,0,71,75,1,0,0,0,72,75,3,18,9,0,73,75,
        3,20,10,0,74,55,1,0,0,0,74,58,1,0,0,0,74,61,1,0,0,0,74,64,1,0,0,
        0,74,65,1,0,0,0,74,66,1,0,0,0,74,69,1,0,0,0,74,72,1,0,0,0,74,73,
        1,0,0,0,75,3,1,0,0,0,76,77,5,2,0,0,77,78,3,24,12,0,78,5,1,0,0,0,
        79,80,5,3,0,0,80,81,5,30,0,0,81,7,1,0,0,0,82,83,5,4,0,0,83,84,3,
        24,12,0,84,9,1,0,0,0,85,86,5,5,0,0,86,87,3,24,12,0,87,90,3,26,13,
        0,88,89,5,6,0,0,89,91,3,26,13,0,90,88,1,0,0,0,90,91,1,0,0,0,91,11,
        1,0,0,0,92,93,5,7,0,0,93,94,5,30,0,0,94,95,5,8,0,0,95,96,3,24,12,
        0,96,97,3,26,13,0,97,13,1,0,0,0,98,100,5,9,0,0,99,98,1,0,0,0,99,
        100,1,0,0,0,100,101,1,0,0,0,101,102,5,10,0,0,102,103,5,30,0,0,103,
        104,5,11,0,0,104,105,3,24,12,0,105,15,1,0,0,0,106,107,5,30,0,0,107,
        108,5,11,0,0,108,109,3,24,12,0,109,17,1,0,0,0,110,111,5,12,0,0,111,
        112,5,30,0,0,112,114,5,13,0,0,113,115,3,22,11,0,114,113,1,0,0,0,
        114,115,1,0,0,0,115,116,1,0,0,0,116,117,5,14,0,0,117,118,3,26,13,
        0,118,19,1,0,0,0,119,120,5,30,0,0,120,122,5,13,0,0,121,123,3,22,
        11,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,5,15,
        0,0,125,21,1,0,0,0,126,131,5,30,0,0,127,128,5,16,0,0,128,130,5,30,
        0,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,
        0,0,132,23,1,0,0,0,133,131,1,0,0,0,134,135,6,12,-1,0,135,142,5,29,
        0,0,136,142,5,30,0,0,137,138,5,13,0,0,138,139,3,24,12,0,139,140,
        5,14,0,0,140,142,1,0,0,0,141,134,1,0,0,0,141,136,1,0,0,0,141,137,
        1,0,0,0,142,148,1,0,0,0,143,144,10,1,0,0,144,145,7,0,0,0,145,147,
        3,24,12,2,146,143,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,25,1,0,0,0,150,148,1,0,0,0,151,155,5,27,0,0,152,154,
        5,31,0,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,162,3,0,0,0,159,161,
        5,31,0,0,160,159,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,5,28,0,0,166,27,
        1,0,0,0,15,32,35,40,46,52,74,90,99,114,122,131,141,148,155,162
    ]

class gramatykaParser ( Parser ):

    grammarFileName = "gramatyka.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print '", "'input '", "'output '", 
                     "'if '", "' else '", "'for '", "' in '", "'final '", 
                     "'var '", "'='", "'function '", "'('", "')'", "');'", 
                     "','", "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "STRING", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_printStatement = 2
    RULE_inputStatement = 3
    RULE_outputStatement = 4
    RULE_ifStatement = 5
    RULE_forStatement = 6
    RULE_variableDeclaration = 7
    RULE_variableAssignment = 8
    RULE_functionDefinition = 9
    RULE_functionCall = 10
    RULE_parameterList = 11
    RULE_expression = 12
    RULE_codeBlock = 13

    ruleNames =  [ "prog", "statement", "printStatement", "inputStatement", 
                   "outputStatement", "ifStatement", "forStatement", "variableDeclaration", 
                   "variableAssignment", "functionDefinition", "functionCall", 
                   "parameterList", "expression", "codeBlock" ]

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
    T__26=27
    T__27=28
    INT=29
    STRING=30
    NEWLINE=31
    WS=32

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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.statement()
                pass

            elif la_ == 2:
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 29
                        self.match(gramatykaParser.NEWLINE) 
                    self.state = 34
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass


            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 37
                        self.match(gramatykaParser.NEWLINE)
                        self.state = 42
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 43
                    self.statement() 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.match(gramatykaParser.NEWLINE) 
                self.state = 54
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


        def forStatement(self):
            return self.getTypedRuleContext(gramatykaParser.ForStatementContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(gramatykaParser.VariableDeclarationContext,0)


        def variableAssignment(self):
            return self.getTypedRuleContext(gramatykaParser.VariableAssignmentContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(gramatykaParser.FunctionDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(gramatykaParser.FunctionCallContext,0)


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
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.printStatement()
                self.state = 56
                self.match(gramatykaParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.inputStatement()
                self.state = 59
                self.match(gramatykaParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.outputStatement()
                self.state = 62
                self.match(gramatykaParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.variableDeclaration()
                self.state = 67
                self.match(gramatykaParser.T__0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.variableAssignment()
                self.state = 70
                self.match(gramatykaParser.T__0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.functionDefinition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.functionCall()
                pass


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
        self.enterRule(localctx, 4, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(gramatykaParser.T__1)

            self.state = 77
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

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

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
        self.enterRule(localctx, 6, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(gramatykaParser.T__2)
            self.state = 80
            self.match(gramatykaParser.STRING)
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
        self.enterRule(localctx, 8, self.RULE_outputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(gramatykaParser.T__3)
            self.state = 83
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

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


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
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(gramatykaParser.T__4)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.codeBlock()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 88
                self.match(gramatykaParser.T__5)
                self.state = 89
                self.codeBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def codeBlock(self):
            return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatykaParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(gramatykaParser.T__6)
            self.state = 93
            self.match(gramatykaParser.STRING)
            self.state = 94
            self.match(gramatykaParser.T__7)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = gramatykaParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 98
                self.match(gramatykaParser.T__8)


            self.state = 101
            self.match(gramatykaParser.T__9)
            self.state = 102
            self.match(gramatykaParser.STRING)
            self.state = 103
            self.match(gramatykaParser.T__10)
            self.state = 104
            self.expression(0)
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

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


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
            self.state = 106
            self.match(gramatykaParser.STRING)
            self.state = 107
            self.match(gramatykaParser.T__10)
            self.state = 108
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def codeBlock(self):
            return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(gramatykaParser.ParameterListContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = gramatykaParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(gramatykaParser.T__11)
            self.state = 111
            self.match(gramatykaParser.STRING)
            self.state = 112
            self.match(gramatykaParser.T__12)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 113
                self.parameterList()


            self.state = 116
            self.match(gramatykaParser.T__13)
            self.state = 117
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def parameterList(self):
            return self.getTypedRuleContext(gramatykaParser.ParameterListContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = gramatykaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(gramatykaParser.STRING)
            self.state = 120
            self.match(gramatykaParser.T__12)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 121
                self.parameterList()


            self.state = 124
            self.match(gramatykaParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(gramatykaParser.STRING)
            else:
                return self.getToken(gramatykaParser.STRING, i)

        def getRuleIndex(self):
            return gramatykaParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = gramatykaParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(gramatykaParser.STRING)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 127
                self.match(gramatykaParser.T__15)
                self.state = 128
                self.match(gramatykaParser.STRING)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(gramatykaParser.INT, 0)

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 135
                self.match(gramatykaParser.INT)
                pass
            elif token in [30]:
                self.state = 136
                self.match(gramatykaParser.STRING)
                pass
            elif token in [13]:
                self.state = 137
                self.match(gramatykaParser.T__12)
                self.state = 138
                self.expression(0)
                self.state = 139
                self.match(gramatykaParser.T__13)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 143
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 144
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134086656) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self.expression(2) 
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_codeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(gramatykaParser.T__26)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self.match(gramatykaParser.NEWLINE) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 158
            self.prog()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 159
                self.match(gramatykaParser.NEWLINE)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(gramatykaParser.T__27)
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
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




