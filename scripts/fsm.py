#! /usr/bin/env python

import actionlib
import roslib
import rospy
from rospy.impl.tcpros_service import Service, ServiceProxy, wait_for_service
import smach
import smach_ros
import time
import random
from datetime import datetime
from geometry_msgs.msg import Point
from ExperimentalRoboticsLab.srv import RandomPlace
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction
import json

reached = False
random_position_client = None

# define state Navigation
class Navigation(smach.State):
    def __init__(self):
        # initialisation function, it should not wait
        smach.State.__init__(self, 
                             outcomes=['navigation', 'investigation'])
        Navigation.before_navigation()
    
    def arrived_to_the_point(msg):
        global reached
        reached = msg.result
    
    def choosing_random_position():
        global random_client
        position = ExperimentalRoboticsLab.msg.PositionGoal()
        rospy.wait_for_service('/random_place_service')
        rnd_place = random_client()
        position.x = rnd_place.x
        position.y = rnd_place.y
        position.theta = rnd_place.theta
        return position

    def before_navigation():
        goal = Navigation.choosing_random_position()
        random_position_client.send_goal(goal)
        rospy.sleep(5)

    def execute(self, userdata):
        # function called when exiting from the node, it can be blacking
        global reached
        while reached == False:
            time.sleep(5)
        reached = False
        Navigation.before_navigation()
        return 'navigation'
    

# define state Investigation
class Investigation(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation'])

    def execute(self, userdata):
        # simulate that we have to get 5 data samples to compute the outcome
        while not rospy.is_shutdown():  
            time.sleep(1)
            

        

def main():
    global random_position_client, file_path, random_client
    rospy.init_node('fsm')

    random_client = rospy.ServiceProxy('/random_place_service', RandomPlace)
    random_position_client = actionlib.SimpleActionClient("/go_to_point", ExperimentalRoboticsLab.msg.PositionAction)
    rospy.Subscriber('/go_to_point/result', ExperimentalRoboticsLab.msg.PositionActionResult, Navigation.arrived_to_the_point)
    
    
    # Create a SMACH state machine
    fsm = smach.StateMachine(outcomes=['container_interface'])

    # Open the container
    with fsm:
        # Add states to the container
        smach.StateMachine.add('NAVIGATION', Navigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION'})
        smach.StateMachine.add('INVESTIGATION', Investigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION'})
        

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
