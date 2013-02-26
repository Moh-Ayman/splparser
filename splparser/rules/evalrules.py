#!/usr/bin/env python

from splparser.parsetree import *
from splparser.exceptions import SPLSyntaxError

from splparser.cmdparsers.common.evalfnexprrules import *
from splparser.cmdparsers.common.simplefieldrules import *

from splparser.lexers.evallexer import precedence, tokens

start = 'cmdexpr'

def p_cmdexpr_eval(p):
    """cmdexpr : evalcmd"""
    p[0] = p[1]

def p_eval_evalexpr(p):
    """evalcmd : EVAL oplist"""
    p[0] = ParseTreeNode('EVAL')
    p[0].add_children(p[2].children)

def p_error(p):
    raise SPLSyntaxError("Syntax error in eval parser input!") 
