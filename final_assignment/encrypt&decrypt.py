'''Create a Python script that encrypts and decrypts text files using a simple substitution cipher. 
Implement functions for encryption and decryption using a basic substitution cipher algorithm (e.g., shifting each letter by a fixed number of positions in the alphabet).
Prompt users to enter a filename and choose whether to encrypt or decrypt the file.
Ensure the script handles cases where the file does not exist or cannot be opened for reading/writing.
'''

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def process_file(filename, mode, shift):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        if mode == "e":
            processed_text = encrypt(content, shift)
        else:
            processed_text = decrypt(content, shift)

        output_file = open(filename, "w")
        output_file.write(processed_text)
        output_file.close()

        print("File processed successfully.")

    except FileNotFoundError:
        print("Error: File does not exist.")
    except IOError:
        print("Error: File cannot be opened or written.")


# Main program
filename = input("Enter the filename: ")
mode = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
shift = int(input("Enter shift value (e.g., 3): "))

if mode in ["e", "d"]:
    process_file(filename, mode, shift)
else:
    print("Invalid choice! Please enter 'e' or 'd'.")
