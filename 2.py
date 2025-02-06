def parse_numbers(input_string):
    return set(map(int, input_string.split(", ")))


def find_common_numbers(set1, set2, set3):
    return set1 & set2 & set3


def main():
    input1 = input("Введите первую строку чисел: ")
    input2 = input("Введите вторую строку чисел: ")
    input3 = input("Введите третью строку чисел: ")
    set1 = parse_numbers(input1)
    set2 = parse_numbers(input2)
    set3 = parse_numbers(input3)
    common_numbers = find_common_numbers(set1, set2, set3)
    print(" ".join(map(str, common_numbers)))
    if common_numbers:
        print(max(common_numbers))
    else:
        print("Нет общих чисел")


if __name__ == "__main__":
    main()