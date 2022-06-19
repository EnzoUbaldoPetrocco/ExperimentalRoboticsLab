# ExperimentalRoboticsLab
This repository represents the assignment of Experimental Robotics Lab course

## Introduction
The assignment concerns a robot that has to move randomly in a Cluedo Environment, enter in the rooms, where it receives some hints. Through the hints the robot must reason and generate hypotheses which have to be consistent, must go to the oracle that knows which hypothesis is the truth and ask him. If the robot has guessed the hypothesis the robot won, else the robot continues to play.

The following assignment is: [Assignment2](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/assignment2)

## Software Structure

### Component diagram:

![Component diagram](https://user-images.githubusercontent.com/48513075/142313128-79114576-d12c-440f-b708-89f265e6ec3d.jpg)


### Sequence diagram:

![Sequence diagram](https://user-images.githubusercontent.com/48513075/142313898-8d2a956a-f888-4b72-b59d-f9262063f341.jpg)

## Video
Example of the working with a video:
![Video](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/main/video)




## Installation
In order to install this package you should have [Armor][https://github.com/EmaroLab/armor], but the package 'armor_py_api' must be replace with the one which can be found in the branch 'armor_api' of this repository.
In order to not have problems with docker, replace: armor_api.armor_exceptions with armor_api anywhere in armor_api folder in armor_py_api.

In order to compile the workspace you have to source setup.bash, from your workspace:

```
source devel/setup.bash

```

Then you have to compile it:

```
catkin_make
```

Now the packages are ready.

## Running Procedure
Every time you want to launch the program you have to source the terminal as explained in the previous chapter.

In order to launch the program:

```
roslaunch ExperimentalRoboticsLab basic.launch
```


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
