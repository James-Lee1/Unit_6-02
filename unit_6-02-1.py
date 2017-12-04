# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This program displays an enumerated type

from enum import Enum

# an enumerated type of days of the week

Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

day_selected = raw_input('Enter your favorite day of the week: ')

counter = 0
position = None

for day in Days:
    if str(day) == day_selected:
        print(day_selected)
        position = counter + 1
    counter = counter + 1

print("Day " + str(position) + " is your favourite day of the week")
