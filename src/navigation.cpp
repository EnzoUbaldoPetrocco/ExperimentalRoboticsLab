//#include <unistd.h>
#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <rosplan_interface/navigation.h>
#include <ExperimentalRoboticsLab/PositionAction.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <ExperimentalRoboticsLab/Replan.h>
#include <std_msgs/String.h>
#include <ExperimentalRoboticsLab/CustomTargetAction.h>
#include <random.h>
ros::Publisher replan_pub;

namespace KCL_rosplan {
  NavigationActionInterface::NavigationActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool NavigationActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Going from: " << msg->parameters[0].value << " to: "<< msg->parameters[1].value << std::endl;
    
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::CustomTargetAction> ac_pose("/custom_pose", true);
    ExperimentalRoboticsLab::CustomTargetGoal goal_pose;
    ac_pose.waitForServer();
    goal_pose.pose = "home";
    ac_pose.sendGoal(goal_pose);
    ac_pose.waitForResult();
  
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::PositionAction> ac("/go_to_point", true);
    ExperimentalRoboticsLab::PositionGoal goal;

    ac.waitForServer();
    int location = rand()%4;
    if(location == 0){
      goal.x = -2.3;
      goal.y = 0; 
      goal.theta = -3.14/2;
    }
    else if (location == 1){
      goal.x = 2.3;
      goal.y = 0; 
      goal.theta = 3.14/2;
    }
    else if (location == 2){
      goal.x = 0; 
      goal.y = 2.3;
      goal.theta = 3.14;
    }
    else if (location == 3){
      goal.x = 0; 
      goal.y = -2.3;
      goal.theta = 0;
    }
    
    //std::cout << "Debug" <<std::endl;
    ac.sendGoal(goal);
    ac.waitForResult();
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
      ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
       return true;
    }
    else {
      std_msgs::String message;
      message.data = msg->parameters[0].value;
      replan_pub.publish(message);
      return false;
    }
    
   
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_navigation", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 100 );
KCL_rosplan::NavigationActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}