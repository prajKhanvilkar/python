def count_digits(number):
    count = len(number)
    return count

def main():
    num = input("Enter a number: ")
    res = count_digits(num)
    print("Count of digits:", res)

if __name__ == "__main__":
    main()