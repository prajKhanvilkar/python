from functools import reduce

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [int(num) for num in user_input.split()]
    print(number_list)
    filtered_numbers = list(filter(lambda x: 70 < x < 90, number_list))
    print("Filtered List:", filtered_numbers)
    mappedList = list(map(lambda z: z + 10, filtered_numbers))
    print("Mapped List:", mappedList)
    reduceValue = reduce(lambda x, y: x * y, mappedList)
    print("Reduced Value:", reduceValue)

if __name__ == "__main__":  
    main()