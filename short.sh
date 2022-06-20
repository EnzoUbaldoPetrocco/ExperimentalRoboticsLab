#!/bin/bash

gnome-terminal --tab --title="assignment2" -- bash -c "sleep 0; source ros.sh; roslaunch ExperimentalRoboticsLab assignment2_short.launch"
gnome-terminal --tab --title="investigation" -- bash -c "sleep 5; source ros.sh; roslaunch ExperimentalRoboticsLab investigation.launch"
gnome-terminal --tab --title="simulation" -- bash -c "sleep 5; source ros.sh; roslaunch ExperimentalRoboticsLab simulation.launch 2>/dev/null"
gnome-terminal --tab --title="rosplan" -- bash -c "sleep 10; source ros.sh; roslaunch ExperimentalRoboticsLab rosplan.launch"