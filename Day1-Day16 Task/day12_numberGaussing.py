import random
def guess(num):
    if num == numberGauss:
        print("you got it!")
        exit()
    elif num > numberGauss:
        print("Too High!")
    elif num < numberGauss:
        print("Too Low!")
print("Welcome to numberGauss!")
numberGauss = random.randint(1,100)
level = str(input("Difficulty level: (hard / easy)"))
level = level.lower()
life = 0
if level == "hard":
    life = 5
    while life:
        number = int(input("Guess number between 1 and 100: "))
        guess(number)
        life -= 1
    print("you lose!")
elif level == "easy":
    life = 10
    while life :
        number = int(input("Guess number between 1 and 100: "))
        guess(number)
        life -= 1
    print("you lose!")