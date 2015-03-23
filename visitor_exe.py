"""
"""

from antlr4 import *
from muVisitor import *
from muParser import muParser as Parser
import pdb


class visitorExe(muVisitor):

    varMem = dict()

    # Visit a parse tree produced by muParser#parse.
    def visitParse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#assignment.
    def visitAssignment(self, ctx):
        # pdb.set_trace()
        idStr = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.varMem[idStr] = value
        return self.varMem.update()


    # Visit a parse tree produced by muParser#if_stat.
    def visitIf_stat(self, ctx):
       #  pdb.set_trace()

        conditions = ctx.condition_block()

        evaluatedBlock = False

        for condition in conditions:
            evaluated = self.visit(condition.expr())
            if evaluated:
                evaluatedBlock = True
                self.visit(condition.stat_block())

        if (evaluatedBlock is not None) and ctx.stat_block() != None:
            self.visit(ctx.stat_block())
        return None


    # Visit a parse tree produced by muParser#condition_block.
    def visitCondition_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#stat_block.
    def visitStat_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#while_stat.
    def visitWhile_stat(self, ctx):

        value = self.visit(ctx.expr())

        while value:
            self.visit(ctx.stat_block())
            value = self.visit(ctx.expr())
        return None

    # Visit a parse tree produced by muParser#until_stat.
    def visitUntil_stat(self, ctx):
        pdb.set_trace()

        self.visit(ctx.block())
        value = self.visit(ctx.expr())

        while not value:
            self.visit(ctx.block())
            value = self.visit(ctx.expr())
        return None

    # Visit a parse tree produced by muParser#log.
    def visitLog(self, ctx):
        value = self.visit(ctx.expr())
        print  "log :" , value
        return value


    # Visit a parse tree produced by muParser#andExpr.
    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left and right


    # Visit a parse tree produced by muParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx):
        val = self.visit(ctx.expr())
        return -val



    # Visit a parse tree produced by muParser#relationalExpr.
    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        result = {
            Parser.LT: left < right,
            Parser.LTEQ: left <= right,
            Parser.GT: left > right,
            Parser.GTEQ: left >= right
        }.get(op,None)

        return result


    def visitAtomExpr(self, ctx):
        return self.visitChildren(ctx)


    def visitAdditiveExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        # pdb.set_trace()
        if op ==Parser.PLUS:
            result = (str(left) + str(right)) if (type(left) <> type(right)) else (left + right)
        elif op == Parser.MINUS:
            result = left - right
        else:
            result = None

        return result


    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        result = {
            Parser.EQ: left == right,
            Parser.NEQ: left != right
        }.get(op, None)

        return result


    # Visit a parse tree produced by muParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # pdb.set_trace()
        op = ctx.op.type
        result = {
            Parser.MULT:  left * right,
            Parser.DIV: left / right,
            Parser.MOD: left % right,
        }.get(op,None)
        return result


    # Visit a parse tree produced by muParser#orExpr.
    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left or right


    # Visit a parse tree produced by muParser#powExpr.
    def visitPowExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return  pow(left, right)


    # Visit a parse tree produced by muParser#notExpr.
    def visitNotExpr(self, ctx):
        value = self.visit(ctx.expr())
        return not value


    # Visit a parse tree produced by muParser#parExpr.
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by muParser#numberAtom.
    def visitNumberAtom(self, ctx):
        return float(ctx.getText())


    # Visit a parse tree produced by muParser#booleanAtom.
    def visitBooleanAtom(self, ctx):
        pdb.set_trace()
        tf = ctx.getText()
        if tf == 'true':
            bl = True
        elif tf == 'false':
            bl = False
        else:
            bl = None

        return bl


    # Visit a parse tree produced by muParser#idAtom.
    def visitIdAtom(self, ctx):
        idStr = ctx.getText()
        if idStr in self.varMem.keys():
            value = self.varMem[idStr]
        else:
            value =  None
        return  value


    # Visit a parse tree produced by muParser#stringAtom.
    def visitStringAtom(self, ctx):
        theStr = ctx.getText()
        return theStr


    # Visit a parse tree produced by muParser#nilAtom.
    def visitNilAtom(self, ctx):
        return None


