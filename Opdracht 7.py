import datetime as dt
import dateutil
from dateutil.relativedelta import relativedelta

date_now = dt.date.today().strftime("%d %m %Y")
date_y18 = dt.date.today()-relativedelta(years=18)
date_y18 = date_y18.strftime("%d %m %Y") 
date_format = "%d %m %Y"

x = dt.datetime.now()
print("De datum van vandaag is " + x.strftime("%d %m %Y"))

while True:
    try:
        leeftijd = (input("Vul hier uw geboorte datum in als DD MM YYYY: "))

        leeftijd = dt.datetime.strptime(leeftijd, date_format)
    except ValueError:
        print("Typ AUB een getal in")
        break
    if leeftijd >= dt.datetime.strptime(date_y18, date_format) and leeftijd <= dt.datetime.strptime(date_now, date_format):
        print("U bent niet oud genoeg om te rijden")
        break
    else: leeftijd
    print("U bent oud genoeg om te rijden")
    break
    