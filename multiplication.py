#Write a program that takes an input number from the user and prints the multiplication table for that number using a while loop.
user = int(input("Enter the number for multiplication: "))
counter = 1

while counter <= 10:
    result = user * counter
    print(f"{user} * {counter} = {result}")
    counter += 1
print("You have generated the multiplication of " + str(user) + " number")

