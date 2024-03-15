from hashlib import sha256
from random import choice
from string import ascii_letters
import secrets

SALT_LENGTH = 32
OUTPUT_FILE = "password.txt"


def generate_salt():
    return "".join(secrets.choice(ascii_letters) for _ in range (SALT_LENGTH))


def hash_password(password, salt):
    return sha256(password.encode() + salt.encode()).hexdigest()


def main():
    password = input("Enter password: ")
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    with open(OUTPUT_FILE, "w") as output:
        output.write(f"Salt: {salt}\n")
        output.write(f"Hashed Password: {hashed_password}\n")


if __name__ == "__main__":
    main()

