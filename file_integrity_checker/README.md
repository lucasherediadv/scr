# What I'am trying to achieve?

Check the integrity of a file that I have downloaded based on the SHA256-Hash provided by the source.

# How to use

Run the script with
```
$ python3 file_integrity_checker.py
```
Enter the directory where the download is stored
```
$ Enter the directory path to check integrity: ~/Downloads/dir_example/
```
The output would be something like this
```
$ File: path/to/file
$ SHA-256 hash: hashexample
```

Then, the hash **MUST** coincide with the provided by the source

