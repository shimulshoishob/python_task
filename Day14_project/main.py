import random
import game_art
import game_data

def description_print(person):
    storage = []
    for celebrity in game_data.celebrities[person].values():
        storage.append(celebrity)
    print(f"    name :{storage[0]}")
    print(f"    profession :{storage[1]}")
    print(f"    from :{storage[3]}")
    return storage[2]

point = 0
run_game = True

print(game_art.higher_lower)

while run_game:
    print(game_art.line)
    print("current point:", point)
    print(game_art.line)
    length_of_celebrity = len(game_data.celebrities)-1
    # print(length_of_celebrity)

    person_1 = -1
    person_2 = -1
    while person_1 == person_2:
        person_1 = random.randint(0,length_of_celebrity)
        person_2 = random.randint(0,length_of_celebrity)

    # print(person_1, person_2)
    print("Person A:")
    follwer_1 = description_print(person_1)
    print(game_art.line)
    print("Person B:")
    follwer_2 = description_print(person_2)

    print(game_art.line)

    usr = str(input("which one has more followers A or B :"))


    if usr == "A" and follwer_1 > follwer_2:
        point = point+1
        print("\n"*25)
    elif usr == "B" and follwer_1 < follwer_2:
        point = point+1
        print("\n"*25)
    else:
        run_game = False
        print("\n" * 25)

    # print(follwer_1)
    # print(follwer_2)

print("Game Over!")
print(game_art.line)
print(f"Your final score is: {point}")
print(game_art.line)