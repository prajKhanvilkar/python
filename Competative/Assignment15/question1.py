Square = lambda No : No * No
def main():
    data = [2,3,4,5,6,7,8,]
    res = list(map(Square, data))
    print(res)

if __name__ =="__main__":
    main()