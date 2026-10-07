import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
symbols = ['!','@' ,'#','^','-','_', '$', '%', '&', '(', ')', '*', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter_num = random.randint(4,7)
symbol_num = random.randint(4,7)
numbers_num = random.randint(4,7)
password = []
for i in range(letter_num):
    password += random.choice(letters)
for i in range(symbol_num):
    password += random.choice(symbols)
for i in range(numbers_num):
    password += random.choice(numbers)

random.shuffle(password)
new_password ="".join(password)
print(new_password)