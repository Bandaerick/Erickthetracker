import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = key % 26
    shift = 26 - shift  # Calculate decryption shift
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    message = encrypted_message.translate(cipher)
    return message

message = "Subscribe to W J Pearce"
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")

