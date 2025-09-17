
num_str = input("Enter a number: ")
try:
    num = float(num_str)
except ValueError:
    print("That is not a valid number.")
    exit(1)
if num < 0:
    print("This number is negative.")
elif num > 0:
    print("This number is positive.")
else: 
    print("This number is both positive and negative.")