#!/bin/bash

sudo echo

cd ~/openvpn-CA/recived

sudo cp crl.pem /etc/openvpn/server

sudo grep crl-verify /etc/openvpn/server/server.conf > /dev/null \
&& sudo echo "crl-verify /etc/openvpn/server/crl.pem" | sudo tee -a /etc/openvpn/server/server.conf

cd - > /dev/null

echo "crl.pem updated"