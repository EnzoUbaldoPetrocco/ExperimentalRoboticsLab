#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point
import random
from datetime import datetime
import math
from math import pi
import time
import actionlib
import ExperimentalRoboticsLab.msg
from ExperimentalRoboticsLab.srv import RandomPlace

places=[{'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi }, {'name' : 'Biliard Room', 'x':5 , 'y':2, 'theta': pi/2 },
{'name' : 'Conservatory', 'x':5 , 'y':5, 'theta': pi/3 }, {'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi/4 },
{'name' : 'Dining Room', 'x':-5 , 'y':0,  'theta': pi/5 }, {'name' : 'Ballroom', 'x':0 , 'y':5, 'theta': pi/6 },
{'name' : 'Hall', 'x':0 , 'y':-5, 'theta': pi/9 }, {'name' : 'Kitchen', 'x':-5 , 'y':5, 'theta': pi/10 },
{'name' : 'Library', 'x':5 , 'y':-1, 'theta': -pi/2 }, {'name' : 'Lounge', 'x':-5 , 'y':-5, 'theta': -pi },
{'name' : 'Study', 'x':5 , 'y':-5, 'theta': -2*pi }]


def random_place(msg):
    random.seed(datetime.now())
    index = random.randint(0,len(places)-1)
    res = {
        'x':places[index]['x'],
        'y': places[index]['y'],
        'name': places[index]['name'],
        'theta': places[index]['theta']
    }
    return res

def main():
    global actual_position, action_position
    rospy.init_node('random_place') 
    random_place_service = rospy.Service('/random_place_service', RandomPlace, random_place)
    rospy.spin()

if __name__ == '__main__':
    main()