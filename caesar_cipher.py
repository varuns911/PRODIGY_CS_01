def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                shifted = (ord(char) - ascii_offset + shift) % 26
            else:  # decrypt
                shifted = (ord(char) - ascii_offset - shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit: ").lower()
        
        if mode == 'q':
            print("Goodbye!")
            break
        
        if mode not in ['e', 'd']:
            print("Invalid mode. Please try again.")
            continue
        
        message = input("Enter the message: ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 1 and 25. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 25.")
        
        if mode == 'e':
            result = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()