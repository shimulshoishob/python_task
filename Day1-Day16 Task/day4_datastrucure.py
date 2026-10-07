import random
#List
state_of_usa = ["Delaware", "Pennsylvania"]
print(state_of_usa[0])
print(state_of_usa[1])

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1]) #it represents last index
#print(fruits[3]) index out of bound/ range

#change item
fruits[1]="Mango"
print(fruits[1])

#add single item on the existing list
fruits.append("papaya")
print(fruits[3]) # now it not show index out of range

#add a bunch of code on end of the existing list
fruits.extend(["dates", "jack fruits", "lichy"])
print(fruits)

#select random fruits
#opt 01
select_fruits = random.randint(0, len(fruits)-1)
print(fruits[select_fruits])

#opt 02
print(random.choice(fruits))

#nested list
vowel = ["a", "e", "i", "o", "u"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m","n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
alphabets = [vowel, consonant]
print(alphabets)
print(alphabets[0][1])#e