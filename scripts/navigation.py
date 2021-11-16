#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \navigation.py
# \brief node implementing the navigation part of the robot
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date November 2021
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   None
#
# ServiceCline:<BR>
#   None
#
# ActionServer:<BR>
#   /go_to_point (ExperimentalRoboticsLab.msg.PositionAction)
#
#
# Description:
#
# navigation.py is a script which manages the navigation to a point of the robot
# It starts from [0,0], then it goes for the point which has been asked to reached
# when it gets this, it sets 'succeded' to the result
##

import rospy
from geometry_msgs.msg import Point
import math
import time
import actionlib
import ExperimentalRoboticsLab.msg

## goal positions are mapped as Points
goal_pos = Point()
## actual position is mapped as a point
actual_position = Point()
## result is of type PositionResult
result = ExperimentalRoboticsLab.msg.PositionResult()


## go_to_point callback 
def go_to_point(msg):
    """!
    /go_to_point callback
    This callback simply waits proportionally to the 
    euclidian distance between start and goal
    /param msg (PositionAction)
    """
    global actual_position, action_position
    goal_pos.x = msg.x
    goal_pos.y = msg.y
    distance = math.sqrt(pow(goal_pos.x-actual_position.x, 2)+pow(goal_pos.y-actual_position.y, 2))
    time.sleep(distance * 0.1)
    actual_position.x = goal_pos.x
    actual_position.y = goal_pos.y
    action_position.set_succeeded(result)

## main function
def main():
    """!
    /main function
    This function initialize the node, the 
    simple action server /go_to_point and the initial position
    """
    global actual_position, action_position
    rospy.init_node('navigation') 
    action_position = actionlib.SimpleActionServer('/go_to_point', ExperimentalRoboticsLab.msg.PositionAction, execute_cb = go_to_point, auto_start=False)
    action_position.start()
    actual_position.x = 0
    actual_position.y = 0
    rospy.spin()

if __name__ == '__main__':
    main()