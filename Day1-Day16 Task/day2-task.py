print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15 ?"))
person = int(input("How many people split the bill? "))
percentage = percentage
per = percentage/100
bill = (total_bill + total_bill*per) / person
bill = round(bill, 2)
print("Each person should pay: $" + str(bill))

