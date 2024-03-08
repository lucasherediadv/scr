#!/bin/bash
#
# Description

# Path to the configuration file
CONF_FILE="/etc/NetworkManager/conf.d/99-random-mac.conf"

# Create the configuration file or overwrite if it already exists
cat <<EOF > "$CONF_FILE"
[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=random
ethernet.cloned-mac-address=random
EOF

# Set appropriate permissions to the file
chmod 644 $CONF_FILE

echo "Configuration file $CONF_FILE created succsesfully"

# Reload NetworkManager configuration
sudo nmcli general reload conf

# Disable sendind hostname to DHCP server

CONNECTION_UUID="your_connection_uuid_here" # Assuming you'll pass the connection UUID as an argument

cat <<EOF | sudo tee /etc/NetworkManager/dispatcher.d/no-wait.d/01-no-send-hostname.sh > /dev/null
#! /bin/bash

if [ "$(nmcli -g 802-11-wireless.cloned-mac-address c show "$CONNECTION_UUID")" = 'permanent' ] \
  || ["$(nmcli -g 802-3-ethernet.cloned-mac-address c show "$CONNECTION_UUID")" = 'permanent' ]
then
  nmcli connection modify "$CONNECTION_UUID" \
    ipv4.dhcp-send-hostname true \
    ipv6.dhcp-send-hostname true
else
  nmcli connection modify "$CONNECTION_UUID" \
    ipv4.dhcp-send-hostname false \
    ipv6.dhcp-send-hostname false
fi
EOF

# Set ownership and permissions
sudo chown root:root /etc/NetworkManager/dispatcher.d/no-wait.d/01-no-send-hostname.sh

# Create the symbolic link
sudo ln -s /etc/NetworkManager/dispatcher.d/no-wait.d/01-no-send-hostname.sh ./

