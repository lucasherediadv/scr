# Trackability Reduction

- MAC address spoofing and randomization.
- Remove the static hostname to prevent hostname broadcast.

## Motivation

Ensure packages updates do not overwrite the configuration, and if that happens, just run this script.

## How to use?

Make the script executable
```
$ chmod +x trackability_reduction
```
Run the script
```
$ sudo ./trackability_reduction
```

## Sources

- [NetworkManager Trackability Reduction](https://privsec.dev/posts/linux/networkmanager-trackability-reduction/)
- [Randomize your MAC address using NetworkManager](https://fedoramagazine.org/randomize-mac-address-nm/)

