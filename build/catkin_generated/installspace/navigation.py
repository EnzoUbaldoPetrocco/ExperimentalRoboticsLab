#!/usr/bin/env python3

import roslib
import rospy
from geometry_msgs.msg import Point
import math
import time

## goal positions are mapped as Points
goal_pos = Point()
actual_position = Point()
sub_target = None



def go_to_point(msg):
    global actual_position
    goal_pos.x = msg.x
    goal_pos.y = msg.y
    distance = math.sqrt(pow(goal_pos.x-actual_position.x, 2)+pow(goal_pos.y-actual_position.y, 2))
    time.sleep(distance * 0.5)
    actual_position.x = goal_pos.x
    actual_position.y = goal_pos.y
    

def main():
    global actual_position
    rospy.init_node('navigation') 

    actual_position.x = 0
    actual_position.y = 0
    rospy.spin()



if __name__ == '__main__':
    main()