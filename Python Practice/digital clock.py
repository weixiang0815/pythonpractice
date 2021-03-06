from time import sleep
from os import system as sys

hour = int(input("Please enter a starting hour: "))
minute = int(input("Please enter a starting minute: "))
second = int(input("Please enter a starting second: "))

if hour >= 24 or minute >= 60 or second >= 60:
    print("An error has occurred!")
    exit()

sys("cls")

while True:
    print("Clock: %02d:%02d:%02d" % (hour,  minute,  second))
    second += 1
    if second == 60:
        minute += 1
        second *= 0
    if minute == 60:
        hour += 1
        minute *= 0
    if hour == 24:
        hour *= 0
    sleep(1)
    sys("cls")
