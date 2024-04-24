"""
Verify the integrity of a file by comparing its hash with a user
provided hash. The program calculates the SHA-256 hash of the
specified file and check if it matches the expected.

Usage:
    - Run the script with python.
    - Follow the prompts to enter the file path and the expected hash.
    - The program will display wether the hashes match or not.
"""

import os
import hashlib
from pathlib import Path


def validate_file(file_path):
    """
    Validates the existence of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file exists and is a regular file, False otherwise.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)


def calculate_hash(file_path):
    """
    Calculates the hash of a file using the specified algorithm.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[str]: The hexadeciaml representation of the calculated
        hash, or None if the file does not exists.
    """
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


def check_integrity(file_path, user_hash):
    """
    Checks the integrity of a file by comparing its calculated hash
    with a user provided hash.

    Args:
        file_path (str): Path to the file.
        user_hash (str): Expected hash provided by the user.

    Returns:
        None
    """
    # Expands the tile character (~) in "file_path" to the user's
    # home directory.
    expanded_path = Path(file_path).expanduser()

    if not validate_file(expanded_path):
        print(f"File '{expanded_path}' does not exists.")
        return False

    calculated_hash = calculate_hash(expanded_path)
    if calculated_hash == user_hash:
        print(
            "\nIntegrity check successful! The hashes match:\n"
            f"\nFile: {expanded_path}\n"
            f"Provided hash: {user_hash}\n"
            f"Calculated hash: {calculated_hash}\n"
        )
    else:
        print("\nWARNING: The calculated hash does not match the provided hash.\n")
    return None


def main():
    """Main execution."""
    file_path = input("\nEnter the file path to check integrity: ")
    user_hash = input("Enter the expected hash: ")
    check_integrity(file_path, user_hash)


if __name__ == "__main__":
    main()
