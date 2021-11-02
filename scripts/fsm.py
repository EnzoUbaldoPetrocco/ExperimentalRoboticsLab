#! /usr/bin/env python

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

def arrived_to_the_point(msg):
    global reached
    reached = msg.result
    

# define state Navigation
class Navigation(smach.State):
    def __init__(self):
        # initialisation function, it should not wait
        smach.State.__init__(self, 
                             outcomes=['navigation', 'investigation'],
                             input_keys=['navigation_counter_in'],
                             output_keys=['navigation_counter_out'])
        
    def execute(self, userdata):
        # function called when exiting from the node, it can be blacking
        time.sleep(5)
        rospy.loginfo('Executing state NAVIGATION (users = %f)'%userdata.navigation_counter_in)
        userdata.navigation_counter_out = userdata.navigation_counter_in + 1
        return 'navigation'
    

# define state Investigation
class Investigation(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation'],
                             input_keys=['investigation_counter_in'],
                             output_keys=['investigation_counter_out'])
        self.sensor_input = 0
        self.rate = rospy.Rate(200)  # Loop at 200 Hz

    def execute(self, userdata):
        # simulate that we have to get 5 data samples to compute the outcome
        while not rospy.is_shutdown():  
            time.sleep(1)
            if self.sensor_input < 5: 
                rospy.loginfo('Executing state INVESTIGATION (users = %f)'%userdata.investigation_counter_in)
                userdata.investigation_counter_out = userdata.investigation_counter_in + 1
                return 'navigation'
            self.sensor_input += 1
            self.rate.sleep

        

def main():
    rospy.init_node('fsm')
    rospy.Subscriber('/go_to_point/result', ExperimentalRoboticsLab.msg.PositionActionResult, arrived_to_the_point)
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
    fsm.userdata.sm_counter = 0

    # Open the container
    with fsm:
        # Add states to the container
        smach.StateMachine.add('NAVIGATION', Navigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION'},
                               remapping={'navigation_counter_in':'sm_counter',
                                          'navigation_counter_out':'sm_counter'})
        smach.StateMachine.add('INVESTIGATION', Investigation(), 
                               transitions={'navigation':'NAVIGATION', 
                                            'investigation':'INVESTIGATION'},
                               remapping={'investigation_counter_in':'sm_counter', 
                                          'investigation_counter_out':'sm_counter'})
        

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
