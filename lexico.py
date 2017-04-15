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
    contStr = 0

    for i in source:
        linha += 1
        coluna = 0
        contStr = 0
        tokenAux = ""

        for j in xrange(0, len(i)):
            coluna += 1
            tokenAux += i[j]
            print tokenAux

            if(tokenAux == '//'):    # verifica se a linha é um comentario
                coluna = 0
                tokenAux = ""
                break

            for valor in tabela:     #Percorre a tabela de simbolos

                if(len(tokenAux) > 0):  # remover espaços no inicio da string tokenAux
                    if (tokenAux[0]== ' '):
                        tokenAux = tokenAux.replace(" ","")

                if(tokenAux == "(" or   # verificação de simbolos atomicos
                   tokenAux == ")" or
                   tokenAux == "{" or
                   tokenAux == "}" or
                   tokenAux == "[" or
                   tokenAux == "]" or
                   tokenAux == ";" or
                   tokenAux == "," or
                   tokenAux == "'" or
                   tokenAux == '"' ):
                   tokens.append(tokenAux)
                   tokenAux = ""

                if(re.match(valor[1], tokenAux)): # verificação da expresssao regular
                    contFind += 1
                    print contFind
                    print valor[1]

            if(contFind == 1 ): # Caso tenha casado com apenas um tipo de token, a string é adicionada na lista
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
