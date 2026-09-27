from cryptography.fernet import Fernet
from pathlib import Path

CURRENT_FOLDER = Path(__file__).resolve().parent

#generate key to encrypt file
def generate_key(file_path = 'encryption_key.key'):
    #create a key
    key = Fernet.generate_key()
    file_path = CURRENT_FOLDER / file_path
    #wb - will open a file in binary format
    with open(file_path, "wb") as key_file:
        key_file.write(key)

    print(f"Encryption key saved to {file_path}")

#write key to file "encryption key"
def load_key(file_path = "encryption_key.key"):
    file_path = CURRENT_FOLDER / file_path
    #rb - will read key from the file in binary
    with open(file_path, "rb") as key_file:
        key = key_file.read()
    return key

#encrypt file - save content in binary 
def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)

    input_file = CURRENT_FOLDER / input_file
    output_file = CURRENT_FOLDER / output_file

    with open(input_file, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(output_file, "wb") as file:
        file.write(encrypted)

    print(f"File encrypted and saved to {output_file}.")

#decrypt file using key
def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)

    input_file = CURRENT_FOLDER / input_file
    output_file = CURRENT_FOLDER / output_file

    with open(input_file, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(output_file, "wb") as file:
        file.write(decrypted)

    print(f"File {input_file} decrypted and saved to {output_file}")

def main():
    print("Welcome to the Encryption/Decryption tool!")

    while True:
        print("1. Generate an encryption key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit the program")

        option = input("What option would you like to go with?")
        if option == "1":
            file_path = input("Enter the file path to save the key (default: 'encryption_key.key'): ") or "encryption_key.key" 
            generate_key(file_path)
        elif option == "2":
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input("Enter the path of the encryption key, otherwise the default key will be used.") or "encryption_key.key"

            try:
                key = load_key(key_path)
                encrypt_file(input_file, output_file, key)
            except Exception as e:
                print(f"Error during encryption: {e}")

        elif option == "3":
            input_file = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input("Enter the path of the encryption key, otherwise the default key will be used.") or "encryption_key.key"

            try:
                key = load_key(key_path)
                decrypt_file(input_file, output_file, key)
            except Exception as e:
                print(f"Error during decryption: {e}")

        elif option == "4":
            print("Exiting the program")
            break

        else:
            print("Choose a valid option")

main()