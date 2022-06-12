# Assignment 2 of Experimental Robotics Laboratory course

This is the second assignment of the course, in this assignment I have had to implement some features of the robot in a cluedo game environment. In particular: planning part and robot description and his movements in an simulation environment.
Also some little changes have been made, but the main concept has been maintained. 
In particular: you have a robot, which must find hints, like it is playing cluedo game, it must reason about possible complete hypotheses and then, it must ask to the oracle if the hypothesis is correct. If it is not, the robot must go on and keep playing until it finds the solution.

## Software structure
From an architectural point of view the software is structured as follows, a better explanation of services, actions, ... is explained below the picture, this is done because of readability of the component diagram.

#### Component diagram
![class_diagram_ass_2 drawio (2)](https://user-images.githubusercontent.com/48513075/166264792-902c78d4-b3b1-4d31-9056-ff45079da4a8.png)


- Rosplan component: this component is launched by Rosplan Management when program starts, it asks him to generate a plan from the domain and problem described by the Rosplan Management component through services. This component is responsible for launching the 4 actions Navigation, Find Hint, Reason and Oracle, which in this part are described as component.
Each of the previous 4 actions/components mentioned before has a some general properties that may be interesting to be outlined: 
1. **The action can fail in its aim**, in fact it's impossibile that these actions let the program finish in a single plan, this is due from the fact that a complete hypothesis is made by 3 hints, so a service toward rosplan management must be performed in order to replan if something fails. The service is "/replan" service.
2. **Every action decouples the problem and the other components**, in order to not write too specific code, and in order to perform flexibility concept, every nodes link the rosplan, which can be changed in order to perform other types of plans, and Go To Point, My MoveIt and Investigation components, which are more general and can be used in other contexts (as you can see, since Go To Point and Investigation come from previous assignment)
- Rosplan Management component: this component can be called from each action/component through "/replan" service. Every time it is called, this component must make a new plan. When the robots simply plays, this component manages the dispatch of the actions.
- Navigation component: this component must perform the respective durative action of the PDDL plan. At the beginning of the action the robot is at a waypoint, then it is at another one. In order to perform effectively the navigation, this node sends an action to the Go To Point component (alias go_to_point node), which will perform a navigation algorithm. The waypoint location is chosen randomly among the different possibilities.
- Find Hint component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot is at a waypoint with his arm in a custom pose, previously chosen in order to be as stable as possible (also this can be discussed as possible improvements). Then the component calls My MoveIt component, (the details are explained below), with a custom action HintAction twice (marker can be in 2 points), at the end of the action the robot cluedo joint must have found the hint.
- Reason component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot must reason about the hints he have. Notice that, as said before, at the beginning it is impossible to have complete hypotheses, so it is impossible to have consistent hypotheses, so this action will fail several times. This component calls Investigate component in order to know if there are consistent hypotheses. 
- Oracle component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot must perform a navigation to the oracle, through the GoToPoint component and then must ask to the Oracle (which is in the Simulation Component).
- GoToPoint component: this component must perform navigation action. The algorithm is such that the result can be shown through simulation in RViz and Gazebo environments, where also the physics of the robot is simulated. Here can be noticed, for example, the precision and limitations of the algorithm, which simply perform a rotation until correct angle is reached, and then moves on straightforward; for this reason this is not a suitable algorithm for obstacle avoidance.
- My MoveIt component: this component must perform arm movements. One can choose if the robot must reach a custom pose or you can give a pose to the robot and then it reaches it with the cluedo link. There are 2 actions respectively CustomTargetAction, HintAction.
- Investigation component: this component represent the link with the reasoner part. When it is needed, it calls Armor, and asks him for consistent hypotheses. This component also adds automatically the hints into the owl file, if they are well formed.
- Armor component: this component represent the reasoner, hints correctly formed are stored in owl file and then, the Armor reasoner is responsible for check to consistent hypotheses. 
- MoveIt component: this component is responsible for IK, planning parts and, when it is asked for a target, IK procedure is called, then planning procedure runs. After this, joints controller are used for reaching the target.
- Simulation component: this component manages hints generation, check of the true consistent hypothesis, marker position in the rviz scenario.
- MoveIt component: this component is generated by moveit setup assistant. This manages controllers, launch file, simulation etc. In this package it is slightly modified, in order to use gazebo and rviz that have been already generated.
- Armor component: this component uses reasoner and ontology of Armor. This is simply the Armor Server with its functionalities.

#### Flowchart
Here below there is the flowchart explaining how the planning part works.
![flowchart drawio](https://user-images.githubusercontent.com/48513075/167388758-dde170b4-af95-4ef7-be8d-07c60f2e1a5d.png)

#### Temporal Diagram
![TemporalDiagram drawio](https://user-images.githubusercontent.com/48513075/168557788-1fb6998d-a01f-48ce-9d5a-d9242645b80d.png)
Temporal diagram is an example of the most lucky case, where rosplan node initialize the plan, the robot navigates until a waypoint, a hint is found, but there is no complet hypothesis, so a new plan is dispatched thanks to rosplan node. This happend two times.
The third time find_hint node is executed, a complete hypothesis is found and it is the exact one. 

## Installation and Running Procedure
### Installation
In order to install this package you should have [Armor][https://github.com/EmaroLab/armor], but the package 'armor_py_api' must be replace with the one which can be found in the branch 'armor_api' of this repository.
In order to not have problems with docker, replace: armor_api.armor_exceptions with armor_api anywhere in armor_api folder in armor_py_api.
Two packages must be installed and built in order to run the code: [assignment2](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/assignment2) and [m2wr_moveit](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab/tree/m2wr_moveit).

the entire package ExperimentalRoboticsLab download from assignment2 must be pasted in the workspace, while only the package m2wr_moveit package of m2wr_moveit branch must be pasted in the workspace.
Then ROS terminal source must be done.

After this, build your workingspace with:
```
catkin_make
```

### Running Procedure
In order to run the program, go inside the folder: ExperimentalRoboticsLab in the workspace and run:
```
./short.sh
```
Some terminals will open. Don't care about warnings in the fourth terminal opened.

## A Sample of the scenario
### Casual sample of navigation
![Screenshot from 2022-05-19 18-11-47](https://user-images.githubusercontent.com/48513075/169991482-2209fea6-8db1-460b-a9a2-2a48daf17d91.png)

### Conclusion
![Screenshot from 2022-05-24 10-49-20](https://user-images.githubusercontent.com/48513075/169991240-0e46e07b-b97d-4378-bac8-82a8d652da37.png)

## Working hypothesis and environment
### System's feature
The system must play cluedo game in a simulated environment.
System is capable of:
- Perform a complete plan/replan procedure with a fixed domain and a fixed problem;
- Perform arm movements until a custom pose and a reachable pose;
- Perform navigation through a simulated environment, devoid of obstacles;
- Perform reasoner part given an ontology structure.
System in general is characterized also by:
- Hints are objects with fields: 
    1) ID: this tells the hypothesis the hint belongs to;
    2) value: tells the value of the hint;
    3) key: may be "where","who","what" and tells the type of hint;
- Hints can be not well generated;
- Every action can fail, so a replan strategy is implemented every time it is needed;
- Hints can be at different altitudes.

### System's limitations
- System is very slow, in order to minimize failures;
- Navigation node does not perform obstacle avoidance;
- Arm motion node does not perform obstacle avoidance;
- Arm motion is slow, also due to the fact that PID control is not optimal, PID controllers are chosen thanks to trial and error;
- Navigation is slow, this is due to the fact that robot must be stable and must not 'wheelie';
- Robot chassis is not as small as possible (in order to reduce configuration space), in order to assure stability while arm is moving;
- Arm is not efficient in its movements: between the two poses the robot passes through the home pose;
- Replanning and ROSPlan are not efficient, also, sometimes it fails. Maybe the finite state machine is faster. On the contrary ROSPlan is more flexible;
- Random waypoint approach may produce the same waypoint;
- User Interface may help in start and restart the game.
- Optimizations can be done: planner could use a function in order to know if at least 3 hints must be found before asking the reasoner.


## Authors and contacts
The author of this repository is [Enzo Ubaldo Petrocco](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab): i'm a student of robotics engineering in the University of Genova (s4530363); if you have some issues please contact me:
- email: enzopetrocco@hotmail.it 

