# File integrity checker

Check the integrity of a file based on their provided hash. By comparing the calculated hash with the expected hash, you can ensure that files have not been tampered with.

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

## Verify the Hash:

Compare the calculated hash with the expected hash provided by the file source. The hash exposed by this program **MUST** match the one provided by the file source.

