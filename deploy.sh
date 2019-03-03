#!/usr/bin/env bash
HOST=$1
USER=$2

ssh "$USER@$HOST" "rm -r /home/$USER/kuuma"
ssh "$USER@$HOST" "mkdir -p /home/$USER/kuuma"
scp -r src main.py config.properties requirements.txt kuuma.service update.sh "$USER@$HOST:/home/$USER/kuuma"
