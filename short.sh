#!/bin/bash
gnome-terminal --tab --title="assignment2" -- bash -c " source ros.sh; roslaunch ExperimentalRoboticsLab assignment2_short.launch"
gnome-terminal --tab --title="armor" -- bash -c "sleep 2; source ros.sh; source ros.sh; rosrun armor execute it.emarolab.armor.ARMORMainService"
gnome-terminal --tab --title="investigation" -- bash -c "sleep 16; source ros.sh; roslaunch ExperimentalRoboticsLab investigation.launch"
gnome-terminal --tab --title="simulation" -- bash -c "sleep 10; source ros.sh; roslaunch ExperimentalRoboticsLab simulation.launch;"
gnome-terminal --tab --title="rosplan" -- bash -c "sleep 25; source ros.sh; roslaunch ExperimentalRoboticsLab rosplan.launch"