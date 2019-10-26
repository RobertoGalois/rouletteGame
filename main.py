#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

import random
import math
import gameMsgs
import gameFeatures

def main():

	userMoney = 500

	gameMsgs.welcomeMsg()
	while (userMoney > 0):
		userMoney = gameFeatures.game(userMoney)

	gameMsgs.goodbyeMsg()

#end main()

main()
