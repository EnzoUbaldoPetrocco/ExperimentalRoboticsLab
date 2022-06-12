#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file fsm.py
# \brief node implementing the finite state machined
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date November 2021
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   
#
# ServiceCline:<BR>
#   /random_place_service (ExperimentalRoboticsLab.srv.RandomPlace)
#   /investigate (ExperimentalRoboticsLab.srv.Investigate)
#   /ask_solution (ExperimentalRoboticsLab.srv.TrySolution)
#
# ActionServer:<BR>
#   /go_to_point (ExperimentalRoboticsLab.action.PositionAction)
#
#
# Description:
#
# fsm.py is a script which manages a state machine which represents the actions that a robot must do in
# order to play Cluedo in a fictitious environment. 
# The FSM has 5 states:
#       Navigation: the robot navigates through an environment thanks to the random position
#       which has been given by a custom service, possible outcomes are:
#                                       - investigation
#                                       - navigation
#       Investigation: the robot investigates thanks to armor client, in order to know if there is 
#       a consistent hypothesis, possible outcomes are:
#                                       - navigation
#                                       - investigation
#                                       - go_to_oracle
#       GoToOracle: the robot goes to the oracle; even if in this implementation the only outcome 
#       is assert, in theory the possible outcomes are:
#                                       - navigation
#                                       - investigation
#                                       - go_to_oracle_
#                                       - assert
#       Assert: the robot asks if among the consistent hypotheses it has there is
#       the correct one, possible outcomes are:
#                                       - navigation
#                                       - investigation
#                                       - go_to_oracle
#                                       - assert
#                                       - finished
#       Finished: the robot has won
#
#
# 
##

import actionlib
import rospy
import smach
import smach_ros
import time
from datetime import datetime
from ExperimentalRoboticsLab.srv import RandomPlace
from ExperimentalRoboticsLab.srv import Investigate, InvestigateRequest
from ExperimentalRoboticsLab.srv import TrySolution
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction
import json
from ExperimentalRoboticsLab.srv import *
from std_msgs.msg import *
from nav_msgs.msg import *
from move_base_msgs.msg import *
from geometry_msgs.msg import *
from actionlib import SimpleGoalState
## GLOBAL VARIABLES

## boolean global variable set to true when the robot reaches its target position
reached = False
## random position client global variable
random_position_client = None

def move_arm_routine():
    global mymoveit_client, cmd_pub
    while mymoveit_client.get_state != SimpleGoalState.DONE:
        velocity = Twist()
        velocity.linear.x = 0
        velocity.angular.z = 0
        cmd_vel_pub.publish(velocity)
        time.sleep(2)

## define state Navigation
class Navigation(smach.State):
    def __init__(self):
        """!
        /init function of Navigation class
        It initialize the Navigation class
        """
        smach.State.__init__(self, 
                             outcomes=['navigation', 'investigation'])
    
    def arrived_to_the_point(msg):
        """!
        /go_to_point callback
        It sets the result of the action go to point
        /param msg (bool)
        """
        global reached
        reached = msg.result
    
    def choosing_random_position():
        """!
        /choosing_random_position
        It calls /random_place_service in order to get a random destination
        /param None
        """
        global random_client
        position = ExperimentalRoboticsLab.msg.PositionGoal()
        rnd_place = random_client()
        position.x = rnd_place.x
        position.y = rnd_place.y
        position.theta = rnd_place.theta
        return position


    def execute(self, userdata):
        """!
        /execute state
        It executes the Navigation state: it selects a random target 
        and sends it to the navigation node, then it waits
        /param userdata ()
        """
        global reached, mymoveit_client
        hint_goal = ExperimentalRoboticsLab.msg.HintGoal()
        hint_goal.pose = "home"
        mymoveit_client.send_goal(hint_goal)
        mymoveit_client.wait_for_result()
        #time.sleep(5)
        #move_arm_routine()
        #mymoveit_client.wait_for_result()
        goal = Navigation.choosing_random_position()
        print("\nGoing to [" + str(goal.x) + "," + str(goal.y) + "] with orientation " +  str(goal.theta) + "\n")
        random_position_client.send_goal(goal)
        # function called when exiting from the node, it can be blacking
        random_position_client.wait_for_result()
        #while reached == False:
        #    time.sleep(2)
        #reached = False
        return 'investigation'
    

