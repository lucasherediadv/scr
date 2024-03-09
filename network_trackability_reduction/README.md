# Network Trackability Reduction

- MAC address spoofing and randomization.
- Removes the static hostname to prevent hostname broadcast.
- Disable sending hostname to DHCP server.

## Why?

Ensure packages updates do not overwrite the configuration, and if that happens, just run this script.

## How to use?

Make the script executable
```
$ chmod +x network_trackability_reduction
```
Execute the script
```
$ sudo ./network_trackability_reduction
```

