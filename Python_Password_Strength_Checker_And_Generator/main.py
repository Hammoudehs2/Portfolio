import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen(i, p, j):
    gen_passwords = []
    password = ""
    for letter in range(i):
        gen_passwords.append(random.choice(letters))
    for number in range(p):
        gen_passwords.append(random.choice(numbers))
    for symbol in range(j):
        gen_passwords.append(random.choice(symbols))

    random.shuffle(gen_passwords)
    for i in gen_passwords:
        password += i
    return password
def password_check(password):
    gap_so_it_returns_something = ""
    check = 0
    has_symbol = 0
    has_number = 0
    has_letter = 0
    if len(password) >= 12:
        check += 4
        print("Your password length is great! +4")
    else:
        check += 1
        print("Your password length is short, needs improvement. +1")
    for i in password:
        if i in symbols:
            has_symbol = 1
        elif i in numbers:
            has_number = 1
        elif i in letters:
            has_letter = 1
    if has_symbol == 1:
        check += 2
        print("Your password contains symbols! +2")
    else:
        print("Your password needs a symbol.")
    if has_number == 1:
        check += 2
        print("Your password contains numbers! +2")
    else:
        print("Your password needs a number.")
    if has_letter == 1:
        check += 2
        print("Your password contains letters! +2")
    else:
        print("Your password needs a letter.")

    print("Your score is:", check)
    if check == 10:
        print("Your password is great!")
    elif check >= 8:
        print("Your password is good!")
    elif check >= 6:
        print("Your password is okay but needs to change!")
    else:
        print("Your password needs to change ASAP.")
    return gap_so_it_returns_something


print("Welcome to the your Password Helper!")


if __name__ == "__main__":
    users_choice = input("Would you like to check your password or generate a password? C for check, G to Generate: \n").lower()
while True:
    if users_choice != 'c' and users_choice != 'g':
        print("Invalid output, please re-enter your choice, either C for check, G for generate!")
        users_choice = input()
    if users_choice == 'c' or users_choice == 'g':
        break

if users_choice == "g":
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    print(f"Your new password is: {password_gen(nr_letters, nr_symbols, nr_numbers)}")
else:
    password = input("Please enter your password: \n")
    print(password_check(password))




