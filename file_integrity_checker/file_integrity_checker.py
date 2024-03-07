import os
import hashlib
from pathlib import Path

CHUNK_SIZE = 65536
HASH_ALGORITHM = hashlib.sha256


def validate_directory(directory_path):
    """
    Validates the existence of a directory.

    Args:
        directory_path (str): Path to the directory.

    Return:
        bool: True if the directory exists, False otherwise.
    """
    return os.path.exists(directory_path) and os.path.isdir(directory_path)


def calculate_hash(file_path):
    """
    Calculates the hash of a file using the specified algorithm.

    Args:
        file_path (str): Path to file.

    Returns:
        str: Hexadecimal representation of the hash.
    """
    hash_obj = HASH_ALGORITHM()
    with open(file_path, "rb") as f: # Binary read mode "rb"
        while True:
            data = f.read(CHUNK_SIZE) # Read data in chunks of 65536 bytes (64KB)
            if not data:
                break
            hash_obj.update(data)
        return hash_obj.hexdigest()


def check_integrity(directory_path):
    """
    Checks the integrity of files within a specified directory.

    Args:
        directory_path (str): Path to directory.
    """
    # Expand the user's home directory
    expanded_directory = Path(directory_path).expanduser()

    if not validate_directory(expanded_directory):
        print(f"Directory '{expanded_directory}' does not exists.")
        return

    for root, dirs, files in os.walk(expanded_directory):
        for file_name in files:
            file_path = Path(root) / file_name
            calculated_hash = calculate_hash(file_path)
            print(f"\nFile: {file_path}\nHash: {calculated_hash}\n")


if __name__ == "__main__":
    """Main execution"""
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)

