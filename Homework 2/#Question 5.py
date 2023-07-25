#Question 5

number = int(input("What  is your number?:"))
print("Multiplication table of", number)
for count in range(1,13):
    product = number * count
    print(number, "x", count, "=", product)
