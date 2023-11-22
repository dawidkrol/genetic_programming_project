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
        print(self.visitExpression(value))


    # def visitInputStatement(self, ctx):
    #     with open('input.txt', 'w') as file:
    #         value = ctx.getText()[7:]
    #         file.write(str(variables_dict[value]))

    def visitOutputStatement(self, ctx):
        with open('output.txt', 'w') as file:
            value = ctx.getText()[7:]
            file.write(str(self.visitExpression(value)))

    def visitIfStatement(self, ctx):
        print(ctx.getText())
        data = replace_multiple_spaces(ctx.getText())
        iterator = data[3:data.find('{')]
        print(iterator)
        iterator = self.visitComparison(iterator)
        print(iterator)
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

    def visitVariableAssignment(self, ctx):
        data = ctx.getText().split('=')
        name = data[0]
        variables_dict[name] = self.visitExpression(data[1])
    def visitWhile(self, ctx:gramatykaParser.WhileContext):
        return self.visitChildren(ctx)

    def visitComparison(self, ctx):
        return sympy.sympify(ctx)

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
