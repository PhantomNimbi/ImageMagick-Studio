#!/bin/bash

# Change the working directory to the folder where this script lives
cd "$(dirname "$0")"

# Execute Python cleanly in the background, suppressing terminal-locking logs
nohup python3 main.py > /dev/null 2>&1 &

# Instantly close the empty terminal window that the OS automatically spawns
osascript -e 'tell application "Terminal" to close first window' &
exit 0
