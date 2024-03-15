from hashlib import sha256
from random import choice
from string import ascii_letters
import secrets

SALT_LENGTH = 32
OUTPUT_FILE = "password.txt"


def generate_salt():
    """
    Generates a random salt string.

    Return:
        str: A random salt
    """
    return "".join(secrets.choice(ascii_letters) for _ in range (SALT_LENGTH))


def hash_password(password, salt):
    """
    Hashes the given password with the provided salt using SHA-256.

    Args:
        password (str): The user's password.
        salt (str): A random salt.

    Return:
        str: Hexadecimal representation of the hashed password.
    """
    return sha256(password.encode() + salt.encode()).hexdigest()


def main():
    """
    Interact with the user and store salt and hashed password in a file
    """
    password = input("Enter password: ")
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    with open(OUTPUT_FILE, "w") as output:
        output.write(f"Salt: {salt}\n")
        output.write(f"Hashed Password: {hashed_password}\n")


if __name__ == "__main__":
    main()

