#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point
import random
from datetime import datetime
import math
import time
import actionlib
import ExperimentalRoboticsLab.msg
from ExperimentalRoboticsLab.srv import RandomPlace

places=[{'name' : 'Ballroom', 'x':0 , 'y':5 }, {'name' : 'Biliard Room', 'x':5 , 'y':2 },
{'name' : 'Conservatory', 'x':5 , 'y':5 }, {'name' : 'Ballroom', 'x':0 , 'y':5 },
{'name' : 'Dining Room', 'x':-5 , 'y':0 }, {'name' : 'Ballroom', 'x':0 , 'y':5 },
{'name' : 'Hall', 'x':0 , 'y':-5 }, {'name' : 'Kitchen', 'x':-5 , 'y':5 },
{'name' : 'Library', 'x':5 , 'y':-1 }, {'name' : 'Lounge', 'x':-5 , 'y':-5 },
{'name' : 'Study', 'x':5 , 'y':-5 }]


def random_place(msg):
    random.seed(datetime.now())
    index = random.randint(0,len(places)-1)
    res = {
        'x':places[index]['x'],
        'y': places[index]['y'],
        'name': places[index]['name']
    }
    return res

def main():
    global actual_position, action_position
    rospy.init_node('random_place') 
    random_place_service = rospy.Service('/random_place_service', RandomPlace, random_place)
    rospy.spin()

if __name__ == '__main__':
    main()