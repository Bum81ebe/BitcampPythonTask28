#twitter


def main():
    shorten()


def shorten(text):
    output = ""
    for char in text:
        if char.upper() not in "AEIOU":
            output += char

    return output


if __name__ == "__main__":
    main()