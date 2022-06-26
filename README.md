# ExperimentalRoboticsLab
This repository represents the third assignment of Experimental Robotics Lab course.

## Introduction
The assignment concerns a robot that has to move randomly in a Cluedo Environment, it enters in the rooms, where it receives some hints. Through the hints the robot must reason and generate hypotheses which have to be consistent, must go to the oracle that knows which hypothesis is the truth and ask him. If the robot has guessed the hypothesis the robot won, else the robot continues to play.
The rooms are:
- x:-4 , y:-3;
- x:-4 , y:2;
- x:-4 , y:7;
- x:5 , y:-7;
- x:5 , y:-3,;
- x:5 , y:1;

Then I added some other reference points, call corridors:
- x:-1 , y:6;
- x:0 , y:-4;
- x:-3 , y:-2;
- x:1 , y:-7;

Note that: 
- A **consistent** hypothesis is a hypothesis which is not inconsistent and is complete.
- A **complete** hypothesis is a hypothesis which has at least one value for each field.
- A **inconsistent** hypothesis is a hypothesis which has more than one value in at least one field.

## System Architecture
System architecture is presented in two ways: component diagram and temporal diagram.

### Component diagram

![Component Diagram](https://user-images.githubusercontent.com/48513075/174858144-dfdfbf52-9c6d-47c9-8612-23cdec851025.png)

List of components:
- SMACH component: this component is used as State Machine manager. It implements the infrastructure of a State Machine and, in theory, also the visualization part of it;
- FSM component: this component actually implements the State Machine. So every node is a version of the finite state machine applied into the problem. This component is a sort of brain of the robot, it controls his behavior. FSM is composed by 5 states, each of them is 'Navigation', 'Investigation', 'GoToOracle', 'Assert' and 'Finished'.
    - Navigation: this state will call RandomPlace Service in order to get a random position. After that, it uses the Navigation component, which will call MoveBase algorithm.
    - Investigation: this state will first call MyMoveIt component in order the robot to reach a precise pose called 'check low first', then it turns until it make an angle of 360°, then it does the same with the pose 'check high first'. In theory with this method, thanks to the width and height of the image camera, every hints can be found. Note that some rooms, called corridors, are added to the list in order to be sure the robot will discover all the hints.
    - GoToOracle: this state simply calls MoveBase in order to reache GoToOracle position: (0,-1).
    - Assert: this node calls Investigate component in order to get the consistent hypotheses. These hypotheses are compared with the true one given by the Oracle.
    - Finished: this state formulates the famous Cluedo Game final sentence and tells you that you have won.
- Navigation component: this component will use RandomPlace service, given by FSM component, in order to get the 2D pose of the robot and then calls MoveBase component in order to manage Navigation part. When the robot arrives to the point it stops the robot motion.
- RandomPlace component: this component uses the list of the possible target rooms and generates a sequence of them. Note that, thanks to an index, this sequence is in fact a circular buffer, so that the robot could continue to navigate to the rooms as much as one want.
- MoveBase component: this component is represented by the algorithm MoveBase. You can look to a better explaining of how it works [here](http://wiki.ros.org/move_base).
- Investigation component: this component is the interface between the Reasoner and the rest of the world. This component manages the operations between hints received and the reasoning about them. Also it is useful in the conversion from the marker id to the hint id.
- Reasoner component: this component is an *ad* *hoc* reasoner. This means you cannot upload an ontology, but it is useful only in this case.
- Simulation component: this component is the component given by professors in order to setup the environment. This component gives the solution of the game, gives an hint given a marker id and places markers and walls around, in the simulation environment.
- MyMoveIt component: this component uses MoveIt package in order to perform *arm* movements. Custom pose and General pose are implemented. 
- MoveIt component: this component uses motion-planning in order to effectively perform *arm* movements. You can visit their website [here](https://moveit.ros.org/).
- Rviz/Gazebo component: even I've put this components together their are in fact two different component. They are used also in the previous assignments, here they are mentioned for precision sake. In Gazebo there are the walls that build the environment given by professor. RViz is used for visualizing the path planning, moveit planning and camera.

### Temporal diagram
Let's consider a lucky case:
![Temporal Diagram](https://user-images.githubusercontent.com/48513075/175829077-e84ad055-0e60-46b2-8370-8470fb6d9c95.png)

This temporal diagram shows a lucky case where the investigation is short.
In this example the robot goes to a location where it finds some hints, during the travel and during the investigation phase.
After completed this phase, the robot has not found a consistent hypothesis.
So it must go to another destination, where it starts investing. After this investigation phase, the robot has found a consistent hypothesis. So it goes to the oracle for asking if it is the correct hypothesis.
Luckily it is the correct hypothesis so the game finished.

## A Sample of the Scenario
Example of the scenario with a video:
[Video](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/assignment3/video)

### Casual Sampling of the scenario
A casual sampling of Gazebo environment is:
![Gazebo](https://user-images.githubusercontent.com/48513075/175826764-1ccb5537-6cc3-47a4-bdb2-90784b98ebfe.png)
A casual sampling of RViz environment is:
![RViz](https://user-images.githubusercontent.com/48513075/175826773-acabb95e-d512-4eba-a394-ed7806b6e504.png)



## Installation and Running Procedure
### Installation
In order to install this package we have to be sure to have all the components.
ROS environment is of course trivial, but it is needed also a particular package which is 'move_base', so make sure you have installed it.
From this branch, copy ExperimentalRoboticsLab folder, and paste it into the workspace.
Armor reasoner has been substitued by a custom reasoner, so that package is no more required.
PDDL has been used nomore, so is valid same for it.
MoveIt package has been changed together with robot description, so another branch has been added: [m2wr_moveit2](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/m2wr_moveit2). From this branch, copy the folder 'm2wr_moveit' and paste it into the workspace.
ArUco Ros package is used for marker detection. You can find a modified version in the branch: [aruco_ros_package](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/aruco_ros_package). From this branch, copy the folder 'aruco_ros'  (note that there are two aruco_ros folder, the above-mentioned folder is the parent one), and paste it into the workspace. Compile the workspace with the command:
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

The previous one was the recommended running procedure.
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
The environment is represented by a static map, where we have many rooms; this conformation introduces static obstacles, so that a path planning algorithm should take into account also static obstacles. MoveBase algorithm has been chosen in order to overcome this problem, this problem 

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
- The investiganting node could be splitted in two parts: one for treating with a general reasoner, one for treating to armor in particular, this could increase modularity and flexibility.

## Author
The author of this repository is [Enzo Ubaldo Petrocco](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab): i'm a student of robotics engineering in the University of Genova (s4530363); if you have some issues please contact me:
- email: enzopetrocco@hotmail.it
