import os
import hashlib


def calculate_sha256(file_path):
    """Calculates the SHA-256 hash of a file specified by it file path"""
    # Initialize SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # The file is opened in binary read mode ("rb")
    with open(file_path, "rb") as f:
        while True:
            # Read data in chunks of 65536 bytes (64KB) at a time
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)
            # Returns hexadecimal representation of the hash
        return sha256_hash.hexdigest()


def check_integrity(directory_path):
    """Checks the integrity of files within a specified directory"""
    # Verifies if the directory exists and is indeed a directory
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"directory '{directory_path}' does not exists.")
        return

    # Recursively walks through the directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            print(f"File: {file_path}\nSHA-256 hash: {calculated_hash}")


if __name__ == "__main__":
    """Main execution"""
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)

