import re
import sys
from antlr4 import *
from gen.gramatykaLexer import gramatykaLexer
from gen.gramatykaParser import gramatykaParser
from gen.gramatykaVisitor import gramatykaVisitor
import sympy

variables_dict = {}
input = []
with open('input.txt', 'r') as file:
    input = (file.read().split(' '))
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
        with open('output.txt', 'w') as file:
            value = ctx.getText()[7:]
            file.write(str(self.visitExpression(value)))

    def visitIfStatement(self, ctx):
        data = replace_multiple_spaces(ctx.getText())
        iterator = data[3:data.find('{')]
        iterator = iterator.replace('True', '1>0').replace('False', '0>1')
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
        to_check = self.visitComparison(while_id)
        while to_check:
            visitFun(ctx.getText()[ctx.getText().find('{')+1:-1], visitor)
            to_check = self.visitComparison(while_id)


    def visitComparison(self, while_id):
        if self.used_lines > 100:
            sys.exit("Error: Too many lines used")
        self.used_lines += 1
        operators = ['==', '!=', '>=', '<=', '>', '<', 'and', 'or']
        pattern = '|'.join(map(re.escape, operators))
        while_id_split = re.split(f'({pattern})', while_id)
        substrings = []
        used_operators = []
        for i in range(0, len(while_id_split), 2):
            substrings.append(while_id_split[i])
            if i + 1 < len(while_id_split):
                used_operators.append(while_id_split[i + 1])
        for g, x in enumerate(used_operators):
            if (x == 'and' or x == 'or'):
                continue
            val1 = variables_dict[substrings[0]] if substrings[0] in variables_dict else substrings[0]
            val2 = variables_dict[substrings[1]] if substrings[1] in variables_dict else substrings[1]
            if len(substrings) > 2:
                substrings.remove(substrings[0])
                substrings.remove(substrings[0])
            used_operators[g] = sympy.sympify(f'{val1} {x} {val2}')
        while_id = ' '.join(str(x) for x in used_operators)
        return sympy.sympify(while_id)

    def visitExpression(self, ctx):
        if isinstance(ctx, str):
            data = ctx
        else:
            data = ctx.getText()

        for key, value in variables_dict.items():
            data = data.replace(key, str(value))

        sympified_data = sympy.sympify(data)
        return sympified_data


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
