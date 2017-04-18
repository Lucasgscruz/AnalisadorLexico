#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from files import *
from erros import *
import re
from dicionario import *


def findTokens(source):
    i = 0
    linha = 0
    coluna = 0
    tokens = []
    tokenAux = ""

    while(i < len(source)):
        tokenAux += source[i]
        coluna += 1

        if (tokenAux == " "):  # Eliminar espaços
            tokenAux = ""
        else:

            if(tokenAux == '\n'):
                linha += 1
                coluna = 0
                tokenAux = ""

            if(tokenAux == '/'):   # verifica comentarios
                if(source[i + 1] == '/'):
                    tokenAux = ""
                    i += 1
                    while (source[i] != '\n'):
                        i += 1
                    else:
                        linha += 1
                        coluna = 0

                elif(source[i + 1] == '*'):  # ???
                    tokenAux = ""
                    i += 2
                    while (source[i] != '*' and source[i + 1] != '/'):
                        if(source[i] == '\n'):
                            linha += 1
                            coluna = 0
                        i += 1
                    else:
                        i += 2

            if(i + 1 < len(source)):
                if(re.match(r'^[a-zA-z0-9_]+$', tokenAux)):  # Pode ser um identificador ou uma palavra reservada.
                    if((source[i + 1] in delimitadores) or
                       (source[i + 1] in aritmeticos) or
                       (source[i + 1] in logicos) or
                       source[i + 1] == "\n"):
                        tokens.append(tokenAux)
                        tokenAux = ""

                if(re.match(r'([-\d]+[.]*[\d]+)', tokenAux)):  # verifica numeros
                    if((source[i + 1] in delimitadores) or
                        (source[i + 1] in aritmeticos) or
                        (source[i + 1] in logicos) or
                       source[i + 1] == '\n'):
                        tokens.append(tokenAux)
                        tokenAux = ""

                if(tokenAux == '='):    # verifica atribuição
                    if(re.match(r'^[-0-9.]+$', source[i + 1]) or
                       re.match(r'^[a-zA-z0-9_]+$', source[i + 1]) or
                       source[i + 1] == ' '):
                        tokens.append(tokenAux)
                        tokenAux = ""

                if(tokenAux in delimitadores):  # verifica delimitadores
                    tokens.append(tokenAux)
                    tokenAux = ""

                if(tokenAux in aritmeticos):  # verifica aritmeticos
                    tokens.append(tokenAux)
                    tokenAux = ""

                if(tokenAux in logicos):  # verifica logicos
                    if(str(tokenAux + source[i + 1] in uniaoLogicos) or
                       source[i + 1] == ' ' or
                       source[i + 1] == r'^[-0-9.]+$' or
                       source[i + 1] == r'^[a-zA-z]+$'):

                    # Reconhecimento de dois simbolos logicos juntos
                    #    if(re.match(r'^[-0-9.]+$', source[i+1])):
                    #         tokens.append(tokenAux)
                    #         tokenAux = ""
                    #    else:
                    #        tokens.append(tokenAux + source[i+1])
                    #        tokenAux = ""
                    #        i += 1
                        tokens.append(tokenAux)
                        tokenAux = ""

        i += 1

    print tokens
    return tokens


def findErros(tokens):
    for lexema in tokens:
        # Encontrar identificadores errados
        if(re.match(r'([\d]+[a-zA-z_]+)', lexema)):
            setListaErros(getErro(02, 1, 1))
        if(lexema in logicos and
          ((tokens[tokens.index(lexema)+2] in logicos) or
          (tokens[tokens.index(lexema)+2] in aritmeticos))):
            setListaErros(getErro(02, 1, 12323))

    for i in (getListaErros()):
        print i


def main():
    try:
        sys.argv[1]
    except Exception:
        print getErro(00, None, None)
        return None

    if(checarExtensao(sys.argv[1]) != 1):
        print getErro(01, None, None)
        return None

    source = readSource(sys.argv[1])
    tokens = findTokens(source)
    findErros(tokens)


if __name__ == '__main__':
    main()
