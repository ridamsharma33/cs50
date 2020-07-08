import sys


def main():
    n = len(sys.argv)

    if n != 2:
        print("Usage: Please provide a key.")
        return 1

    key = sys.argv[1]

    if len(key) != 26 or not key.isalpha():
        print("Usage: Key must contain 26 charaters.")
        return 1
    else:
        print(f'Ciphertext: {substitution(key)}')
        return 0


def substitution(key):
    text = input("pliantext:  ")
    output = ""

    for char in text:
        if char.isupper():
            idx = ord(char) - 65
            output += key[idx].upper()
        elif char.islower():
            idx = ord(char) - 97
            output += key[idx].lower()
        else:
            output += char

    return output


main()
