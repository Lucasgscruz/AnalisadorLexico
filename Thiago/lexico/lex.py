#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import fileinput
from LexicalError import LexicalError
from dictionary import * 
from arq import *

def saveAtt(palavra,row,col):
	for x in xrange(0,len(listAtt)):
		if(listAtt[x]["palavra"] == palavra):
			return listAtt[x]["id"]
	id = len(listAtt)
	listAtt.append({	
		"id": id,
	   	"palavra": palavra,
	   	"linha" : row,
	   	"coluna" : col
    	})
	return id

def saveTokens(type,palavra,linha,coluna,id):
	if(palavra != '"'):
		listTokens.append({"Tipo": type,"palavra": palavra,"linha": linha + 1,"coluna": coluna + 1,"id": id})

def specialCases(caractere, proxCaratere):
	if ((caractere == "/") & (proxCaratere == "/")):
		return -1
	elif (caractere == "'"):
		return 2
	elif (caractere == '"'):
		return 3
	elif ((caractere == "=") & (proxCaratere == "=")):
		return 1
	elif ((caractere == ">") & (proxCaratere == "=")):
		return 1
	elif ((caractere == "<") & (proxCaratere == "=")):
		return 1
	elif ((caractere == "!") & (proxCaratere == "=")):
		return 1
	elif ((caractere == "&") & (proxCaratere == "&")):
		return 1
	elif ((caractere == "|") & (proxCaratere == "|")):
		return 1
	elif ( ((caractere == "&") & (proxCaratere != "&")) | ((caractere == "|") & (proxCaratere != "|"))):
		return 0

def verifyType(palavra, caractere, tipo,x, linha):
	if(findDictionary(palavra, caractere, tipo) == 1):
		saveTokens(tipo,palavra,x,linha.find(palavra),"-1")
	elif (palavra != ""):
		saveTokens("Attr",palavra,x,linha.find(palavra),saveAtt(palavra,x,linha.find(palavra)))


def findError(caractere, proxCaratere, key):
	isAlpha = 0
	isDigit = 0
	if (dictionary[key][caractere][0] == "all"):
		return 0
	for x in xrange(0,len(dictionary[key][caractere])):		
		if (proxCaratere == dictionary[key][caractere][x]):
			return 0
		if (dictionary[key][caractere][x] == "letter"):
			isAlpha = 1
		if (dictionary[key][caractere][x] == "number"):
			isDigit = 1
	if ((isAlpha == 1) & (proxCaratere.isalpha() == True)):
		return 0
	if ((isDigit == 1) & (proxCaratere.isdigit() == True)):
		return 0
	return 1

def findDictionary(caractere, proxCaratere, key):
	for x, val in dictionary[key].items():
		if (caractere == x):
			if (findError(caractere, proxCaratere, key) == 0):
				return 1
			else:
				return -1
	return 0

def findDictionaryAlpha(caractere, proxCaratere, key):
	isAlpha = 0
	isDigit = 0
	for x, val in dictionary[key].items():
		if ("letter" == x):
			for y in xrange(0,len(dictionary[key][x])):		
				if (proxCaratere == dictionary[key][x][y]):
					return 1
				if (dictionary[key][x][y] == "letter"):
					isAlpha = 1
				if (dictionary[key]["letter"][y] == "number"):
					isDigit = 1
		if ("number" == x):
			for y in xrange(0,len(dictionary[key][x])):		
				if (proxCaratere == dictionary[key][x][y]):
					return 1
				if (dictionary[key][x][y] == "letter"):
					isAlpha = 1
				if (dictionary[key][x][y] == "number"):
					isDigit = 1
	if ((isAlpha == 1) & (proxCaratere.isalpha() == True)):
		return 1
	if ((isDigit == 1) & (proxCaratere.isdigit() == True)):
		return 1
	return 0

def makeTable(arq):
	hasLiteral = 0
	hasSpecialCase = 0
	hasSimpleMarks = 0
	hasDoubleMarks = 0
	flagNumber = 0
	hasError = 0
	count = 0
	for x in xrange(0,len(arq)):
		linha = arq[x]
		palavra = ""
		hasError = 0
		for y in xrange(0,len(linha)):
			if(count == 1):
				count = 0
				continue
			if (((hasSimpleMarks == 0) & (hasDoubleMarks == 0)) | ((hasSimpleMarks == 1) & (linha[y] == "'")) | ((hasDoubleMarks == 1) & (linha[y] == '"'))):
				if ((linha[y].isalpha() == True) & (y+1 < len(linha))):
					if(findDictionaryAlpha(linha[y], linha[y+1], "caractere") == 1):
						hasSpecialCase = 0
						palavra = palavra + linha[y]
						flagNumber = 1
					else:
						hasError = 1
						break
				elif ((flagNumber == 1) & (linha[y].isdigit() == True)):
					if(findDictionaryAlpha(linha[y], linha[y+1], "caractere") == 1):
						hasSpecialCase = 0
						palavra = palavra + linha[y]
					else:
						hasError = 1
						break
				else:
					if (y + 1 < len(linha)):
						specialType = specialCases(linha[y], linha[y+1])
						if (specialType == -1):
							verifyType(linha[y]+linha[y+1],linha[y+2],"comentários",x,linha)
							hasSpecialCase = 1
							verifyType(palavra,linha[y],"reservadas",x,linha)
							palavra = ""
							break
						elif (specialType == 2):
							if (hasSimpleMarks == 0):
								hasSimpleMarks = 1
							else:
								hasSimpleMarks = 0
						elif (specialType == 3):
							if (hasDoubleMarks == 0):
								hasDoubleMarks = 1
							else:
								hasDoubleMarks = 0
								palavra += '"'
								listTokens.append({"Tipo": "palavras","palavra": palavra,"linha": str(x),"coluna": str(linha),"id": str(0)})
								continue
						elif (specialType == 1):
							verifyType(linha[y]+linha[y+1],linha[y+2],"lógicos",x,linha)
							hasSpecialCase = 1
							count = 1
							verifyType(palavra,linha[y],"reservadas",x,linha)
							palavra = ""
							continue
						elif (specialType == 0):
							hasError = 1
							break
					verifyType(palavra,linha[y],"reservadas",x,linha)
					palavra = ""
				if (hasSpecialCase == 0):
					for chave, val in dictionary.items():
						if (y+1 < len(linha)):
							findD = findDictionary(linha[y], linha[y+1], chave)
							if(findD  == 1):
								verifyType(linha[y],linha[y+1],chave,x,linha)
							elif (findD == -1):
								hasError = 1
								break
			if (hasDoubleMarks == 1):
				palavra += linha[y]
			if ((hasDoubleMarks == 0) and (linha[y] == '"')):
				palavra = ""
		if (hasError == 1):
			a = LexicalError()
			a.LexicalError(linha[y],x,y)
	saveArq("tokens.txt",listTokens,"token")
	saveArq("att.txt",listAtt,"")

def main():
	if(isEmpty(sys.argv) == 1):
		if(checkFile(sys.argv[1]) != 1):
			a = LexicalError()
			a.LexicalError("O arquivo informado não está na extensão correta",1,2)
		else:
			arq = readFile(sys.argv[1])
			makeTable(arq)
	else:
		print "help"
		print "Nenhum arquivo foi passado como parametro"
	

if __name__ == '__main__':
    main()