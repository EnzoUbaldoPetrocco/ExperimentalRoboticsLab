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
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction
import json

#people=['Col.Mustard', 'Miss.Scarlett', 'Mrs.Peacock', 'Mrs.White', 'Prof.Plum', 'Rev.Green']
#places=['Ballroom', 'Biliard_Room', 'Conservatory', 'Dining_Room', 'Hall', 'Kitchen', 'Library', 'Lounge','Study']
#weapons=['Candlestick', 'Dagger','LeadPipe', 'Revolver', 'Rope', 'Spanner']
solution = None

def initialization(environment_description):
    global solution
    random.seed(datetime.now())
    completed_solution_found = False
    while completed_solution_found == False:
        index = random.randint(0,len(environment_description)-1)
        index_string = "ID"+ str(index)
        solution = environment_description[index_string]
        print(solution)
        condition_who = len(solution["who"]) == 1
        condition_where = len(solution["where"]) == 1
        condition_what = len(solution["what"]) == 1
        if condition_where and condition_what and condition_who:
            completed_solution_found = True
    print(solution)

def main():
    global random_position_client, solution
    rospy.init_node('oracle')
    
    environment_description_string = rospy.get_param('/environment_description')
    environment_description = json.loads(environment_description_string)
    initialization(environment_description)
    

    # Wait for ctrl-c to stop the application
    rospy.spin()
   

if __name__ == '__main__':
    main()