import re
import sys
from antlr4 import *
from Language.gen.gramatykaLexer import gramatykaLexer
from Language.gen.gramatykaParser import gramatykaParser
from Language.gen.gramatykaVisitor import gramatykaVisitor
import sympy

variables_dict = {}
input = []

def get_input():
    input.clear()
    with open('./input.txt', 'r') as file:
        input.extend((file.read().split(' ')))

def replace_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text)


class MyVisitor(gramatykaVisitor):
    def __init__(self):
        self.used_lines = 0

    def visitProg(self, ctx: gramatykaParser.ProgContext):
        return self.visitChildren(ctx)


    def visitPrintStatement(self, ctx):
        self.used_lines += 1
        value = ctx.getText()[6:]
        print(self.visitExpression(value))


    def visitOutputStatement(self, ctx):
        self.used_lines += 1
        with open('./output.txt', 'a') as file:
            value = ctx.getText()[7:]
            if value == 'input':
                value = int(input.pop(0)) if len(input) > 0 else 0
            #append to file not overwrite if in same session
            file.write(str(self.visitExpression(value)) + '\n')


    def visitIfStatement(self, ctx):
        data = replace_multiple_spaces(ctx.getText())
        iterator = data[3:data.find('{')]
        iterator = iterator.replace('True', '1>0').replace('False', '0>1')
        while 'input' in iterator:
            vale = int(input.pop(0)) if len(input) > 0 else 0
            iterator = iterator[:iterator.find('input')] + str(vale) + iterator[iterator.find('input')+5:]
        iterator = self.visitComparison(iterator)
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

    def visitVariableAssignment(self, ctx):
        self.used_lines += 1
        data = ctx.getText().split('=')
        name = data[0]
        if data[1] == 'input':
            variables_dict[name] = int(input.pop(0))
        else:
            variables_dict[name] = self.visitExpression(data[1])
    def visitWhile(self, ctx:gramatykaParser.WhileContext):
        while_id = ctx.getText()[6:ctx.getText().find('{')]
        while_id = while_id.replace('True', '1>0').replace('False', '0>1')
        new_while_id = while_id
        while 'input' in new_while_id:
            vale = int(input.pop(0)) if len(input) > 0 else 0
            new_while_id = new_while_id[:new_while_id.find('input')] + str(vale) + new_while_id[new_while_id.find('input') + 5:]
        to_check = self.visitComparison(new_while_id)
        while to_check:
            visitFun(ctx.getText()[ctx.getText().find('{')+1:-1], visitor)
            new_while_id = while_id
            while 'input' in new_while_id:
                vale = int(input.pop(0)) if len(input) > 0 else 0
                new_while_id = new_while_id[:new_while_id.find('input')] + str(vale) + new_while_id[
                                                                                                    new_while_id.find(
                                                                                                        'input') + 5:]
            to_check = self.visitComparison(new_while_id)


    def visitComparison(self, while_id):
        if self.used_lines > 100:
            sys.exit("Error: Too many lines used")
        self.used_lines += 1
        for key, value in variables_dict.items():
            while_id = while_id.replace(key, str(value))
        result = eval(while_id)
        return sympy.sympify(result)

    def visitExpression(self, ctx):
        if isinstance(ctx, str) or isinstance(ctx, int):
            data = str(ctx)
        else:
            data = ctx.getText()

        for key, value in variables_dict.items():
            data = data.replace(key, str(value))
        while 'input' in data:
            vale = int(input.pop(0)) if len(input) > 0 else 0
            data = data[:data.find('input')] + str(vale) + data[data.find('input')+5:]
        sympified_data = sympy.sympify(data)
        return sympified_data

def get_output():
    output = []
    with open('./output.txt', 'r') as file:
        data = file.read()
        output += data.strip().split("\n")
    return output


def clear_output_file():
    with open('./output.txt', 'w') as file:
        file.write('')

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

visitor = MyVisitor()

def run(inp):
    input.append(inp)
    clear_output_file()
    with open('./program.txt', 'r') as file:
        data = file.read().replace('\n', '\t')
        visitFun(data, visitor)
    input.clear()

def run_best_program():
    get_input()
    clear_output_file()
    with open('./best_program.txt', 'r') as file:
        data = file.read().replace('\n', '\t')
        visitFun(data, visitor)
run_best_program()
