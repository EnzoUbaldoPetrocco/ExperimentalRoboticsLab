#!/usr/bin/env python3

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
from armor_py_api.scripts.armor_api.armor_client import ArmorClient

def main():
    rospy.init_node('fsm')
    
    ontology_path = dirname(realpath(__file__))+"cluedo_ontology.owl"
    
    # Wait for ctrl-c to stop the application
    rospy.spin()
    # sis.stop()


if __name__ == '__main__':
    main()
