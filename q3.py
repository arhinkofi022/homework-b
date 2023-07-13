# Assign initial values
P = 10000
n = 12
r = 0.08

# Ask user for the number of years
t = int(input("Enter the number of years: "))

# Calculate the final amount using the compound interest formula
final_amount = P * (1 + r/n) ** (n * t)

# Print the final amount
print("The final amount after", t, "years is:", final_amount)
