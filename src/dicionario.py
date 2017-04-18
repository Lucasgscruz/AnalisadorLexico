#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ != '__main__':

    delimitadores = [' ', '(', ')', '[', ']', '{', '}', ';', ',', "'", '"']
    aritmeticos = ["%", "+", "-", "/", "*", "^"]
    logicos = ['>', '<', '!', '&', '=', '|']
    uniaoLogicos = ['>=', '<=', '==', '&&', '||', '!=']
    reservadas = ['if', 'else', 'break', 'while',
                  'print', 'char', 'int', 'float','for', 'return']

        # tabela = [
        #     ['PlvReservada', "if"],
        #     ['PlvReservada', "else"],
        #     ['PlvReservada', "for"],
        #     ['PlvReservada', "while"],
        #     ['PlvReservada', "int"],
        #     ['PlvReservada', "float"],
        #     ['PlvReservada', "char"],
        #     ['PlvReservada', "return"],
        #     ['PlvReservada', "continue"],
        #     ['PlvReservada', "print"],
        #     ['PlvReservada', "break"],
        #     #['identificador', r'^[a-zA-z0-9_]+$'],
        #     ['numero', r'^[-0-9.]+$'],
        #     ['opLogico', "&&"],
        #     #['opLogico', "||"],
        #     ['opLogico', "<"],
        #     ['opLogico', ">"],
        #     ['opLogico', "<="],
        #     ['opLogico', ">="],
        #     ['opLogico', "="],
        #     ['opLogico', "=="],
        #     ['opLogico', "!="],
        #     ['opAritmetico', '"'],
        # ]
