# if condition1 :
#     print("YES-1")
#elif condition2 :
#     print("YES-2")
# else:
#     print("NO")


# print("Welcome to the rollercoaster !")
# height = int(input("Enter your height in cm: "))
# if height >= 120:
#     print("You can ride the rollercoaster !")
# else:
#     print("Sorry, you cannot ride the rollercoaster !\n\n")



# % modulo operator or reminder operator
# print("Check number : Even or odd")
# number = int(input("Enter your number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("Welcome to the rollercoaster !")
height = int(input("Enter your height in cm: "))
ticket =0
if height >= 120:
    age = int(input("Enter your age: "))
    if age > 18:
        ticket = 12
        if (age >=45) and (age <=55):
            ticket =0
    elif (age >=12) and (age <= 18):
        ticket = 7
    else:
        ticket = 5
    click = bool(input("Do you click photos?"))
    if click :
        if ticket > 0 :
            ticket += 3
    else:
        ticket += 0
    print("Your ticket price is: ", ticket)
    print("Thank you for playing!")
else:
    print("Sorry, you cannot ride the rollercoaster !\n\n")
