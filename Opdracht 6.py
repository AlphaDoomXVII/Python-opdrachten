import sys

leeftijd = 0

while True:
    try:
        leeftijd = int(input("Typ hier uw leeftijd: "))
    except ValueError:
        print("Typ AUB een getal in")
        break
    if leeftijd >= 18:
        print("U bent oud genoeg om te rijden")
        break
    elif leeftijd <= 17: 
        print("U bent niet oud genoeg om te rijden")
        break
    else: break
    



    












