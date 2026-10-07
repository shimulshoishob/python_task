
# python don't have block scope[if, while, for]

if 3 > 2:
    my_if_block_variable = 10

print("block var :",my_if_block_variable)




# function scope

my_variable = 2 # var-1
def my_function():
     my_variable = 3 # var-2
     print("inside function:",my_variable)

#var-1 and var-2 both are different

my_function()
print("outside function",my_variable)




# modify global var [avoid this]
# use return in function
shimul =157
def idf():
    global shimul
    shimul += 1

print("before call function",shimul)
idf()
print("after call function",shimul)


#use return statement
shoishob = 157
def idf_inc(num):
    num +=1
    return num
print("before call increment function",shoishob)
shoishob = idf_inc(shoishob)
print("after call increment function",shoishob)