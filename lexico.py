#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from files import *
from erros import *


def construirTabela(source):
    linha = 0
    coluna = 0


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
