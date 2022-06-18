# ExperimentalRoboticsLab
This repository represents the assignments of Experimental Robotics Lab course.
In particular, this branch contains ArUco package, necessary for the implementation of the marker identification.
In order to install this package clone this branch, copy the folder 'aruco_ros' (note that there are two aruco_ros folder, the above-mentioned folder is the parent one), and paste it into the workspace.
Compile the workspace with the command:
```
catkin_make -DCATKIN_WHITELIST_PACKAGES=""
```
The package is now ready.
