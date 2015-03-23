# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by muParser.

class muVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#if_stat.
    def visitIf_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#condition_block.
    def visitCondition_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#stat_block.
    def visitStat_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#while_stat.
    def visitWhile_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#until_stat.
    def visitUntil_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#log.
    def visitLog(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#andExpr.
    def visitAndExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#relationalExpr.
    def visitRelationalExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#atomExpr.
    def visitAtomExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#additiveExpr.
    def visitAdditiveExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#equalityExpr.
    def visitEqualityExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#orExpr.
    def visitOrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#powExpr.
    def visitPowExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#parExpr.
    def visitParExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#numberAtom.
    def visitNumberAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#booleanAtom.
    def visitBooleanAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#idAtom.
    def visitIdAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#stringAtom.
    def visitStringAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by muParser#nilAtom.
    def visitNilAtom(self, ctx):
        return self.visitChildren(ctx)


