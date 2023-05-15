#!/bin/bash
# Open the gnome terminal in full screen mode

PID=$(pgrep -x gnome-terminal-)
if [[ $PID -ne "" ]]
then
    xdotool windowactivate `xdotool search --pid $PID | tail -1`
else
    gnome-terminal --full-screen -e tmux
fi
