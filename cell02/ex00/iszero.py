num_str = input("Enter a number: ")
try:num = int(num_str)
except ValueError:
    print("That is not a valid integer.")
    exit(1)
if num == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")