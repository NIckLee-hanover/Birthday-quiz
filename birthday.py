"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

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
"""
from datetime import datetime
from calendar import month_name

months = list (["January", "Febuary", "March", "April", "May", "June", "Juyl", "August", "September", "October", "November", "December"])

todaymonth = datetime.today().month
todaydate = datetime.today().day


name = input ("Hello, what is your name? ")
month1 = input ("Hi " + name + ", what was the name of the month you were born in? ")
#year = int (input ("And what year were you born in, " + name + "? "))
#day = int (input ("And the day? "))
month2 = datetime.today().month
""" this one of my failed attemps at getting this to work, I resorted to my weak JS knowledge.
x = 0
while (month1 != str(months[x]) for x in range (0,12)) and x <= 12:
     print (x)
     x = x + 1
month1 = x
print (month1)
"""
num1 = 0
while num1 < 13:
    if month1 == months[num1]:
        month1 = num1
    if num1 == 12:
        print ("Sorry I didn't understand that month name!")
        break
    num1 += 1
print (month1)




