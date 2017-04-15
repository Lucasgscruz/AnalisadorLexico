#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from files import *
from erros import *
import re
from dicionario import *


def construirTabela(source):
    linha = 0
    coluna = 0
    tokens = []
    tokenAux = ""
    contFind = 0

    for i in source:
        linha += 1
        coluna = 0
        tokenAux = ""

        for j in xrange(0, len(i)):
            coluna += 1
            tokenAux += i[j]

            if(tokenAux == '//'):    # verifica se a linha é um comentario
                coluna = 0
                tokenAux = ""
                break
            for valor in tabela:
                if(tokenAux == "(" or
                   tokenAux == ")" or
                   tokenAux == "{" or
                   tokenAux == "}" or
                   tokenAux == "[" or
                   tokenAux == "]" or
                   tokenAux == ";" or
                   tokenAux == "," or
                   tokenAux == "'" or
                   tokenAux == '"'
                    ): # Verificaçao de simbolos atomicos
                    tokens.append(tokenAux)
                    tokenAux = ""
                elif(re.match(valor[1], tokenAux)):
                    contFind += 1
            if(contFind == 1 ):
                tokens.append(tokenAux)
                tokenAux = ""
            contFind = 0

    print tokens

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
    construirTabela(source)


if __name__ == '__main__':
    main()
