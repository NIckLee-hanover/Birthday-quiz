"""
birthday.py
Author: Nick Lee
Credit: none
Assignment: Birthday quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
//\\//\\//\\
this one of my failed attemps at getting this to work that i didn't delete.
x = 0
while (month1 != str(months[x]) for x in range (0,12)) and x <= 12:
     print (x)
     x = x + 1
month1 = x
print (month1)
"""
from datetime import datetime
from calendar import month_name

# monts list
months = list (["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "extra"])

todaymonth = datetime.today().month
todaydate = datetime.today().day

# sets variables
name = input ("Hello, what is your name? ")
month1 = input ("Hi " + name + ", what was the name of the month you were born in? ")
year = int (input ("And what year were you born in, " + name + "? "))
day = int (input ("And the day? "))

# converts the month name into a number
num1 = 0
while num1 < 13:
    if month1 == months[num1]:
        month1 = int(num1)
        break
    if num1 == 12:
        print ("Sorry I can't understand that month name!")
        break
    num1 += 1

# decides what month zone you were born in
if month1 == 11 or month1 < 2:
    baby = "winter"
elif month1 > 1 and month1 < 5:
    baby = "spring"
elif month1 > 4 and month1 < 8:
    baby = "summer"
else:
    baby = "fall"

# decides what generation you were born in

if year < 1980:
    generation = "stone age"
elif year < 1990:
    generation = "eighties"
elif year < 2000:
    generation = "nineties"
else:
    generation = "two thousands"

# prints the text
if month1 + 1 == todaymonth and day == todaydate:
    print ("Happy birthday!")
elif month1 == 9 and day == 31:
    print ("You were born on Halloween!")
else:
    print ("You are a {0} baby of the {1}".format(baby, generation))


