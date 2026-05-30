def frequencyOfNumber(data, num):
    count = 0
    for item in data:
        if item == num:
            count += 1
    return count
   

def main():
    number1 = int(input("Enter a number for List: "))
    data = list()
    for i in range(number1):
        num = int(input("Enter a number: "))
        data.append(num)
    frequency = int(input("Enter a number to ge the frequency: "))
    result = frequencyOfNumber(data,frequency)
    print("Frequency in list is:", result)

if __name__ == "__main__":
    main()