import random

rarity = random.randint(1, 1000)

if rarity >= 1 and rarity <= 5: loot = ("\033[1;31m mythical ")
elif rarity >= 6 and rarity <= 25: loot = ("\033[1;33m legendary ")
elif rarity >= 26 and rarity <= 75: loot = ("\033[1;35m epic ")
elif rarity >= 76 and rarity <= 200: loot = ("\033[1;34m rare ") 
elif rarity >= 201 and rarity <= 500: loot = ("\033[1;32m uncommen ")
elif rarity >= 501 and rarity <= 1000: loot = ("\033[1;0m common ")

print("\033[1;0m Je hebt een" + loot + "\033[1;0mitem gekregen!!")
