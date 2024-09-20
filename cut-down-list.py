def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    modified_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List without odd numbers:", modified_list)


if __name__ == "__main__":
    main()
