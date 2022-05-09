#!/bin/bash


gnome-terminal --tab --title="assignment2" -- bash -c "source ros.sh; roslaunch ExperimentalRoboticsLab assignment2.launch"
#gnome-terminal --tab --title="bridge" -- bash -c "sleep 5; source ros12.sh; ros2 run ros1_bridge dynamic_bridge"
#gnome-terminal --tab --title="ros2" -- bash -c "sleep 2; source ros2.sh; ros2 launch rt2_assignment1 ros2.py"