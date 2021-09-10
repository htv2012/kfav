#!/usr/bin/env bash
sudo cp ./kfav.service /etc/systemd/system
sudo systemctl enable kfav
sudo systemctl start kfav

