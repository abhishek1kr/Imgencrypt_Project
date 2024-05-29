from cryptography.fernet import Fernet
import os
import base64

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_image(image_path):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    with open(image_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(image_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_image(image_path):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    with open(image_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(image_path, "wb") as file:
        file.write(decrypted_data)

def main():
    generate_key()
    while True:
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        choice = input("Enter your choice: ")
        if choice == "1":
            image_path = input("Enter the path to the image file: ")
            encrypt_image(image_path)
            print("Image encrypted successfully!")
        elif choice == "2":
            image_path = input("Enter the path to the encrypted image file: ")
            decrypt_image(image_path)
            print("Image decrypted successfully!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()