from random import Random

lowest = int(input("Please enter the lowest number: "))
highest = int(input("Please enter the highest number: "))
rd = Random()
answer = rd.randint(lowest, highest)
level = input("Which level would you like to take?(easy/hard/self-challenging) ")
if level.lower() == 'easy':
    while True:
        key = int(input("Please enter your guess: "))
        if key > answer:
            print("It's higher than the answer.")
        elif key < answer:
            print("It's lower than the answer.")
        else:
            print("Good job! Your answer is correct!")
            break
elif level.lower() == 'hard':
    hard_level = rd.randint(1, 10)
    while hard_level > 0:
        if hard_level == 1:
            print("You still have " + str(hard_level) + " more chance. Good luck.")
        else:
            print("You still have " + str(hard_level) + " more chances. Good luck")
        key = int(input("Please enter your guess: "))
        if key > answer:
            print("It's higher than the answer.")
            hard_level -= 1
            if hard_level == 0:
                break
        elif key < answer:
            print("It's lower than the answer.")
            hard_level -= 1
            if hard_level == 0:
                break
        else:
            break
    if hard_level > 0:
        print("Congratulation! You won the hard level challenge!")
    else:
        print("I'm sorry. You didn't guess the answer out before your chances ran to 0.")
else:
    self_chall_level = int(input("Please enter a number as the chances left: "))
    while True:
        if self_chall_level == 1:
            print("You still have "+str(self_chall_level)+" more chance. Good luck.")
        else:
            print("You still have "+str(self_chall_level)+" more chances. Good luck.")
        key = int(input("Please enter your guess: "))
        if key > answer:
            print("It's higher than the answer.")
            self_chall_level -= 1
            if self_chall_level == 0:
                break
        elif key < answer:
            print("It's lower than the answer.")
            self_chall_level -= 1
            if self_chall_level == 0:
                break
        else:
            break
    if self_chall_level > 0:
        print("Congratulation! You won the self-challenging level!")
    else:
        print("I'm sorry. You didn't guess the answer out before your chances ran to 0.")
