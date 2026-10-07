def find_max_key(my_dictionary):
    max_bid = 0
    max_bider = ""
    for key in my_dictionary:
        if max_bid < my_dictionary[key]:
            max_bid = my_dictionary[key]
            max_bider = key
    return max_bider

Data_Hub = {}
Has_user = True
while Has_user:
    name = str(input("What is your name? :"))
    value = int(input("What is your bid ? $:"))
    Data_Hub[name] = value
    usr = str(input("Has any biders ? (yes/no):"))
    usr = usr.lower()
    if usr == "no":
        Has_user = False
    else:
        print('\n'*100)

print('\n'*100)
max_key = find_max_key(Data_Hub)
print(f"Winner is :{ max_key}")
print(f"Max bid is : { Data_Hub[max_key] }")