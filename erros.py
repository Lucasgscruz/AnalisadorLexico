#!/usr/bin/python
# -*- coding: utf-8 -*-


__dicErros__ = {
    00: "[Erro]: Arquivo contendo o código fonte não foi passado!",
    01: "[Erro]: O arquivo passado possui extensão incompatível.",
    02: "[Erro]: Erro léxico na linha "
}


def getErro(chave, linha, coluna):
    """A função retorna a string do erro correspondente contido no dicionário
    de erros."""

    if(linha is None and coluna is None):
        return __dicErros__[chave]
    return __dicErros__[chave] + str(linha) + " e coluna " + str(coluna)
