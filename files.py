#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

if __name__ != '__main__':
    def checarExtensao(source):
        """Função que verifica a extensão do arquivo passado com o código fonte."""

        ext = os.path.splitext(source)
        if(ext[1] == ".c"):
            return 1
        return 0

    def readSource(source):
        """Função que realiza a leitura do código fonte."""

        arq = open(source, 'r')
        return arq.read()

    def writeTable():
        pass
