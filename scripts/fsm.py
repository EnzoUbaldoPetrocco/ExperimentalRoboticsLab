#! /usr/bin/env python

import actionlib
import roslib
import rospy
from rospy.impl.tcpros_service import Service, ServiceProxy
import smach
import smach_ros
import time
import random
from datetime import datetime
from geometry_msgs.msg import Point
from os.path import dirname, realpath
from armor_client import ArmorClient
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction

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
        position = ExperimentalRoboticsLab.msg.PositionGoal()
        position.x = 5*random.random()
        position.y = 5*random.random()
        position.theta = 0
        return position

    def before_navigation():
        goal = Navigation.choosing_random_position()
        random_position_client.send_goal(goal)
        rospy.sleep(1)

    def execute(self, userdata):
        # function called when exiting from the node, it can be blacking
        global reached
        while reached == False:
            time.sleep(1)
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
    global random_position_client
    rospy.init_node('fsm')

    random_position_client = actionlib.SimpleActionClient("/go_to_point", ExperimentalRoboticsLab.msg.PositionAction)
    rospy.Subscriber('/go_to_point/result', ExperimentalRoboticsLab.msg.PositionActionResult, Navigation.arrived_to_the_point)
    # getting path to file
    file_path = dirname(realpath(__file__))
    file_path_size = len(file_path)
    # cutting scripts part which contains 7 character and replacing it with cluedo_ontology.owl
    ontology_path = file_path[:file_path_size-7]+"cluedo_ontology.owl"
    armor_client = ArmorClient("client", "reference")
    armor_client.utils.load_ref_from_file(ontology_path, "http://www.emarolab.it/cluedo-ontology",
                                True, "PELLET", True)  # initializing with buffered manipulation and reasoning
    armor_client.utils.mount_on_ref()
    
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
