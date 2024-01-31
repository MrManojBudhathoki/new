#Create a program that asks the user to guess a password. Use a while loop to repeatedly prompt the user until the correct password is entered.
correct_password = "password"
while True:
    users_guess = input("Guess the password: ").lower()
    if users_guess == correct_password:
        print("You guessed the password successfully!")
        break
    else:
        print("Try again!")
