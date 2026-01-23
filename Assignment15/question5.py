from functools import reduce

def main():
    data = [2,3,4,5,6,7,8,9,10]
    res = reduce(lambda x, y: x if (x > y) else y, data)
    print(res)

if __name__ =="__main__":
    main()