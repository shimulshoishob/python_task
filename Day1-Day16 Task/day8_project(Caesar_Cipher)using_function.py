
alphabets = letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
def encrypt(original_text, shift_amount):
    text = ""
    for char in original_text:
        #index function return integer number and it's argument obj
        if char in alphabets:
            shift_alphabet = alphabets.index(char) + shift_amount
            text += alphabets[shift_alphabet]
        else:
            text += char
    return text

def decrypt(original_text, shift_amount):
    text = ""
    for char in original_text:
        if char in alphabets:
            shift_alphabet = alphabets.index(char) - shift_amount
            text += alphabets[shift_alphabet]
        else:
            text += char
    return text


print("Welcome to the Caesar Cipher Program")
print("_____________________________________")
print("1. encrypt a string")
print("2. decrypt a string")
print("_____________________________________")
usr = int(input("Enter your choice: "))

massage = str(input("Enter your message: "))
shift = int(input("Enter shift amount: "))
print(f"Your message is: {massage}\n")

if usr == 1:
    encrypted = encrypt(massage, shift)
    print(f"Your encrypted message is: {encrypted}")
elif usr == 2:
    decrypted = decrypt(massage, shift)
    print(f"Your decrypted message is: {decrypted}")

print("\nshimul_Kumar_Shoishob\n")