## define state Investigation
class Investigation(smach.State):
    def __init__(self):
        """!
        /init function of Investigation class
        It initialize the Investigation class
        """
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle'])

    def execute(self, userdata):
        """!
        /execute state
        It executes the Investigation state: it calls investigation 
        node and check if it has to go to the oracle or go to get other
        hints
        /param userdata ()
        """
        #rospy.wait_for_service('/investigate')
        global investigate_client, mymoveit_client, cmd_vel_pub
        hint_goal = ExperimentalRoboticsLab.msg.HintGoal()
        
        print("\nInvestigating...\n")
        hint_goal.pose = "check low first"
        mymoveit_client.send_goal(hint_goal)
        mymoveit_client.wait_for_result()
        velocity = Twist()
        velocity.linear.x = 0
        velocity.angular.z = (2 * 3.14)/8
        cmd_vel_pub.publish(velocity)
        time.sleep(10)
        print('Looking around...')
        hint_goal.pose = "check low second"
        mymoveit_client.send_goal(hint_goal)
        mymoveit_client.wait_for_result()
        velocity.angular.z = (2 * 3.14)/10
        cmd_vel_pub.publish(velocity)
        time.sleep(8)
        print('Looking around...')
        hint_goal.pose = "check high first"
        mymoveit_client.send_goal(hint_goal)
        mymoveit_client.wait_for_result()
        velocity.angular.z = (2 * 3.14)/10
        cmd_vel_pub.publish(velocity)
        time.sleep(8)
        req = InvestigateRequest()
        req.investigate = False
        res = investigate_client(req)
        if len(res.IDs) == 0 :#or shall_go==True:
            next_step = 'navigation'
        else:
            next_step = 'go_to_oracle'
        return next_step

## define state GoToOracle
class GoToOracle(smach.State):
    def __init__(self):
        """!
        /init function of GoToOracle class
        It initialize the GoToOracle class
        """
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle', 'assert'])

    def position_of_the_oracle():
        """!
        /position_of_the_oracle
        It gives simply the position of the oracle (by default it is 0,0 with theta = 0)
        """
        position = ExperimentalRoboticsLab.msg.PositionGoal()
        position.x = 0
        position.y = -1.0
        position.theta = 0
        return position

    def execute(self, userdata):
        """!
        /execute state
        It executes the GoToOracle state: it retrieves position of the oracle 
        and send it to the navigation node, then waits
        /param userdata ()
        """
        global reached
        print("\nI am going to speak with the oracle\n")
        goal = GoToOracle.position_of_the_oracle() 
        random_position_client.send_goal(goal)
        random_position_client.wait_for_result()
        
        return 'assert'

## define state Assert
class Assert(smach.State):
    def __init__(self):
        """!
        /init function of Assert class
        It initialize the Assert class
        """
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle', 'assert', 'finished'])

    def execute(self, userdata):
        """!
        /execute state
        It executes the Assert state: it retrieves consistent hypotheses 
        and ask to the oracle if they are correct
        /param userdata ()
        """
        global reached
        print("\nI am telling to the oracle my hypotheses\n")
        req = InvestigateRequest()
        req.investigate = True
        res = investigate_client(req)
        oracle_res = oracle_client()
        for i in res.IDs:
            if i==oracle_res.ID:
                return 'finished'
        return 'navigation'
        
## define state Finished
class Finished(smach.State):
    def __init__(self):
        """!
        /init function of Finished class
        It initialize the Finished class
        """
        smach.State.__init__(self, outcomes=['finish'])

    def execute(self, userdata):
        """!
        /execute state
        It executes the Finished state: it states that the fsm is finished
        /param userdata ()
        """
        print('\nCongratulations, you won')
        return 'finish'

        
## Main function
def main():
    """!
        /main function
        It initialize the node fsm, then the clients and actions needed, also the fsm with smach
        then it waits
        /param userdata ()
        """
    global random_position_client, file_path, random_client, investigate_client, random_position_client, mymoveit_client, cmd_vel_pub, oracle_client
    rospy.init_node('fsm')

    random_client = rospy.ServiceProxy('/random_place', RandomPlace)
    random_position_client = actionlib.SimpleActionClient("/go_to_point", ExperimentalRoboticsLab.msg.PositionAction)
    rospy.Subscriber('/go_to_point/result', ExperimentalRoboticsLab.msg.PositionActionResult, Navigation.arrived_to_the_point)
    investigate_client = rospy.ServiceProxy('/investigate', Investigate)
    mymoveit_client = actionlib.SimpleActionClient("/hint", ExperimentalRoboticsLab.msg.HintAction)
    oracle_client = rospy.ServiceProxy("/oracle_solution", Oracle)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    random_client.wait_for_service()
    investigate_client.wait_for_service()
    random_position_client.wait_for_server()
    mymoveit_client.wait_for_server()
    #ask_solution_client.wait_for_service()
    #rospy.sleep(1)
    # Create a SMACH state machine
    fsm = smach.StateMachine(outcomes=['finish'])

    # Open the container
    with fsm:
        # Add states to the container
        smach.StateMachine.add('NAVIGATION', Navigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION'})
        smach.StateMachine.add('INVESTIGATION', Investigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION',
                                            'go_to_oracle': 'GOTOORACLE'})
        smach.StateMachine.add('GOTOORACLE', GoToOracle(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION',
                                            'go_to_oracle': 'GOTOORACLE',
                                            'assert': 'ASSERT'})
        smach.StateMachine.add('ASSERT', Assert(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION',
                                            'go_to_oracle': 'GOTOORACLE',
                                            'assert': 'ASSERT',
                                            'finished': 'FINISHED'})
        smach.StateMachine.add('FINISHED', Finished(),
                                transitions={
                                    'finish':'finish'
                                }
                            )
        
        

     # Create and start the introspection server for visualization
    sis = smach_ros.IntrospectionServer('server_name', fsm, '/SM_ROOT')
    
    sis.start()
    
    # Execute the state machine
    outcome = fsm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()