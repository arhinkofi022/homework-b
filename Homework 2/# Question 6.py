import random

# Generate a random integer between 1 and 100
magic_number = random.randint(1, 100)

while True:
    user_num = int(input("Enter the number (1-100): "))

    if magic_number < user_num:
        print("Too high")
    elif magic_number > user_num:
        print("Too low")
    else:
        print("Hooray! You guessed it correctly.")
        break
