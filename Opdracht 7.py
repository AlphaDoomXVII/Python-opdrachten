import datetime

leeftijd = int(input("uw geboortedatum hier "))

if leeftijd >= datetime.datetime.today:
    print("u bent oud genoeg om te rijden")
else: print("u mag bent niet oud genoeg om te rijden")
