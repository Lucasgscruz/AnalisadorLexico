#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

tabela = [
    ['PlvReservada', "if"],
    ['PlvReservada', "else"],
    ['PlvReservada', "for"],
    ['PlvReservada', "while"],
    ['PlvReservada', "int"],
    ['PlvReservada', "float"],
    ['PlvReservada', "char"],
    ['PlvReservada', "return"],
    ['PlvReservada', "continue"],
    ['PlvReservada', "print"],
    ['PlvReservada', "break"],
    ['identificadores', r'sdfnfvfvjxvxcvcvxcvxcvj'],
    ['numeros', r'[0-9]'],
    ['opLogicos', "jjjj"],
    ['opAritmeticos', "kkkkk"],

]


# print tabela[15][1]
# print "(" in tabela[15][1]
#print  re.search(tabela[15][1], '(')

# for valor in tabela:
#     print valor
#     if ("lucas" in valor[1] or re.match(valor[1], "lucas")):
#         print "casou"
#     else:
#         print 'nao casoou'

# if ("lucas" in tabela[1][1]):
#     print "funciona"

#print len(tabela)
# if( a in tabela[0][1] or re.match(tabela[0][1],a) ):
#      print 'entrouoiiiiiiiiiiiiiiiiiiiiiiiiiii'


# ['identificadores', r'_|[a-z|[A-Z]|[0-9]|_|[a-z]|A-Z]|_'],
