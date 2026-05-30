import threading

def isMax(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    print(f"Maximum value is: {max_val}")         

def isMin(nums):
    min_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
    print(f"Maximum value is: {min_val}")  
            
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [int(num) for num in user_input.split()]
    t1 = threading.Thread(target=isMax, args=(number_list,))
    t2 = threading.Thread(target=isMin, args=(number_list,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()