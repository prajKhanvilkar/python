import threading

def Sum(nums,result):
    sum = 0
    for n in nums:
        sum += n
    result["value"] = sum

def Mul(nums, result):
    mult =1
    for n in nums:
        mult = mult * n
    result["value"] = mult
            
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [int(num) for num in user_input.split()]
    result ={}
    result1 = {}
    t1 = threading.Thread(target=Sum, args=(number_list,result))
    t2 = threading.Thread(target=Mul, args=(number_list,result1))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

    print("Sum is",result["value"])
    print("Multiplication is ",result1["value"])

if __name__ == "__main__":
    main()