# ExperimentalRoboticsLab
This repository represents the third assignment of Experimental Robotics Lab course.

## Introduction
The assignment concerns a robot that has to move randomly in a Cluedo Environment, it enters in the rooms, where it receives some hints. Through the hints the robot must reason and generate hypotheses which have to be consistent, must go to the oracle that knows which hypothesis is the truth and ask him. If the robot has guessed the hypothesis the robot won, else the robot continues to play.

## System Architecture
### Component diagram

![Component Diagram](https://user-images.githubusercontent.com/48513075/174617451-fa774280-29b3-43e3-a6c4-1100e7938c0d.png)



### Sequence diagram

![Sequence diagram](https://user-images.githubusercontent.com/48513075/142313898-8d2a956a-f888-4b72-b59d-f9262063f341.jpg)

## Video
Example of the working with a video:
![Video](https://unigeit-my.sharepoint.com/:f:/g/personal/s4530363_studenti_unige_it/Evgh67vVc89EnqRuW1RhmTUBw8b1sSGz_1oKpHSLzuI49g?e=etqFqy)


## Installation and Running Procedure
### Installation
In order to install this package we have to be sure to have all the components.
ROS environment is of course trivial, but it is needed also a particular package which is 'move_base', so make sure you have installed it.
From this branch, copy ExperimentalRoboticsLab folder, and paste it into the workspace.
Armor reasoner has been substitued by a custom reasoner, so that package is no more required.
PDDL has been used nomore, so is valid same for it.
MoveIt package has been changed together with robot description, so another branch has been added: ![m2wr_moveit2](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/m2wr_moveit2). From this branch, copy the folder 'm2wr_moveit' and paste it into the workspace.
ArUco Ros package is used for marker detection. You can find a modified version in the branch: ![aruco_ros_package](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/aruco_ros_package). From this branch, copy the folder 'aruco_ros'  (note that there are two aruco_ros folder, the above-mentioned folder is the parent one), and paste it into the workspace. Compile the workspace with the command:
```
catkin_make -DCATKIN_WHITELIST_PACKAGES=""
```
The package is now ready.


### Running Procedure
After sourcing the terminal:

```
source bash.sh
```

In order to launch the program, go into the ExperimentalRoboticsLab folder and write write in the terminal:

```
./short.sh
```

The previous one was the recommended run procedure.
But this is not the only one way, of course, single launch file can be launched in different terminals, in each of them you have to go into the folder: ExperimentalRoboticsLab and run:

```
source ros.sh 
```
Then the sequence, in each terminal:
```
roslaunch ExperimentalRoboticsLab simulation.launch 2>/dev/null
```
```
roslaunch ExperimentalRoboticsLab assignment3_short.launch
```
```
roslaunch ExperimentalRoboticsLab investigation.launch
```
```
roslaunch ExperimentalRoboticsLab final.launch 2>/dev/null
```
```
roslaunch ExperimentalRoboticsLab navigation.launch 2>/dev/null
```

You can get rid of the '2>/dev/null' if you want to see warnings.
## Assumptions, working hypotheses and environment

### System's features
The system is capable of simulating an environment, with some limitations, where the robot has to reach a position and receives hints which will let him to reason on them and arriving to some solutions (aka consistent hypotheses). 
One solution is the right one and can be revealed when the robots arrives to the oracle and ask for the right solution.
Given that, the system has:
- a state machine, which organizes the robot's work;
- a navigation simulation, which manages the navigation part. Up to now it is very simple, but can be modified in order to become a real navigation system;
- a investigation node, which has to communicate with the 'reasoner' (in this case armor, but the node can be of course substituted at will);
- an oracle has been provided, so that you can ask him for the right solution and for hints;
- a random place node which gives the random targets.

Note that some specifications/characteristics of the system are:
- An hypothesis is considered 'consistent' if it is not 'inconsistent' and is 'complete';
- An hypothesis is considered 'inconsistent' if a field has more than one value;
- An hypothesis is considered 'complete' if every field has at least one value;
- The list of the possible hypotheses has been written in a json format, which has a high readability and can be managed also by hand;
- In order to increase performances hints sent are registered (in json format), in order to not send hints already sent;
- Consistent hypotheses are saved in a file in order to know what hypotheses can be asked to the oracle, it is saved also if an hypothesis has been asked to the oracle. This system may appear a bit redundant, since a message with the new complete hypothesis could be used. But in fact this redundancy can be useful in order to keep track to the previous hypotheses and in order to increase flexibility (maybe one could want to receive many hints for a room, in this case the message mechanism does not work anymore, this in fact is more flexible).

### System's limitations
- Navigation is simulated, the robot waits proportionally to the 'distance'. As distance angle is not taken into account;
- Hints are always given with an hypothesis ID, which they belong to;
- The correct hypothesis has been selected randomly by the oracle among preselected consistent hypotheses;
- Rooms are mapped as specific Pose (x,y,theta);
- Robot is a point;
- The usage of json file as a way of exchanging information is not a proper way of passing information among nodes. But since the file does not change continously, it may be considered a weak limitation in terms of performance.

### Possible improvements
Many possible improvements can be achieved: 
- a room could be mapped as an area, so that the robot is in a room when in fact is in it;
- navigation could be simulated using a 'real' environment, the rooms can be mapped into a system like Gazebo or Rviz, and a robot type could be selected in order to actually navigate in an environment. Note that, if it has to be done, navigation must be replaced with a state machine, a planning algorithm must be selected and these depend also on the previous point (if the room is mapped like a Pose or as an area);
- Hints could be considered as hints without an ID which indicates the corresponding hypothesis: even if the specifications indicate the contrary, at the expense of an exponential growth in terms of complexity, hints can be part of multiple hypotheses. This change must involve also the oracle, due to this reason an improvement can be found: telling if an hint in a hypothesis is right or wrong for every hint in a hypothesis. If this is done, of course consistent_hypotheses file becomes crucial for what said in the previous paragraph
- Another improvement could be the physical search of hints in the room, the robot could search for Qrcode for example in a room, and they can be considered as hints. Or alternatively, 'physical object' could be placed in the room and revealed thanks to object recognition paradigms;
- The investiganti node could be splitted in two parts: one for treating with a general reasoner, one for treating to armor in particular, this could increase modularity and flexibility.

## Author
The author of this repository is [Enzo Ubaldo Petrocco](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab): i'm a student of robotics engineering in the University of Genova (s4530363); if you have some issues please contact me:
- email: enzopetrocco@hotmail.it
