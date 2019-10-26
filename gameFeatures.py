#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

import random
import math

def atoi(p_str):

	retInt = 0

	try:
		retInt = int(p_str)
	except ValueError:
		retInt = -1

	return (retInt)

#end atoi()

def	game(p_userMoney):

	randomNumber = random.randrange(0, 50)
	chosenNumber = -1
	bet = 0
	gain = 0

	print("=============================")
	print("Nouvelle partie de Roulette !")
	print("Vous disposez de", p_userMoney, "$ !")

	while (bet > p_userMoney or bet <= 0):
		bet = atoi(input("Combien misez-vous: "))

		if (bet > p_userMoney):
			print("Vous n'avez pas assez d'argent pour effectuer une telle mise !")
		elif (bet <= 0):
			print("Vous devez indiquer une somme strictement positive !")

	while (chosenNumber < 0 or chosenNumber > 49):
		chosenNumber = atoi(input("Choisissez un nombre entre 0 et 49: "))


	print("-----------------------------------")
	print("numéro tiré:", randomNumber, "! Votre numéro:", chosenNumber, "!")
	print("-----------------------------------")

	if (chosenNumber == randomNumber):
		gain = 3 * bet
		print("Bravo vous avez gagné 3 fois votre mise soit", gain, "$ !")

	elif ((chosenNumber % 2) == (randomNumber % 2)):
		gain = math.ceil(bet / 2)
		print("Bien ! Concordance de couleur ! Vous avez gagné la moitié de votre mise soit", gain, "$ !")

	else:
		print("Vous avez perdu votre mise de", bet, "$ !")
		gain = -bet

	return (p_userMoney + gain)

#end game()
