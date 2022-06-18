#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file random_place.py
# \brief node implementing the oracle behavior
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date November 2021
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   /random_place (ExperimentalRoboticsLab.srv.RandomPlace)
#
# Description:
#
# random_place.py is a script that simply generates
# a random sequence of rooms among selected ones.
##

import rospy
from geometry_msgs.msg import Point
import random
from datetime import datetime
from math import pi
from ExperimentalRoboticsLab.srv import RandomPlace

## Physical description of the possible places
# Note that this is not decoupled from the function itself.
# This mechanisms could be better implemented simply using another file (also
# a prexisting file) which contains this information
places=[{'name' : 'Room1', 'x':-4 , 'y':-3, 'theta': 0 }, {'name' : 'Room2', 'x':-4 , 'y':2, 'theta': 0 },
{'name' : 'Room3', 'x':-4 , 'y':7, 'theta': 0 }, {'name' : 'Room4', 'x':5 , 'y':-7, 'theta': 0 },
{'name' : 'Room5', 'x':5 , 'y':-3,  'theta': 0 }, {'name' : 'Room6', 'x':5 , 'y':1, 'theta': 0 },
{'name' : 'Corridor1', 'x':-1 , 'y':6,  'theta': 0 }, {'name' : 'Corridor2', 'x':0 , 'y':-4, 'theta': 0 },
{'name' : 'Corridor3', 'x':-3 , 'y':-2, 'theta': 0 }, {'name' : 'Corridor4', 'x':1 , 'y':-7, 'theta': 0 }]
## count of the sequence
index = 0

## random_place
def random_place(msg):
    """!
    /random_place callback
    This function returns the next position 
    the robot must achieve. The sequence is in fact a
    circular buffer, so if the robot does not achieve the 
    investigation goal, it continues to try.
    """
    global index, places
    
    res = {
        'x':places[index]['x'],
        'y': places[index]['y'],
        'name': places[index]['name'],
        'theta': places[index]['theta']
    }
    index = index + 1
    if index > (len(places)-1):
        index = 0
    return res

## main
def main():
    """!
    /main function
    This function initialize the node, the 
    random_place_service, and the random sequence of rooms
    """
    global  places, sequence_places, index
    rospy.init_node('random_place') 
    sequence_places = places
    index = 0
    random.seed(datetime.now())
    for i in range(20):
    ## Choosing random sequence, when the callback is called the sequence is performed
        index = random.randint(0,len(places)-1)
        temp_place = sequence_places[index]
        sequence_places.pop(index)
        sequence_places.append(temp_place)

    random_place_service = rospy.Service('/random_place', RandomPlace, random_place)
    rospy.spin()

if __name__ == '__main__':
    main()