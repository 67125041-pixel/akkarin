import math

def main():
    num_str = input("Give me a number: ")
    try:
        num = float(num_str)
       
        rounded = math.ceil(num)
        print(rounded)
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()