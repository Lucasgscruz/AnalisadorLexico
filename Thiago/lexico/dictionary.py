#!/usr/bin/python
# -*- coding: utf-8 -*-


global dictionary
global listAtt
listAtt = []

global listTokens
listTokens = []

dictionary = {

	'comentários': {
		"//": ["all"]
	}, 
	'associação': {
		"=": [" ", "\t", "letter", "number", "(", "!", "'", '"']
	},
	'lógicos': {
		"==": [" ", "\t", "letter", "number", "(", "!", "'", '"'],
		">": [" ", "\t", "letter", "number", "(", "!", "'", '"'],
		"<": [" ", "\t", "letter", "number", "(", "!", "'", '"'],
		">=": [" ", "\t", "letter", "number", "(", "!", "'", '"'],
		"<=": [" ", "\t", "letter", "number", "(", "!", "'", '"'],
		"!=": [" ", "\t", "letter", "number", "(", "'", '"'],
		"&&": [" ", "\t", "("],
		"||": [" ", "\t", "("],
		"!": [" ", "\t", "letter", "("]
	},
	'aritméticos': {
		"%": [" ", "\t", "letter", "number", "("],
		"+": [" ", "\t", "letter", "number", "("],
		"-": [" ", "\t", "letter", "number", "("],
		"/": [" ", "\t", "letter", "number", "("],
		"*": [" ", "\t", "letter", "number", "("],
		"^": [" ", "\t", "letter", "number", "("]
	},
	'reservadas': {
		"if": [" ", "\t", "("],
		"else": [" ", "\t", "("],
		"continue": [" ", "\t", ";"],
		"break": [" ", "\t", ";"],
		"while": [" ", "\t", "("],
		"print": [" ", "\t"],
		"read": [" ", "\t"],
		"int": [" ", "\t"],
		"float": [" ", "\t"],
		"string": [" ", "\t"],
		"char": [" ", "\t"]
	},
	'literais': {
		"'": ["all"],
		'"': ["all"]
	},
	'delimitadores': {
		";": [" ", "\t", "\n", "//"],
		"{": [" ", "\t", "\n"],
		"}": [" ", "\t", "\n"],
		",": [" ", "\t", "letter"],
		"(": [" ", "\t", "letter", "number", "("],
		")": [" ", "\t", "\n", ";", "==", ">", "<", ">=", "<=", "!=", "&&", "||", "!", "%","+","-","/","*","^","{"]
	},
	'caractere' : {
		"letter" : [" ", "\t", "\n", ";", "==", ">", "<", ">=", "<=", "!=", "%","+","-","/","*","^","=",",","(",")","letter","number"],
		"number" : [" ", "\t", "\n", ";", "==", ">", "<", ">=", "<=", "!=", "%","+","-","/","*","^","=",",","(",")","letter","number"]
	}
}