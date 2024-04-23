"""Check the integrity of a file based on their provided hash.
By comparing the calculated hash with a user-provided hash, you can
ensure that files have not been tampered with."""

import os
import hashlib
from pathlib import Path


def validate_file(file_path):
    """Validates the existence of a file."""
    return os.path.exists(file_path) and os.path.isfile(file_path)


def calculate_hash(file_path):
    """Calculates the hash of a file using the specified algorithm."""
    hash_obj = hashlib.sha256()
    chunk_size = 65536

    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                hash_obj.update(data)
            return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        return None


def check_integrity(file_path, user_provided_hash):
    """Checks the integrity of a file by comparing its calculated hash
    with a user provided hash."""
    expanded_file_path = Path(file_path).expanduser()

    if not validate_file(expanded_file_path):
        print(f"File '{expanded_file_path}' does not exists.")
        return False

    calculated_hash = calculate_hash(expanded_file_path)
    if calculated_hash == user_provided_hash:
        print(
            "\nIntegrity check successful! The hashes match:\n"
            f"File: {expanded_file_path}\n"
            f"Provided hash: {user_provided_hash}\n"
            f"Calculated hash: {calculated_hash}\n"
        )
    else:
        print("WARNING: The calculated hash does not match the provided hash.")
    return None


def main():
    """Main execution"""
    file_to_check = input("Enter the file path to check integrity: ")
    user_hash = input("Enter the expected hash: ")
    check_integrity(file_to_check, user_hash)


if __name__ == "__main__":
    main()
