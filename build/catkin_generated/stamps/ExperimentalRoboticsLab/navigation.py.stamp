#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point
import math
import time
import actionlib
import ExperimentalRoboticsLab.msg

## goal positions are mapped as Points
goal_pos = Point()
actual_position = Point()
sub_target = None
result = ExperimentalRoboticsLab.msg.PositionResult()



def go_to_point(msg):
    global actual_position, action_position
    #print('Received the goal')
    goal_pos.x = msg.x
    goal_pos.y = msg.y
    distance = math.sqrt(pow(goal_pos.x-actual_position.x, 2)+pow(goal_pos.y-actual_position.y, 2))
    #print('\nWaiting for reaching the target')
    time.sleep(distance * 0.5)
    actual_position.x = goal_pos.x
    actual_position.y = goal_pos.y
    action_position.set_succeeded(result)

def main():
    global actual_position, action_position
    rospy.init_node('navigation') 
    action_position = actionlib.SimpleActionServer('/go_to_point', ExperimentalRoboticsLab.msg.PositionAction, execute_cb = go_to_point, auto_start=False)
    action_position.start()
    actual_position.x = 0
    actual_position.y = 0
    rospy.spin()

if __name__ == '__main__':
    main()