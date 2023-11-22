import re
import sys
from antlr4 import *
from gen.gramatykaLexer import gramatykaLexer
from gen.gramatykaParser import gramatykaParser
from gen.gramatykaVisitor import gramatykaVisitor
import sympy

variables_dict = {}
functions_dict = {}
def replace_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text)
class MyVisitor(gramatykaVisitor):

    def visitProg(self, ctx: gramatykaParser.ProgContext):
        return self.visitChildren(ctx)

    # def visitStatement(self, ctx):
    #     pass

    def visitPrintStatement(self, ctx):
        value = ctx.getText()[6:]
        print(variables_dict[value])


    # def visitInputStatement(self, ctx):
    #     pass
    #
    def visitOutputStatement(self, ctx):
        print(ctx.getText()[7:-1])

    def visitIfStatement(self, ctx):
        data = replace_multiple_spaces(ctx.getText())
        dataI = data.split(' ')
        iterator = dataI[1][:dataI[1].find('{')]
        iterator = self.visitExpression(iterator)
        trueV = None
        falseV = None
        if 'else' in data:
            trueV = data[data.find('{')+1:data.find('else')-2]
            falseV = data[data.find('else')+6:-1]
            if iterator == True:
                visitFun(trueV, visitor)
            else:
                visitFun(falseV, visitor)
        else:
            trueV = data[data.find('{')+1:-1]
            if iterator == True:
                visitFun(trueV, visitor)


    def visitForStatement(self, ctx):
        data = ctx.getText().split(' ')
        iterator = data[3][:data[3].find('{')]
        iterator = self.visitExpression(iterator)
        if iterator == True:
            iterator = 1
        elif iterator == False:
            iterator = 0
        block = ctx.getText()[ctx.getText().find('{')+1:ctx.getText().rfind('}')]
        for i in range(iterator):
            visitFun(block, visitor)


    def visitVariableDeclaration(self, ctx):
        data = ctx.getText().split('=')
        name = data[0][4:]
        variables_dict[name] = self.visitExpression(data[1])


    def visitVariableAssignment(self, ctx):
        data = ctx.getText().split('=')
        name = data[0]
        variables_dict[name] = self.visitExpression(data[1])


    def visitFunctionDefinition(self, ctx):
        data = replace_multiple_spaces(ctx.getText())
        name = data[9:data.find('(')]
        functions_dict[name] = data[data.find('{')+1:-1]

    def visitFunctionCall(self, ctx):
        data = ctx.getText()
        block = functions_dict[data[:data.find('(')]]
        visitFun(block, visitor)

    def visitExpression(self, ctx):
        data = None
        if isinstance(ctx, str):
            data = ctx
        else:
            data = ctx.getText()
        for keys in variables_dict:
            if keys in data:
                data = data.replace(keys, str(variables_dict[keys]))
        return sympy.sympify(data)


visitor = MyVisitor()
def visitFun(line, visitor):
    data = InputStream(line)
    # lexer
    lexer = gramatykaLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = gramatykaParser(stream)
    tree = parser.prog()
    # evaluator
    output = visitor.visit(tree)
with open('text.txt', 'r') as file:
    data = file.read()
    visitFun(data, visitor)
