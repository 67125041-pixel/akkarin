def main():
    # รับเลขจากผู้ใช้ (คั่นด้วย space)
    user_input = input("ป้อนตัวเลข (คั่นด้วย space): ")

    # แปลงเป็น list ของ int
    numbers = [int(x) for x in user_input.split()]

    # แสดง array
    print(numbers)

if __name__ == "__main__":
    main()