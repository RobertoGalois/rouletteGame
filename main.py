#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

import random
import math
import gameMsgs
import gameFeatures

def main():

	userMoney = 500

	gameMsgs.welcomeMsg()
	try:
		while (userMoney > 0):
			userMoney = gameFeatures.game(userMoney)
	except KeyboardInterrupt:
		gameMsgs.goodbyeCancelMsg(userMoney)
	else:
		gameMsgs.goodbyeMsg()

#end main()

main()
