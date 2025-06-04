# Generated from Calc/CalcParser.g4 by ANTLR 4.13.2
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
        4,1,9,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,45,8,4,10,4,12,4,48,9,4,1,5,1,5,1,5,1,5,1,5,3,5,55,8,5,1,5,0,
        2,6,8,6,0,2,4,6,8,10,0,0,55,0,12,1,0,0,0,2,15,1,0,0,0,4,18,1,0,0,
        0,6,21,1,0,0,0,8,35,1,0,0,0,10,54,1,0,0,0,12,13,3,6,3,0,13,14,5,
        0,0,1,14,1,1,0,0,0,15,16,3,8,4,0,16,17,5,0,0,1,17,3,1,0,0,0,18,19,
        3,10,5,0,19,20,5,0,0,1,20,5,1,0,0,0,21,22,6,3,-1,0,22,23,3,8,4,0,
        23,32,1,0,0,0,24,25,10,3,0,0,25,26,5,1,0,0,26,31,3,8,4,0,27,28,10,
        2,0,0,28,29,5,2,0,0,29,31,3,8,4,0,30,24,1,0,0,0,30,27,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,7,1,0,0,0,34,32,1,0,0,
        0,35,36,6,4,-1,0,36,37,3,10,5,0,37,46,1,0,0,0,38,39,10,3,0,0,39,
        40,5,3,0,0,40,45,3,10,5,0,41,42,10,2,0,0,42,43,5,4,0,0,43,45,3,10,
        5,0,44,38,1,0,0,0,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,9,1,0,0,0,48,46,1,0,0,0,49,55,5,7,0,0,50,51,5,5,0,0,51,
        52,3,6,3,0,52,53,5,6,0,0,53,55,1,0,0,0,54,49,1,0,0,0,54,50,1,0,0,
        0,55,11,1,0,0,0,5,30,32,44,46,54
    ]

class CalcParser ( Parser ):

    grammarFileName = "CalcParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "Surrogate_id_SYMB_0", "Surrogate_id_SYMB_1", 
                      "Surrogate_id_SYMB_2", "Surrogate_id_SYMB_3", "Surrogate_id_SYMB_4", 
                      "Surrogate_id_SYMB_5", "INTEGER", "WS", "ErrorToken" ]

    RULE_start_Exp = 0
    RULE_start_Exp1 = 1
    RULE_start_Exp2 = 2
    RULE_exp = 3
    RULE_exp1 = 4
    RULE_exp2 = 5

    ruleNames =  [ "start_Exp", "start_Exp1", "start_Exp2", "exp", "exp1", 
                   "exp2" ]

    EOF = Token.EOF
    Surrogate_id_SYMB_0=1
    Surrogate_id_SYMB_1=2
    Surrogate_id_SYMB_2=3
    Surrogate_id_SYMB_3=4
    Surrogate_id_SYMB_4=5
    Surrogate_id_SYMB_5=6
    INTEGER=7
    WS=8
    ErrorToken=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CalcParser.ExpContext,0)


        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_start_Exp




    def start_Exp(self):

        localctx = CalcParser.Start_ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_Exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.exp(0)
            self.state = 13
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)


        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_start_Exp1




    def start_Exp1(self):

        localctx = CalcParser.Start_Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start_Exp1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.exp1(0)
            self.state = 16
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(CalcParser.Exp2Context,0)


        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_start_Exp2




    def start_Exp2(self):

        localctx = CalcParser.Start_Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start_Exp2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.exp2()
            self.state = 19
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Coercion_Exp_3Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExpContext
            super().__init__(parser)
            self.p_3_1 = None # Exp1Context
            self.copyFrom(ctx)

        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)



    class ESubContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExpContext
            super().__init__(parser)
            self.p_2_1 = None # ExpContext
            self.p_2_3 = None # Exp1Context
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_1(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_1, 0)
        def exp(self):
            return self.getTypedRuleContext(CalcParser.ExpContext,0)

        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)



    class EAddContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExpContext
            super().__init__(parser)
            self.p_1_1 = None # ExpContext
            self.p_1_3 = None # Exp1Context
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_0(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_0, 0)
        def exp(self):
            return self.getTypedRuleContext(CalcParser.ExpContext,0)

        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)




    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalcParser.Coercion_Exp_3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 22
            localctx.p_3_1 = self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.EAddContext(self, CalcParser.ExpContext(self, _parentctx, _parentState))
                        localctx.p_1_1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(CalcParser.Surrogate_id_SYMB_0)
                        self.state = 26
                        localctx.p_1_3 = self.exp1(0)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.ESubContext(self, CalcParser.ExpContext(self, _parentctx, _parentState))
                        localctx.p_2_1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 27
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 28
                        self.match(CalcParser.Surrogate_id_SYMB_1)
                        self.state = 29
                        localctx.p_2_3 = self.exp1(0)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_exp1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Coercion_Exp1_3Context(Exp1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Exp1Context
            super().__init__(parser)
            self.p_3_1 = None # Exp2Context
            self.copyFrom(ctx)

        def exp2(self):
            return self.getTypedRuleContext(CalcParser.Exp2Context,0)



    class EDivContext(Exp1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Exp1Context
            super().__init__(parser)
            self.p_2_1 = None # Exp1Context
            self.p_2_3 = None # Exp2Context
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_3(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_3, 0)
        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)

        def exp2(self):
            return self.getTypedRuleContext(CalcParser.Exp2Context,0)



    class EMulContext(Exp1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Exp1Context
            super().__init__(parser)
            self.p_1_1 = None # Exp1Context
            self.p_1_3 = None # Exp2Context
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_2, 0)
        def exp1(self):
            return self.getTypedRuleContext(CalcParser.Exp1Context,0)

        def exp2(self):
            return self.getTypedRuleContext(CalcParser.Exp2Context,0)




    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalcParser.Coercion_Exp1_3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 36
            localctx.p_3_1 = self.exp2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.EMulContext(self, CalcParser.Exp1Context(self, _parentctx, _parentState))
                        localctx.p_1_1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(CalcParser.Surrogate_id_SYMB_2)
                        self.state = 40
                        localctx.p_1_3 = self.exp2()
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.EDivContext(self, CalcParser.Exp1Context(self, _parentctx, _parentState))
                        localctx.p_2_1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        self.match(CalcParser.Surrogate_id_SYMB_3)
                        self.state = 43
                        localctx.p_2_3 = self.exp2()
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_exp2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Coercion_Exp2_2Context(Exp2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Exp2Context
            super().__init__(parser)
            self.p_2_2 = None # ExpContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(CalcParser.Surrogate_id_SYMB_5, 0)
        def exp(self):
            return self.getTypedRuleContext(CalcParser.ExpContext,0)



    class EIntContext(Exp2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.Exp2Context
            super().__init__(parser)
            self.p_1_1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(CalcParser.INTEGER, 0)



    def exp2(self):

        localctx = CalcParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exp2)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = CalcParser.EIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                localctx.p_1_1 = self.match(CalcParser.INTEGER)
                pass
            elif token in [5]:
                localctx = CalcParser.Coercion_Exp2_2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(CalcParser.Surrogate_id_SYMB_4)
                self.state = 51
                localctx.p_2_2 = self.exp(0)
                self.state = 52
                self.match(CalcParser.Surrogate_id_SYMB_5)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.exp_sempred
        self._predicates[4] = self.exp1_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




