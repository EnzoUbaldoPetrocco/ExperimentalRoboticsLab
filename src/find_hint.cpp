/**
* \file find_hint.cpp
* \brief move arm action
* \author Enzo Ubaldo Petrocco
* \version 1.0
* \date 15/05/2022
*
* Publisher : <BR>
*    /replan
* ActionClient : <BR>
*    /hint
*
* Description :
*
* move the robot cluedo link until it reaches the marker
*
*/
#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <rosplan_interface/find_hint.h>
#include <ExperimentalRoboticsLab/PositionAction.h>
#include <ExperimentalRoboticsLab/HintAction.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <ExperimentalRoboticsLab/Replan.h>
#include <std_msgs/String.h>
#include <ExperimentalRoboticsLab/CustomTargetAction.h>


// Global Variables
ros::Publisher replan_pub;

// Interface that implements FindHint PDDL action
namespace KCL_rosplan {
  FindHintActionInterface::FindHintActionInterface(ros::NodeHandle &nh) {
  ROS_INFO("FindHintActionInterface initialized");
  }
  bool FindHintActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // Here the implementation of the action
    std::cout << "Reaching cluedo_joint target position in order to find the hint. " << std::endl;
    
    // Here we need to move the arm to goal position, we can do 2 attempts because there exist 2 possible locations
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::HintAction> ac("/hint", true);
    ExperimentalRoboticsLab::HintGoal goal;
    ac.waitForServer();
    goal.pose = "marker_under";
    std::cout << "Goal defined " << std::endl;
    ac.sendGoal(goal);
    ac.waitForResult();
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
      ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
       return true;
    }
    else {
      goal.pose = "marker_upper";
      ac.sendGoal(goal);
      ac.waitForResult();
      if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
      ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
       return true;
      }
      else{
      ROS_INFO("Action (%s) failed: replanning!", msg->name.c_str());
      std_msgs::String message;
      message.data = msg->parameters[0].value;
      replan_pub.publish(message);
      return false;
      }
    }
  }
}

// In the main here we initialize the action interface and the replan published
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_find_hint", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 100 );
KCL_rosplan::FindHintActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}