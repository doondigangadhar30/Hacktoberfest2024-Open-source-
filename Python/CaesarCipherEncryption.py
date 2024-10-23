def caesar_cipher(text, shift):
    result = ""
    for i in text:
        if i.isalpha():
            shift_base = 65 if i.isupper() else 97
            result += chr((ord(i) - shift_base + shift) % 26 + shift_base)
        else:
            result += i
    return result

choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()
text = input("Enter text: ")
shift = int(input("Enter shift value: ")) if choice == 'E' else -int(input("Enter shift value: "))
print(caesar_cipher(text, shift))
