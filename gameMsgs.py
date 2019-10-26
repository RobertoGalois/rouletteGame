#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

def welcomeMsg():
	print("-=================================-")
	print("| BIENVENUE AU --[Z-CASINO]-- !!! |")
	print("-=================================-\n")
#end welcomeMsg()

def goodbyeMsg():
	print("\n|||||||||||||||||||||||||||||")
	print("|VOUS N'AVEZ PLUS DE SOUS ! |")
	print("|     END OF THE GAME     ! |")
	print("|||||||||||||||||||||||||||||\n")
#end goodbyeMsg()

def goodbyeCancelMsg(pMoney):
	print("\n||||||||||||||||||||||||||||||||||")
	print("|VOUS CHOISISSEZ DE VOUS ARRÊTER |")
	print("|      ... PETIT JOUEUR !        |")
	print("|", "Vous partez avec {0} $".format(pMoney).center(32), "|", sep="")
	print("||||||||||||||||||||||||||||||||||\n")

