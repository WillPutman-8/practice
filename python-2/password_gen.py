import random

def password_function():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    charecters = ["!","@","#","$","%","^","&","*","(",")","[","]","{","}","+","_","-","=","<",">","?",",",".",
                  "/",":",";"]

    letters_num = int(input("How many letters would you like in your password?: "))
    numbers_num = int(input("How many numbers do you want in your password?: "))
    charecters_num = int(input("How many special charecters do you want in your password?: "))

    password_list = []
    password = ""

    while letters_num > 0:
        password_list += random.choice(letters)
        letters_num -= 1

    while numbers_num > 0:
        password_list += random.choice(numbers)
        numbers_num -= 1

    while charecters_num > 0:
        password_list += random.choice(charecters)
        charecters_num -= 1

    random.shuffle(password_list)

    for letters in password_list:
        password += letters

    print(password)

    password_function.variable = password
def acount_logins():
    account = []
    website = input("What website is this for? ")
    account.append(website)
    user_name = input("What is the account name/E-mail? ")
    account.append(user_name)
    password_function()
    pass_w = password_function.variable
    account.append(pass_w)
    acount_logins.variable = account

def new_file():
    x = True
    while x == True:

        acount_logins()
        account_list = acount_logins.variable
        account_tracker = ""
        print(account_list)
        bruh = 0
        for items in account_list:
            account_tracker = account_list[bruh]
            print(account_tracker)
            bruh += 1
            with open("/Users/tedputman/Desktop/passwords/Passwords.txt", "a+") as txt:
                txt.seek(0)
                words = txt.read(100)
                if len(words) > 0:
                    txt.write("\n")
                txt.write(account_tracker)
        with open("/Users/tedputman/Desktop/passwords/Passwords.txt", "a+") as txt:
            txt.seek(0)
            words = txt.read(100)
            if len(words) > 0:
                txt.write("\n.........................................................")
                txt.read()




        answer = input("Is that all of your accounts for me to manage? Y/N: ").lower()
        if answer == "yes" or answer == "y":
            x = False
        elif answer == "no" or answer == "n":
            x = True
        else:
            y = True
            while y == True:
                print("Invalid input please try again:")
                answer = input("Is that all of your accounts for me to manage? Y/N: ").lower()
                if answer == "yes" or answer == "y":
                    x = False
                    y = False
                elif answer == "no" or answer == "n":
                    x = True
                    y = False
                else:
                    y = True
#def existing_file():
 #   with open("/Users/tedputman/Desktop/passwords/Passwords.txt", "a+") as txt:
 #       print(txt.read())





print("Welcome to password manager!")
start = input("Have you used this code before? Y/N: ").lower()
if start == "yes" or start == "y":
    existing_file()
else:
    new_file()