# Assignment 2 of Experimental Robotics Laboratory course

This is the second assignment of the course, in this assignment I have had to implement some features of the robot in a cluedo game environment. In particular: planning part and robot description and his movements in an simulation environment.
Also some little changes have been made, but the main concept has been maintained. 
In particular: you have a robot, which must find hints, like it is playing cluedo game, it must reason about possible complete hypotheses and then, it must ask to the oracle if the hypothesis is correct. If it is not, the robot must go on and keep playing until it finds the solution.

## Software structure
From an architectural point of view the software is structured as follows, a better explanation of services, actions, ... is explained below the picture, this is done because of readability of the component diagram.

![class_diagram_ass_2 drawio (2)](https://user-images.githubusercontent.com/48513075/166264792-902c78d4-b3b1-4d31-9056-ff45079da4a8.png)


- UserInterface component: this component asks to the user to play the game, when done it let the robot launching rosplan and starts the game. Rosplan Management and User Interface components communicate each other thanks to a custom action UserInterfaceAction.
- Rosplan component: this component is launched by Rosplan Management when User Interface asks him to generate a plan from the domain and problem described by the Rosplan Management component through services. This component is responsible for launching the 4 actions Navigation, Find Hint, Reason and Oracle, which in this part are described as component.
Each of the previous 4 actions/components mentioned before has a some general properties that may be interesting to be outlined: 
1. **The action can fail in its aim**, in fact it's impossibile that these actions let the program finish in a single plan, this is due from the fact that a complete hypothesis is made by 3 hints, so a service toward rosplan management must be performed in order to replan if something fails. The service is "/replan" service.
2. **Every action decouples the problem and the other components**, in order to not write too specific code, and in order to perform flexibility concept, every nodes link the rosplan, which can be changed in order to perform other types of plans, and Go To Point, My MoveIt and Investigation components, which are more general and can be used in other contexts (as you can see, since Go To Point and Investigation come from previous assignment)
- Rosplan Management component: this component is called from UserInterface through UserInterfaceAction and is also called from each action/component through "/replan" service. Every time it is called, this component must understand where the robot is and must make a new plan.
- Navigation component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot is at a waypoint, then it is at another one. In order to perform effectively the navigation, this node sends an action to the Go To Point component (alias go_to_point node), which will perform a navigation algorithm.
- Find Hint component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot is at a waypoint with his arm in a custom pose, previously chosen in order to be as stable as possible (also this can be discussed as possible improvements). Then the component calls My MoveIt component, (the details are explained below), with a custom action HintAction, at the end of the action the robot cluedo joint must have found the hint.
- Reason component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot must reason about the hints he have. Notice that, as said before, at the beginning it is impossible to have complete hypotheses, so it is impossible to have consistent hypotheses, so this action will fail several times. This component calls Investigate component in order to know if there are consistent hypotheses. 
- Oracle component: this component must perform the respective durative action of the pddl plan. At the beginning of the action the robot must perform a navigation to the oracle, through the GoToPoint component and then must ask to the Oracle (which is in the Simulation Component), 
- GoToPoint component: this component must perform navigation action. The algorithm is such that the result can be shown through simulation in RViz and Gazebo environments, where also the physics of the robot is simulated. Here can be noticed, for example, the precision and limitations of the algorithm, which simply perform a rotation until correct angle is reached, and then moves on straightforward; for this reason this is not a suitable algorithm for obstacle avoidance.
- My MoveIt component: this component must perform arm movements. One can choose if the robot must reache a custom pose or you can give a pose to the robot and then it reaches it with the cluedo link. There are 2 actions respectively CustomTargetAction, HintAction.
- Investigation component: this component represent the link with the reasoner part. When it is needed it calls Armor, and asks him for consistent hypotheses. This component also add aumatically the hints into the owl file if they are well formed.
- Armor component: this component represent the reasoner, hints correctly formed are stored in owl file and then the Armor reasoner is responsible for check for consistent hypotheses. 
- MoveIt component: this component is responsible for IK, planning parts and . When it is asked for a target IK procedure is called, than planning procedure runs. After this, joints controller are used for reaching the target.
- Simulation component: this component manages hints generation, check of the true consistent hypothesis, marker position in the rviz scenario.

## Installation and Running Procedure

## A Sample of the scenario

## Working hypothesis and environment

## Authors and contacts
The author of this repository is [Enzo Ubaldo Petrocco](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab): i'm a student of robotics engineering in the University of Genova (s4530363); if you have some issues please contact me:
- email: enzopetrocco@hotmail.it 

