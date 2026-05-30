def main():
    list_of_strings = ["apple", "banana", "kiwi", "orange", "grapefruit", "fig"]
    filtered_list = list(filter(lambda x: len(x) > 5, list_of_strings))

    print(f"Filtered list (length > 5): {filtered_list}")

if __name__ == "__main__":
    main()