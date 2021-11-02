#!/usr/bin/env python3

import actionlib
import roslib
import rospy
from rospy.impl.tcpros_service import Service, ServiceProxy
import time
import random
from datetime import datetime
from geometry_msgs.msg import Point
from os.path import dirname, realpath
from armor_client import ArmorClient
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction
import json

#people=['Col.Mustard', 'Miss.Scarlett', 'Mrs.Peacock', 'Mrs.White', 'Prof.Plum', 'Rev.Green']
#places=['Ballroom', 'Biliard_Room', 'Conservatory', 'Dining_Room', 'Hall', 'Kitchen', 'Library', 'Lounge','Study']
#weapons=['Candlestick', 'Dagger','LeadPipe', 'Revolver', 'Rope', 'Spanner']
solution = None

def main():
    global random_position_client, solution
    rospy.init_node('oracle')

    # getting path to file
    file_path = dirname(realpath(__file__))
    file_path_size = len(file_path)
    # cutting scripts part which contains 7 character and replacing it with cluedo_ontology.owl
    ontology_path = file_path[:file_path_size-7]+"cluedo_ontology.owl"
    armor_client = ArmorClient("client", "reference")
    armor_client.utils.load_ref_from_file(ontology_path, "http://www.emarolab.it/cluedo-ontology",
                                True, "PELLET", True)  # initializing with buffered manipulation and reasoning
    armor_client.utils.mount_on_ref()
    
    environment_description = rospy.get_param('/environment_description')
    print(environment_description)
    print('diofa')

    # Wait for ctrl-c to stop the application
    rospy.spin()
   

if __name__ == '__main__':
    main()