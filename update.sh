#!/usr/bin/env bash
rm -rf /home/monitor/kuuma
mkdir -p /home/monitor/kuuma
cp -r src main.py config.properties requirements.txt /home/monitor/kuuma
chmod +x /home/monitor/kuuma/main.py

cp kuuma.service /etc/systemd/system/kuuma.service
systemctl daemon-reload
systemctl enable kuuma
systemctl restart kuuma
