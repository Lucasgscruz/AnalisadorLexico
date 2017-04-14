#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def isEmpty(arg):
	if (len(arg) > 1):
		return 1
	return 0

def ordena(t):
	return (t['linha'], t['coluna'])

def checkFile(file_name):
	ext = os.path.splitext(file_name)
	if(ext[1] == ".c"):
		return 1
	return 0

def readFile(file_name):
	arq = open(file_name, 'r')
	return arq.readlines()

def saveArq(file,list,type):
	arq = open(file,"w")
	if(type == "token"):
		list = sorted(list, key=ordena)
		i = 0
		for x in xrange(0,len(list)):
			if list[x]['palavra'] != "//":
				i = i+1
				if(list[x]['id'] != "-1"):
					palavra = str(i) +"," + str(list[x]['id'])+"\t"+list[x]['palavra'] +"\t"+ str(list[x]['linha']) +"\t"+ str(list[x]['coluna']) + "\n"
				else:
					palavra = str(i)+"\t"+list[x]['palavra'] +"\t"+ str(list[x]['linha']) +"\t"+ str(list[x]['coluna']) + "\n"
				if(x == len(list) -1):
					palavra = str(i)+"\t}\t 1 \t 1\n"
				arq.write(palavra)
	else:
		for x in xrange(0,len(list)):
			palavra = str(list[x]['id'])+"\t"+list[x]['palavra'] +"\t"+ str(list[x]['linha']) +"\t"+ str(10) + "\n"
			arq.write(palavra)
	arq.close()
		