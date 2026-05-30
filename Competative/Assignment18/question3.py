def mininList(data):
    max_value = data[0]
    for num in data:
        if num < max_value:
            max_value = num
    return max_value
   

def main():
    number1 = int(input("Enter a number for List: "))
    data = list()
    for i in range(number1):
        num = int(input("Enter a number: "))
        data.append(num)
    result = mininList(data)
    print("Min number in List:", result)

if __name__ == "__main__":
    main()
