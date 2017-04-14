#!/usr/bin/python
# -*- coding: utf-8 -*-


class LexicalError(object):
    
    def LexicalError(self,msg, line, col):
    	print "[Warning]: "+"Existe um erro léxico na linha: "+ str(line + 1) +" coluna: "+ str(col + 1)


         