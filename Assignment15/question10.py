def main():
    data = [2,3,4,5,6,7,8,9,10]
    res = list(filter(lambda No : (No%2==0), data))
    print(len(res))

if __name__ =="__main__":
    main()