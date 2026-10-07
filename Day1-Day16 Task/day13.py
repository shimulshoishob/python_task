# debugging technique
#TODO 1: operator related error
#TODO 2: Compare related error
#TODO 3: Array index out of bounds(AIOB)
#TODO 4: Random number generator from array index (AIOB)
#TODO 5: for loop range() function range(5)=0,1,2,3,4 range(1,5)=1,2,3,4
#TODO 6: use try...catch preventing code crash

try:
    age = int(input("enter age: "))
    # if user input non-numerical value then the code will crash and provide valueError
    # to solve the problem use try... except bock
except ValueError:
    print("enter a numerical value like 12. try again")
    age = int(input("enter age: "))

if age < 20:
    print("age is too young")
else :
    print("age is too old")



import random
import maths
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random. randint(1,3)
        new_item = maths.add (new_item, item)
        b_list. append (new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

#TODO 7: use pycharm debugger and step by step debug code
#TODO 8: Take break, Have a cup of coffe or nape and try it tomorrow
#TODO 9: Asking friend and stake overflow
#TODO 10: Run often, don't wait to finish all task.