#dictionary
my_dictionary = {
    # key : value
    "Shimul" : "East West University",
    "Arafat" : "Bangladesh University of Engineering and Technology",
    157 : "my id : 2023-3-60-157"
}
#print entire dictionary
print(my_dictionary)

#print specific key value
print(my_dictionary["Shimul"])
print(my_dictionary["Arafat"])
print(my_dictionary[157])

#make wipe a dictionary and make an empty dictionary
my_dictionary ={}
print(my_dictionary)

# add new element in dictionary and also valid for editing an existing key value
my_dictionary["CSE"] = "Computer Science Engineering"
print(my_dictionary)
print(my_dictionary["CSE"])
my_dictionary["CSE"] = "Computer Science and Engineering"
print(my_dictionary)
print(my_dictionary["CSE"])
my_dictionary["EEE"] = "Electrical and Electronic Engineering"
my_dictionary["ME"] = "Mechanical Engineering"
my_dictionary["CE"] = "Civil Engineering"
print(my_dictionary)
print('\n')
#looping dictionary
for key in my_dictionary:
    print(key) #this can print only keys
    print(my_dictionary[key]) # this can print values

# this looping technic return only values instate of keys
for value in my_dictionary.values():
    print(value)
