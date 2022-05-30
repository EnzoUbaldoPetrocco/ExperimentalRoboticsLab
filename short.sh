#!/bin/bash

gnome-terminal --tab --title="armor" -- bash -c " source ros.sh; source ros.sh; rosrun armor execute it.emarolab.armor.ARMORMainService"
gnome-terminal --tab --title="assignment3" -- bash -c "sleep 2; source ros.sh; roslaunch ExperimentalRoboticsLab assignment3_short.launch"
gnome-terminal --tab --title="simulation" -- bash -c "sleep 10; source ros.sh; roslaunch ExperimentalRoboticsLab simulation.launch 2>/dev/null"
gnome-terminal --tab --title="investigation" -- bash -c "sleep 16; source ros.sh; roslaunch ExperimentalRoboticsLab investigation.launch"
gnome-terminal --tab --title="navigation" -- bash -c "sleep 12; source ros.sh; roslaunch ExperimentalRoboticsLab navigation.launch 2>/dev/null"
gnome-terminal --tab --title="state machine" -- bash -c "sleep 5; source ros.sh; roslaunch ExperimentalRoboticsLab final.launch"