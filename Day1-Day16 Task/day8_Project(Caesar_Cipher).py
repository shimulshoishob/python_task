
print("1. Encrypt")
print("2. Decrypt")
user = int(input("Enter your choice: "))
if user == 1:
    massage = input("Enter your message: ")
    massage = massage.upper()
    print(massage)
    shift = int(input("Enter your shift: "))
    encry =""
    for char in massage:
        tem = ord(char)+shift
        if tem > ord('Z'):
            tem = (tem-ord('Z'))+ord('A')
        encry += chr(tem)
    print(encry)
elif user == 2:
    massage = input("Enter your Encrypted message: ")
    massage = massage.upper()
    print(massage)
    shift = int(input("Enter your shift: "))
    decry = ""
    for char in massage:
        tem = ord(char) - shift
        if tem > ord('Z'):
            tem = (tem - ord('A')) + ord('Z')
        decry += chr(tem)
    print(decry)
else:
    print("Invalid choice")