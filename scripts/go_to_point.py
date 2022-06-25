#! /usr/bin/env python
## @package ExperimentalRoboticsLab
# \file go_to_point.py
# \brief node implementing the navigation part of the robot
# \author  Carmine Tommaso Recchiuto, Enzo Ubaldo Petrocco
# \version 1.0
# \date 15/05/2022
# \details
#
# Publishes to:<BR>
#   /cmd_vel
#
# Subscriber:<BR>
#   /odom
#
# ActionServer:<BR>
#   /go_to_point
#
#
# Description:
#
# This node is responsible for navigation algorithm. This algorithm is a 
# naive algorithm, which does not implement obstacle avoidance. So it is 
# performed only in a situation when you do not have obstacles
# 
##


import rospy
import actionlib
import ExperimentalRoboticsLab.msg
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf import transformations
import math



# robot state variables
position_ = Point()
feedback=ExperimentalRoboticsLab.msg.PositionFeedback()
result=ExperimentalRoboticsLab.msg.PositionResult()
yaw_ = 0
state_ = 0
pub_ = None

# parameters for control
yaw_precision_ = math.pi / 9  # +/- 20 degree allowed
yaw_precision_2_ = math.pi / 90  # +/- 2 degree allowed
dist_precision_ = 0.08
kp_a = -2.6
kp_d = 0.7
ub_a = 0.6
lb_a = -0.6
ub_d = 0.6

action=None



def clbk_odom(msg):
    global position_
    global yaw_

    # position
    position_ = msg.pose.pose.position

    # yaw
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = transformations.euler_from_quaternion(quaternion)
    yaw_ = euler[2]

def change_state(state):
    global state_
    state_ = state
    print ('State changed to [%s]' % state_)

def normalize_angle(angle):
    if(math.fabs(angle) > math.pi):
        angle = angle - (2 * math.pi * angle) / (math.fabs(angle))
    return angle

def fix_yaw(des_pos):
    desired_yaw = math.atan2(des_pos.y - position_.y, des_pos.x - position_.x)
    err_yaw = normalize_angle(desired_yaw - yaw_)
    twist_msg = Twist()
    if math.fabs(err_yaw) > yaw_precision_2_:
        twist_msg.angular.z = kp_a*err_yaw
        if twist_msg.angular.z > ub_a:
            twist_msg.angular.z = ub_a
        elif twist_msg.angular.z < lb_a:
            twist_msg.angular.z = lb_a
    pub_.publish(twist_msg)
    # state change conditions
    if math.fabs(err_yaw) <= yaw_precision_2_:
        #print ('Yaw error: [%s]' % err_yaw)
        change_state(1)

def go_straight_ahead(des_pos):
    desired_yaw = math.atan2(des_pos.y - position_.y, des_pos.x - position_.x)
    err_yaw = desired_yaw - yaw_
    err_pos = math.sqrt(pow(des_pos.y - position_.y, 2) +
                        pow(des_pos.x - position_.x, 2))
    err_yaw = normalize_angle(desired_yaw - yaw_)

    if err_pos > dist_precision_:
        twist_msg = Twist()
        twist_msg.linear.x = kp_d
        if twist_msg.linear.x > ub_d:
           twist_msg.linear.x = ub_d

        twist_msg.angular.z = kp_a*err_yaw
        pub_.publish(twist_msg)
    else: # state change conditions
        #print ('Position error: [%s]' % err_pos)
        change_state(2)

    # state change conditions
    if math.fabs(err_yaw) > yaw_precision_:
        #print ('Yaw error: [%s]' % err_yaw)
        change_state(0)

def fix_final_yaw(des_yaw):
    err_yaw = normalize_angle(des_yaw - yaw_)
    twist_msg = Twist()
    if math.fabs(err_yaw) > yaw_precision_2_:
        twist_msg.angular.z = kp_a*err_yaw
        if twist_msg.angular.z > ub_a:
            twist_msg.angular.z = ub_a
        elif twist_msg.angular.z < lb_a:
            twist_msg.angular.z = lb_a
    pub_.publish(twist_msg)
    # state change conditions
    if math.fabs(err_yaw) <= yaw_precision_2_:
        #print ('Yaw error: [%s]' % err_yaw)
        change_state(3)
        
def done():
    twist_msg = Twist()
    twist_msg.linear.x = 0
    twist_msg.angular.z = 0
    pub_.publish(twist_msg)
    
def go_to_point(goal):
    global action, state_
    result=ExperimentalRoboticsLab.msg.PositionResult()
    desired_position = Point()
    desired_position.x = goal.x
    desired_position.y = goal.y
    des_yaw = goal.theta
    change_state(0)
    while True:
        
        if action.is_preempt_requested():
            state_=3

        if state_ == 0:
            fix_yaw(desired_position)
        elif state_ == 1:
            go_straight_ahead(desired_position)
        elif state_ == 2:
            fix_final_yaw(des_yaw)
        elif state_ == 3:
            done()
            break
    action.set_succeeded(result)
    return True

def main():
    global pub_, action
    rospy.init_node('go_to_point')
    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub_odom = rospy.Subscriber('/odom', Odometry, clbk_odom)
    action = actionlib.SimpleActionServer('/go_to_point', ExperimentalRoboticsLab.msg.PositionAction, execute_cb = go_to_point, auto_start=False)
    action.start()
    
    rospy.spin()


if __name__ == '__main__':
    main()