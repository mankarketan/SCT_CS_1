def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The input message.
        shift (int): The number of positions to shift.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""

    if mode == 'decrypt':
        shift = -shift  # To decrypt, shift in the opposite direction

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            # Handle wrapping around the alphabet
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            # Handle wrapping around the alphabet
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            # Keep non-alphabetic characters unchanged (e.g., spaces, numbers, punctuation)
            result += char
    return result

def main():
    print("--- Caesar Cipher Program ---")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            try:
                shift_value = int(input("Enter the shift value (an integer): "))
                encrypted_message = caesar_cipher(message, shift_value, 'encrypt')
                print(f"Encrypted message: {encrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            try:
                shift_value = int(input("Enter the shift value (the same integer used for encryption): "))
                decrypted_message = caesar_cipher(message, shift_value, 'decrypt')
                print(f"Decrypted message: {decrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '3':
            print("Exiting Caesar Cipher Program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()