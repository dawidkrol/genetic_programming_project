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


    # Enter a parse tree produced by gramatykaParser#forStatement.
    def enterForStatement(self, ctx:gramatykaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#forStatement.
    def exitForStatement(self, ctx:gramatykaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:gramatykaParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by gramatykaParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:gramatykaParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by gramatykaParser#variableAssignment.
    def enterVariableAssignment(self, ctx:gramatykaParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by gramatykaParser#variableAssignment.
    def exitVariableAssignment(self, ctx:gramatykaParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by gramatykaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:gramatykaParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:gramatykaParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#functionCall.
    def enterFunctionCall(self, ctx:gramatykaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by gramatykaParser#functionCall.
    def exitFunctionCall(self, ctx:gramatykaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by gramatykaParser#parameterList.
    def enterParameterList(self, ctx:gramatykaParser.ParameterListContext):
        pass

    # Exit a parse tree produced by gramatykaParser#parameterList.
    def exitParameterList(self, ctx:gramatykaParser.ParameterListContext):
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