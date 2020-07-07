import sys


def main():
    n = len(sys.argv)

    if n != 2:
        print("Usage: Please pass an integer key.")

    key = sys.argv[1]
    try:
        key = int(sys.argv[1])
        print(f'ciphertext: {caesar(int(key))}')
    except:
        print("Usage: Please pass an integer key.")


def caesar(key):
    text = input("plaintext:  ")
    output = ""
    for char in text:
        if char.isupper():
            output += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            output += chr((ord(char) + key - 97) % 26 + 97)
        else:
            output += char
    return output


main()
