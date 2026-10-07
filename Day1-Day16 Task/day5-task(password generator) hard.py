import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
symbol = ['!','@' ,'#','^','-','_', '$', '%', '&', '(', ')', '*', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to Password Generator")
usr_letter = int(input("How many letters would you like in your password?"))
usr_symbol = int(input("How many symbols would you like in your password?"))
usr_number = int(input("How many numbers would you like in your password?"))

password_list = []
for i in range(usr_letter):
    password_list += random.choice(letter)
for i in range(usr_symbol):
    password_list += random.choice(symbol)
for i in range(usr_number):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = "".join(password_list)
# for i in password_list:
#     password += i
print(password)
