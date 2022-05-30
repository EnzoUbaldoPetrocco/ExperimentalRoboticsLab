#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file navigation.py
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
from nav_msgs.msg import *
from move_base_msgs.msg import *
from tf import transformations
import math
from geometry_msgs.msg import *
import numpy as np 

## goal positions are mapped as Points
goal_pos = Point()
## robot position
robot_pos = Point()
## actual position is mapped as a point
actual_position = Point()
## result is of type PositionResult
result = ExperimentalRoboticsLab.msg.PositionResult()

def euler_dist(point_1,point_2):
	"""
	This function compute the euler distance between two points
	"""
	distance = math.sqrt((point_2.x - point_1.x)**2 + (point_2.y - point_1.y) **2)
	return distance

 
def get_quaternion_from_euler(roll, pitch, yaw):
  """
  Convert an Euler angle to a quaternion.
   
    /param roll: The roll (rotation around x-axis) angle in radians.
    /param pitch: The pitch (rotation around y-axis) angle in radians.
    /param yaw: The yaw (rotation around z-axis) angle in radians.
 
    /return qx, qy, qz, qw: The orientation in quaternion [x,y,z,w] format
  """
  qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
  qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
  qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
  qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
 
  return [qx, qy, qz, qw]

## go_to_point callback 
def go_to_point(msg):
    """!
    /go_to_point callback
    This callback simply waits proportionally to the 
    euclidian distance between start and goal
    /param msg (PositionAction)
    """
    global actual_position, action_position, cmd_vel_pub, robot_pos, move_base_client
    goal_pos.x = msg.x
    goal_pos.y = msg.y
    room_pos=move_base_msgs.msg.MoveBaseActionGoal()
    room_pos.goal.target_pose.header.frame_id = "odom"
    room_pos.goal.target_pose.pose.position.x = msg.x
    room_pos.goal.target_pose.pose.position.y = msg.y
    orientations = get_quaternion_from_euler(0,0,msg.theta)
    room_pos.goal.target_pose.pose.orientation.w = orientations[3]
    
    #
    move_base_client.send_goal(room_pos.goal)
    reached = False
    while reached == False:
        distance = euler_dist(msg, robot_pos)
        if distance <= .15:
            reached = True
            #since probably sherlock has no  perfectly reached the room
            #cancel the goal
            move_base_client.cancel_all_goals()
            #Stop Sherlock
            velocity = Twist()
            velocity.linear.x = 0
            velocity.angular.z = 0
            cmd_vel_pub.publish(velocity)
            time.sleep(.5)
        time.sleep(.1)
    distance = math.sqrt(pow(goal_pos.x-actual_position.x, 2)+pow(goal_pos.y-actual_position.y, 2))
    time.sleep(distance * 0.1)
    actual_position.x = goal_pos.x
    actual_position.y = goal_pos.y
    action_position.set_succeeded(result)

def odom_clbk(odom_msg):
    global robot_pos
    robot_pos = odom_msg.pose.pose.position

## main function
def main():
    """!
    /main function
    This function initialize the node, the 
    simple action server /go_to_point and the initial position
    """
    global actual_position, action_position, cmd_vel_pub, move_base_client
    rospy.init_node('navigation') 
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    odom_sub = rospy.Subscriber('odom', Odometry, odom_clbk)
    action_position = actionlib.SimpleActionServer('/go_to_point', ExperimentalRoboticsLab.msg.PositionAction, execute_cb = go_to_point, auto_start=False)
    move_base_client = actionlib.SimpleActionClient('move_base', move_base_msgs.msg.MoveBaseAction)
    move_base_client.wait_for_server()
    action_position.start()
    print('Navigation node is ready')
    actual_position.x = 0
    actual_position.y = 0
    rospy.spin()

if __name__ == '__main__':
    main()