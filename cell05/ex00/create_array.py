
def main():
    user_input = input("ป้อนตัวเลข (คั่นด้วย space): ")
    numbers = [int(x) for x in user_input.split()]
    print(numbers)
if __name__ == "__main__":
    main()