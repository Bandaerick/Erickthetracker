import random
import string

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation  # Corrected 'punctuation'
    password = ''.join(random.choice(alphabet) for _ in range(length))  # Corrected the string join syntax
    return password

password = generate_password()
print(f"Generated password: {password}")