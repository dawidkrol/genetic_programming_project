# Generated from C:/Users/dkmak/Desktop/genetic_programming_project/Language/gramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,30,182,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,
        12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,
        23,1,24,1,24,1,25,1,25,1,26,4,26,160,8,26,11,26,12,26,161,1,27,1,
        27,5,27,166,8,27,10,27,12,27,169,9,27,1,28,4,28,172,8,28,11,28,12,
        28,173,1,29,4,29,177,8,29,11,29,12,29,178,1,29,1,29,0,0,30,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,1,0,5,1,0,48,57,2,0,65,90,97,122,4,
        0,48,57,65,90,95,95,97,122,2,0,10,10,13,13,2,0,9,9,32,32,185,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,1,61,1,0,
        0,0,3,63,1,0,0,0,5,70,1,0,0,0,7,76,1,0,0,0,9,84,1,0,0,0,11,88,1,
        0,0,0,13,95,1,0,0,0,15,102,1,0,0,0,17,104,1,0,0,0,19,107,1,0,0,0,
        21,110,1,0,0,0,23,112,1,0,0,0,25,114,1,0,0,0,27,117,1,0,0,0,29,120,
        1,0,0,0,31,126,1,0,0,0,33,131,1,0,0,0,35,136,1,0,0,0,37,142,1,0,
        0,0,39,144,1,0,0,0,41,146,1,0,0,0,43,148,1,0,0,0,45,150,1,0,0,0,
        47,152,1,0,0,0,49,154,1,0,0,0,51,156,1,0,0,0,53,159,1,0,0,0,55,163,
        1,0,0,0,57,171,1,0,0,0,59,176,1,0,0,0,61,62,5,59,0,0,62,2,1,0,0,
        0,63,64,5,112,0,0,64,65,5,114,0,0,65,66,5,105,0,0,66,67,5,110,0,
        0,67,68,5,116,0,0,68,69,5,32,0,0,69,4,1,0,0,0,70,71,5,105,0,0,71,
        72,5,110,0,0,72,73,5,112,0,0,73,74,5,117,0,0,74,75,5,116,0,0,75,
        6,1,0,0,0,76,77,5,111,0,0,77,78,5,117,0,0,78,79,5,116,0,0,79,80,
        5,112,0,0,80,81,5,117,0,0,81,82,5,116,0,0,82,83,5,32,0,0,83,8,1,
        0,0,0,84,85,5,105,0,0,85,86,5,102,0,0,86,87,5,32,0,0,87,10,1,0,0,
        0,88,89,5,32,0,0,89,90,5,101,0,0,90,91,5,108,0,0,91,92,5,115,0,0,
        92,93,5,101,0,0,93,94,5,32,0,0,94,12,1,0,0,0,95,96,5,119,0,0,96,
        97,5,104,0,0,97,98,5,105,0,0,98,99,5,108,0,0,99,100,5,101,0,0,100,
        101,5,32,0,0,101,14,1,0,0,0,102,103,5,61,0,0,103,16,1,0,0,0,104,
        105,5,61,0,0,105,106,5,61,0,0,106,18,1,0,0,0,107,108,5,33,0,0,108,
        109,5,61,0,0,109,20,1,0,0,0,110,111,5,60,0,0,111,22,1,0,0,0,112,
        113,5,62,0,0,113,24,1,0,0,0,114,115,5,60,0,0,115,116,5,61,0,0,116,
        26,1,0,0,0,117,118,5,62,0,0,118,119,5,61,0,0,119,28,1,0,0,0,120,
        121,5,32,0,0,121,122,5,97,0,0,122,123,5,110,0,0,123,124,5,100,0,
        0,124,125,5,32,0,0,125,30,1,0,0,0,126,127,5,32,0,0,127,128,5,111,
        0,0,128,129,5,114,0,0,129,130,5,32,0,0,130,32,1,0,0,0,131,132,5,
        84,0,0,132,133,5,114,0,0,133,134,5,117,0,0,134,135,5,101,0,0,135,
        34,1,0,0,0,136,137,5,70,0,0,137,138,5,97,0,0,138,139,5,108,0,0,139,
        140,5,115,0,0,140,141,5,101,0,0,141,36,1,0,0,0,142,143,5,40,0,0,
        143,38,1,0,0,0,144,145,5,41,0,0,145,40,1,0,0,0,146,147,5,42,0,0,
        147,42,1,0,0,0,148,149,5,47,0,0,149,44,1,0,0,0,150,151,5,43,0,0,
        151,46,1,0,0,0,152,153,5,45,0,0,153,48,1,0,0,0,154,155,5,123,0,0,
        155,50,1,0,0,0,156,157,5,125,0,0,157,52,1,0,0,0,158,160,7,0,0,0,
        159,158,1,0,0,0,160,161,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,
        162,54,1,0,0,0,163,167,7,1,0,0,164,166,7,2,0,0,165,164,1,0,0,0,166,
        169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,56,1,0,0,0,169,167,
        1,0,0,0,170,172,7,3,0,0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,58,1,0,0,0,175,177,7,4,0,0,176,175,1,
        0,0,0,177,178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,180,1,
        0,0,0,180,181,6,29,0,0,181,60,1,0,0,0,5,0,161,167,173,178,1,6,0,
        0
    ]

class gramatykaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    INT = 27
    STRING = 28
    NEWLINE = 29
    WS = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'print '", "'input'", "'output '", "'if '", "' else '", 
            "'while '", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "' and '", "' or '", "'True'", "'False'", "'('", "')'", "'*'", 
            "'/'", "'+'", "'-'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "STRING", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "INT", "STRING", "NEWLINE", "WS" ]

    grammarFileName = "gramatyka.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


