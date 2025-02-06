def filter_words(number, words):
    word_list = words.split()
    filtered_words = [word.lower() for word in word_list if len(word) < number and len(word) % 2 != 0]
    return filtered_words


def main():
    number = int(input("Введите число: "))
    words = input("Введите строку слов через пробел: ")
    result = filter_words(number, words)
    print(": ".join(result))


if __name__ == "__main__":
    main()
