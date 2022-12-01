import datetime
from dateutil. relativedelta import relativedelta

x = datetime.datetime.now()
print(x.strftime("%d %m %Y"))

leeftijd = int(input("Typ uw geboortedatum hier zoals hierboven eruit ziet "))

if leeftijd >= datetime.datetime.today()-relativedelta(years=18) and datetime.datetime.now():
    print("U bent oud genoeg om te rijden")
else: print("U mag bent niet oud genoeg om te rijden")

print(leeftijd)