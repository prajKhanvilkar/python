from functools import reduce
import math

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [int(num) for num in user_input.split()]
    print(number_list)
    filtered_numbers = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)), number_list))
    print("Filtered List:", filtered_numbers)
    mappedList = list(map(lambda z: z * 2, filtered_numbers))
    print("Mapped List:", mappedList)
    reduceValue = reduce(lambda x, y: x if(x>y) else y, mappedList)
    print("Reduced Value:", reduceValue)

if __name__ == "__main__":  
    main()