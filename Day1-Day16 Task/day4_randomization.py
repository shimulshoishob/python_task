import random
import day4_my_module

#Generate random integer from 1 to 10 including them
random_int = random.randint(1, 10)
print(random_int)

#use my created module code
print(day4_my_module.my_favourite_number)

#random.random() provides 0 to 1, not included 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#extands random number range by multiplying number
random_number_0_to_1 = random.random()*10
print(random_number_0_to_1)


#unifrom not included upper bounds
random_number_0_to_10 = random.uniform(1, 10)
print(random_number_0_to_10)

#head & tail code
coin = random.randint(0,1)
if coin == 0:
    print("Head")
if coin == 1:
    print("Tail")