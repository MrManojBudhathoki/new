#Write a program that uses a while loop to count down from a given number to 1. Ask the user to input the starting number.
starting_number = int(input("Enter the number you want to give as a target: "))
final_number = 1
while starting_number >= final_number:
    print(starting_number)
    starting_number -= 1
print("You have reached the target!")
