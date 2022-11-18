import random


# r =[.55, .28, .12, .0375, .01, .0025]
# l =[.25, 1]
# s =[.125, .25, .375, .50, .625, .75, .875, 1]

# color = {
#     "white": s[0],
#     "black": s[1], 
#     "gray": s[2], 
#     "red": s[3],
#     "blue": s[4],
#     "yellow": s[5],
#     "orange": s[6],
#     "green": s[7],
# }

# item = (rare * livery * specific)/quantity



rarity = random.randint(1, 1000)

if rarity >= 1 and rarity <= 5: loot = ("\033[1;31m mythical ")
elif rarity >= 6 and rarity <= 25: loot = ("\033[1;33m legendary ")
elif rarity >= 26 and rarity <= 75: loot = ("\033[1;35m epic ")
elif rarity >= 76 and rarity <= 200: loot = ("\033[1;34m rare ") 
elif rarity >= 201 and rarity <= 500: loot = ("\033[1;32m uncommen ")
elif rarity >= 501 and rarity <= 1000: loot = ("\033[1;0m common ")

print("\033[1;0m Je hebt een" + loot + "\033[1;0mitem gekregen!!")
