from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print("Generated key: ", key.decode())

message = "Hello World. This is a secret message."
encrypted_message = cipher.encrypt(message.encode())
print("Encripted message: ", encrypted_message)

decrypted_message = cipher.decrypt(encrypted_message).decode()
print("Decrypted message is: ", decrypted_message)

