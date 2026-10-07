import random

def card_value(card):
    if card == "K" or card == "Q" or card == "J":
        card = "10"
        return int(card)
    elif card =="A":
        card = "1"
        return int(card)
    else:
        return int(card)

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

usr_card1 = random.choice(cards)
usr_card2 = random.choice(cards)
print("Your cards: ",usr_card1,usr_card2)

usr_card1_value = card_value(usr_card1)
usr_card2_value = card_value(usr_card2)

Ace = False
if usr_card1_value == 1:
    Ace = True

if usr_card2_value == 1:
    Ace = True

sum_of_cards = usr_card1_value + usr_card2_value
if sum_of_cards ==2:
    sum_of_cards = 12
elif sum_of_cards <=11 and Ace :
    sum_of_cards += 10
print("Sum of your cards: ",sum_of_cards,"\n")

diller_card1 = random.choice(cards)
diller_card2 = random.choice(cards)
print("Your cards: ",diller_card1,"???")
DAce = False
if usr_card1_value == 1:
    DAce = True

if usr_card2_value == 1:
    DAce = True

input("Press enter to add another card...")
usr_card3 = random.choice(cards)
print("Your cards: ",usr_card1,usr_card2,usr_card3)
usr_card3_value = card_value(usr_card3)
sum_of_cards += usr_card3_value
if sum_of_cards <10:
    sum_of_cards += 10
print("Sum of your cards: ",sum_of_cards,"\n")
if sum_of_cards >21:
    print("You Lose!")
    exit()


print("diller_cards: ",diller_card1,diller_card2)
sum_of_diller_cards = card_value(diller_card1) + card_value(diller_card2)
if sum_of_diller_cards ==2:
    sum_of_diller_cards += 10
elif sum_of_diller_cards <=11 and DAce :
    sum_of_diller_cards += 10
print("Sum of diller cards: ",sum_of_diller_cards,"\n")

input("Press enter to continue...")

if sum_of_diller_cards <17 :
    diller_card3 = random.choice(cards)
    print("now diller cards: ",diller_card1, diller_card2, diller_card3)
    diller_card3_value = card_value(diller_card3)
    sum_of_diller_cards += diller_card3_value
    if sum_of_diller_cards <11:
        sum_of_diller_cards += 10
    print("Sum of diller cards: ",sum_of_diller_cards,"\n")
    if sum_of_diller_cards >21:
        print("You Win!")
        exit()

if sum_of_diller_cards == sum_of_cards:
    print("Draw!")
if sum_of_diller_cards >sum_of_cards:
    print("You lose!")
if sum_of_diller_cards < sum_of_cards:
   print("Congrats! You win!")

