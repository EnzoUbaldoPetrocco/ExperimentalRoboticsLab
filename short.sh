#!/bin/bash
gnome-terminal --tab --title="simulation" -- bash -c " source ros.sh; roslaunch ExperimentalRoboticsLab simulation.launch 2>/dev/null"
gnome-terminal --tab --title="assignment3" -- bash -c "sleep 23; source ros.sh; roslaunch ExperimentalRoboticsLab assignment3_short.launch"
gnome-terminal --tab --title="investigation" -- bash -c "sleep 26; source ros.sh; roslaunch ExperimentalRoboticsLab investigation.launch"
gnome-terminal --tab --title="state machine" -- bash -c "sleep 27; source ros.sh; roslaunch ExperimentalRoboticsLab final.launch 2>/dev/null"
gnome-terminal --tab --title="navigation" -- bash -c "sleep 29; source ros.sh; roslaunch ExperimentalRoboticsLab navigation.launch 2>/dev/null"