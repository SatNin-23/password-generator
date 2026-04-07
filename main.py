import random
import string

min_length = 4
max_length = 32

def generate_password(length=12):
    if length < min_length or length > max_length:
        raise ValueError(f"Password must be between {min_length} and {max_length} characters")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)