import random

dash = """-------------------------------------------------------------"""

cards ={
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
}
keys = list(cards.keys())
usr_card1 = random.choice(keys)
usr_card2 = random.choice(keys)
usr_card3 = random.choice(keys)

ace = False
if usr_card1 == "A" or usr_card2 == "A":
    ace = True


print("Your cards : ", usr_card1, usr_card2)
usr_sum = cards[usr_card1] + cards[usr_card2]

if usr_sum == 2:
    usr_sum +=10
elif usr_sum <11 and ace:
    usr_sum +=10

print("Your sum is: ", usr_sum)
print(dash)
D_card1 = random.choice(keys)
D_card2 = random.choice(keys)
D_card3 = random.choice(keys)

Dace = False
if usr_card1 == "A" or usr_card2 == "A":
    Dace = True
print("Your Diller cards: ", D_card1, "???")
print(dash)
input("Press enter to continue...")

D_sum = cards[D_card1] + cards[D_card2]

if D_sum == 2:
    D_sum +=10
elif D_sum <11 and Dace:
    D_sum +=10

print("Your cards:", usr_card1, usr_card2, usr_card3)
usr_sum += cards[usr_card3]

if usr_card3 == "A" and usr_sum <11:
    usr_sum += 10

print("Your sum is: ", usr_sum)
if usr_sum > 21:
    print("You Lose!")
    exit()

print("Diller cards: ", D_card1, D_card2)
print("Sum: ", D_sum)
print(dash)
if D_sum < 17 :
    print("Diller cards: ", D_card1, D_card2, D_card3)
    D_sum += cards[D_card3]
    if D_card3 == "A" and D_sum <11:
        D_sum += 10
    print("D_sum is: ", D_sum)

print(dash)
if D_sum > 21:
    print("You Win!")
    exit()
if usr_sum > D_sum:
    print("You Win!")
elif usr_sum < D_sum:
    print("You Lose!")
elif usr_sum == D_sum:
    print("Draw!!")



