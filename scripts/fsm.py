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
from ExperimentalRoboticsLab.srv import Investigate
from ExperimentalRoboticsLab.srv import TrySolution
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

    def execute(self, userdata):
        global reached
        goal = Navigation.choosing_random_position()
        random_position_client.send_goal(goal)
        # function called when exiting from the node, it can be blacking
        while reached == False:
            time.sleep(2)
        reached = False
        return 'investigation'
    

# define state Investigation
class Investigation(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle'])

    def execute(self, userdata):
        rospy.wait_for_service('/investigate')
        investigate_client()
        consistent_hypotheses_string = rospy.get_param('consistent_hypotheses')
        consistent_hypotheses_file = json.loads(consistent_hypotheses_string)
        consistent_hypotheses = consistent_hypotheses_file['hypotheses']
        next_step = None
        if len(consistent_hypotheses) == 0:
            next_step = 'navigation'
        else:
            next_step = 'go_to_oracle'
        return next_step

class GoToOracle(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle', 'assert'])

    def position_of_the_oracle():
        position = ExperimentalRoboticsLab.msg.PositionGoal()
        position.x = 0
        position.y = 0
        position.theta = 0
        return position
    def execute(self, userdata):
        global reached
        goal = GoToOracle.position_of_the_oracle() 
        random_position_client.send_goal(goal)
        while reached == False:
            time.sleep(5)
        reached = False
        return 'assert'

class Assert(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['navigation','investigation', 'go_to_oracle', 'assert', 'finished'])

    def execute(self, userdata):
        global reached
        consistent_hypotheses_string = rospy.get_param('consistent_hypotheses')
        consistent_hypotheses_file = json.loads(consistent_hypotheses_string)
        consistent_hypotheses = consistent_hypotheses_file['hypotheses']
        if consistent_hypotheses == []:
            return 'navigation'
        for i in consistent_hypotheses:
            print(i)
            end = ask_solution_client(i['id'], i['who'], i['where'], i['what'])
            print(end)
            if end.found == True:
                return 'finished'
        return 'navigation'
        
class Finished(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['finish'])

    def execute(self, userdata):
        print('\nCongratulations, you won')
        return 'finish'

        

def main():
    global random_position_client, file_path, random_client, investigate_client, ask_solution_client
    rospy.init_node('fsm')

    random_client = rospy.ServiceProxy('/random_place_service', RandomPlace)
    random_position_client = actionlib.SimpleActionClient("/go_to_point", ExperimentalRoboticsLab.msg.PositionAction)
    rospy.Subscriber('/go_to_point/result', ExperimentalRoboticsLab.msg.PositionActionResult, Navigation.arrived_to_the_point)
    investigate_client = rospy.ServiceProxy('/investigate', Investigate)
    ask_solution_client = rospy.ServiceProxy('/ask_solution', TrySolution)
    
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
