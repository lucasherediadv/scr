# File integrity checker

Check the integrity of a file based on the hash provided by the file source.

# How to use

Run the script with:
```
$ python3 file_integrity_checker.py
```
Enter the directory where the file is located:
```
$ Enter the directory path to check integrity: ~/dir_example
```
The output would be something like this:
```
$ File: path/to/file
$ Hash: hashexample
```

The hash that this program exposes **MUST** match the one provided by source of the file.

