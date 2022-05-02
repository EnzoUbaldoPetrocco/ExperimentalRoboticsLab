# Assignment 2 of Experimental Robotics Laboratory course

This is the second assignment of the course, in this assignment I have had to implement some features of the robot in a cluedo game environment. In particular: planning part and robot description and his movements in an simulation environment.
Also some little changes have been made, but the main concept has been maintained. 
In particular: you have a robot, which must find hints, like it is playing cluedo game, it must reason about possible complete hypotheses and then, it must ask to the oracle if the hypothesis is correct. If it is not, the robot must go on and keep playing until it finds the solution.

## Software structure
From an architectural point of view the software is structured as follows, a better explanation of services, actions, ... is explained below the picture, this is done because of readability of the component diagram.
![class_diagram_ass_2 drawio](https://user-images.githubusercontent.com/48513075/166214452-e6c7a5bf-adf2-4239-92ba-cda7e8d5a8be.png)


- UserInterface component: this component asks to the user to play the game, when done it let the robot launching rosplan and starts the game. Rosplan Management and User Interface components communicate each other thanks to a custom action UserInterfaceAction.
- Rosplan component: this component is launched by Rosplan Management when User Interface asks him to generate a plan from the domain and problem described by the Rosplan Management component through services. This component is responsible for launching the 4 actions Navigation, Find Hint, Reason and Oracle, which in this part are described as component.

## Installation and Running Procedure

## A Sample of the scenario

## Working hypothesis and environment

## Authors and contacts
The author of this repository is [Enzo Ubaldo Petrocco](https://github.com/EnzoUbaldoPetrocco/ExperimentalRoboticsLab): i'm a student of robotics engineering in the University of Genova (s4530363); if you have some issues please contact me:
- email: enzopetrocco@hotmail.it 

