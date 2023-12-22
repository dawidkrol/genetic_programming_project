# Generated from C:/Users/dkmak/OneDrive/Pulpit/genetic_programming_project/Language\gramatyka.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramatykaParser import gramatykaParser
else:
    from gramatykaParser import gramatykaParser

# This class defines a complete generic visitor for a parse tree produced by gramatykaParser.

class gramatykaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatykaParser#prog.
    def visitProg(self, ctx:gramatykaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#statement.
    def visitStatement(self, ctx:gramatykaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#name.
    def visitName(self, ctx:gramatykaParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#printStatement.
    def visitPrintStatement(self, ctx:gramatykaParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#inputStatement.
    def visitInputStatement(self, ctx:gramatykaParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#outputStatement.
    def visitOutputStatement(self, ctx:gramatykaParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#ifStatement.
    def visitIfStatement(self, ctx:gramatykaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#while.
    def visitWhile(self, ctx:gramatykaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#variableAssignment.
    def visitVariableAssignment(self, ctx:gramatykaParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#comparison.
    def visitComparison(self, ctx:gramatykaParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#expression.
    def visitExpression(self, ctx:gramatykaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatykaParser#codeBlock.
    def visitCodeBlock(self, ctx:gramatykaParser.CodeBlockContext):
        return self.visitChildren(ctx)



del gramatykaParser