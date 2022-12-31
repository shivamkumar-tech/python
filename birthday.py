import pyfiglet
from datetime import date


today = date.today()
name = input("Enter the name of Client...")

# Clent's Birth Date
date_of_birth = date(2000, 12, 31)

# Match the month and date of Cient's birthdate with current date...
birthday = date(today.year, date_of_birth.month, date_of_birth.day)
days_until_birthday = (birthday-today).days

days_alive = (today-date_of_birth).days

total_years = days_alive//365


if days_until_birthday > 0:
	print( 'It\'s ' + str(days_until_birthday) + ' days until your Birthday')
elif days_until_birthday == 0:
    print(  "it's your " + str(total_years) + 'th Birthday! ')
    wish = pyfiglet.figlet_format("HAPPY BIRTH DAY "+name, font = "digital")
    print(wish)
else:
	print( "You'll have to wait until next year for another birthday")





