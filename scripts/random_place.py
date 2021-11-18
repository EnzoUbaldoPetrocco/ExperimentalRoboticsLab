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
#   /random_place_service (ExperimentalRoboticsLab.srv.RandomPlace)
#
# ServiceCline:<BR>
#   None
#
# ActionServer:<BR>
#   None
#
#
# Description:
#
# random_place.py is a scripts that
# simply generates a random place (x,y,theta),
# which will become the new robot target.
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
places=[{'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi }, {'name' : 'Biliard Room', 'x':5 , 'y':2, 'theta': pi/2 },
{'name' : 'Conservatory', 'x':5 , 'y':5, 'theta': pi/3 }, {'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi/4 },
{'name' : 'Dining Room', 'x':-5 , 'y':0,  'theta': pi/5 }, {'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi/6 },
{'name' : 'Hall', 'x':0 , 'y':-5, 'theta': pi/9 }, {'name' : 'Kitchen', 'x':-5 , 'y':5, 'theta': pi/10 },
{'name' : 'Library', 'x':5 , 'y':-1, 'theta': -pi/2 }, {'name' : 'Lounge', 'x':-5 , 'y':-5, 'theta': -pi },
{'name' : 'Study', 'x':5 , 'y':-5, 'theta': -2*pi }]

## random_place
def random_place(msg):
    """!
    /random_place callback
    This callback simply select a random index,
    using this it returns a Pose (x,y,theta)
    """
    random.seed(datetime.now())
    index = random.randint(0,len(places)-1)
    res = {
        'x':places[index]['x'],
        'y': places[index]['y'],
        'name': places[index]['name'],
        'theta': places[index]['theta']
    }
    return res

## main
def main():
    """!
    /main function
    This function initialize the node and the 
    random_place_service
    """
    global actual_position, action_position
    rospy.init_node('random_place') 
    random_place_service = rospy.Service('/random_place_service', RandomPlace, random_place)
    rospy.spin()

if __name__ == '__main__':
    main()