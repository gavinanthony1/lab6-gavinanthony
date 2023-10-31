
def encode(password):
    new_password = ""
    for x in range(len(password)):
        y = int(password[x]) + 3
        if y >= 10:
            y -= 10
        new_password += str(y)
    return new_password



def decode(pswd):
    output = ''
    for i in range(len(pswd)):
        num = int(pswd[i]) - 3
        output += str(num) if num >= 0 else str(10 + num)
    return output


def main():
    menu = "Menu\n------------\n1. Encode\n2. Decode\n3. Quit"
    print(menu)
    menu_choice = 0
    while menu_choice != 3:
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
        if menu_choice == 2:
            print("The encoded password is", encode(password), "and the original password is", decode(encode(password)))


main()