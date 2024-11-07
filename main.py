import random
from time import sleep
sleep(1)
print("Welcome to Number Guessing game!")
sleep(1)
print("In This Game You'll Try To Guess To Correct Number From 'X' To 'Z'")
print("'X','Z' are By Your Choice.")
X = int(input("Please Enter X Value: "))
Z = int(input("Please Enter Z Value: "))
 
The_Number = random.randint(X,Z)
print("Great, Now Choose one of the following Modes:")
print("1. Easy    (10 chances)")
print("2. Meduim  (7 chances)")
print("3. Hard    (4 chances)")

Difficulty = int(input("Enter Your Choice: "))
Attempts = 0
if Difficulty == 1 :
    print("Great! Your have selected the Easy level")
    sleep(0.5)
    print("Let's Start the Game!!")
    Easy_Mode = 10
    Remaining_Easy = 10
    while Attempts <= Easy_Mode :
        Attempts += 1
        Remaining_Easy -= 1
        Value_By_User = int(input("Enter Your Guess: "))
        if  Value_By_User == The_Number :
            print(f"Congrats You Guessed The Number in {Attempts} Attempts")
            exit()
        else :
            print(f"Inccorect, {Remaining_Easy} Chances remaining ")
elif Difficulty == 2 :
    print("Great! Your have selected the Meduim level")
    sleep(0.5)
    print("Let's Start the Game!!")
    Meduim_Mode = 7
    Remaining_Meduim = 7
    while Attempts <= Meduim_Mode :
        Attempts += 1
        Remaining_Meduim -= 1
        Value_By_User = int(input("Enter Your Guess: "))
        if Value_By_User == The_Number :
            print(f"Congrats You Guessed The Number in {Attempts} Attempts")
            exit()
        else : 
            print(f"Inccorect, {Remaining_Meduim} Chances remaining ")
elif Difficulty == 3 :
    print("Great! Your have selected the Hard level")
    sleep(0.5)
    print("Let's Start the Game!!")
    Hard_Mode = 4
    Remaining_Hard = 4
    while Attempts <= Hard_Mode :
        Attempts += 1
        Remaining_Hard -= 1
        Value_By_User = int(input("Enter Your Guess: "))
        if Value_By_User == The_Number :
            print(f"Congrats You Guessed The Number in {Attempts} Attempts")
            exit()
        else : 
            print(f"Inccorect, {Remaining_Hard} Chances remaining ")
