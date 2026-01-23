def main():
    listofData = [10,20,30,33,21,22,3,15,21,60]
    filtered_list = list(filter(lambda x: (x%3==0 and x%5==0), listofData))

    print(f"Filtered list (length > 5): {filtered_list}")

if __name__ == "__main__":
    main()