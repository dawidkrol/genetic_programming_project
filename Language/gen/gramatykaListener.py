# Generated from C:/Users/dkmak/Desktop/genetic_programming_project/Language/gramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatykaParser import gramatykaParser
else:
    from gramatykaParser import gramatykaParser

# This class defines a complete listener for a parse tree produced by gramatykaParser.
class gramatykaListener(ParseTreeListener):

    # Enter a parse tree produced by gramatykaParser#prog.
    def enterProg(self, ctx:gramatykaParser.ProgContext):
        pass

    # Exit a parse tree produced by gramatykaParser#prog.
    def exitProg(self, ctx:gramatykaParser.ProgContext):
        pass


    # Enter a parse tree produced by gramatykaParser#statement.
    def enterStatement(self, ctx:gramatykaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#statement.
    def exitStatement(self, ctx:gramatykaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#name.
    def enterName(self, ctx:gramatykaParser.NameContext):
        pass

    # Exit a parse tree produced by gramatykaParser#name.
    def exitName(self, ctx:gramatykaParser.NameContext):
        pass


    # Enter a parse tree produced by gramatykaParser#printStatement.
    def enterPrintStatement(self, ctx:gramatykaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#printStatement.
    def exitPrintStatement(self, ctx:gramatykaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#inputStatement.
    def enterInputStatement(self, ctx:gramatykaParser.InputStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#inputStatement.
    def exitInputStatement(self, ctx:gramatykaParser.InputStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#outputStatement.
    def enterOutputStatement(self, ctx:gramatykaParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#outputStatement.
    def exitOutputStatement(self, ctx:gramatykaParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#ifStatement.
    def enterIfStatement(self, ctx:gramatykaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#ifStatement.
    def exitIfStatement(self, ctx:gramatykaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#while.
    def enterWhile(self, ctx:gramatykaParser.WhileContext):
        pass

    # Exit a parse tree produced by gramatykaParser#while.
    def exitWhile(self, ctx:gramatykaParser.WhileContext):
        pass


    # Enter a parse tree produced by gramatykaParser#variableAssignment.
    def enterVariableAssignment(self, ctx:gramatykaParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by gramatykaParser#variableAssignment.
    def exitVariableAssignment(self, ctx:gramatykaParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by gramatykaParser#comparison.
    def enterComparison(self, ctx:gramatykaParser.ComparisonContext):
        pass

    # Exit a parse tree produced by gramatykaParser#comparison.
    def exitComparison(self, ctx:gramatykaParser.ComparisonContext):
        pass


    # Enter a parse tree produced by gramatykaParser#expression.
    def enterExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#expression.
    def exitExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#codeBlock.
    def enterCodeBlock(self, ctx:gramatykaParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by gramatykaParser#codeBlock.
    def exitCodeBlock(self, ctx:gramatykaParser.CodeBlockContext):
        pass



del gramatykaParser