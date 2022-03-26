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

ros::Publisher replan_pub;

namespace KCL_rosplan {
  NavigationActionInterface::NavigationActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool NavigationActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Going from: " << msg->parameters[0].value << " to: "<< msg->parameters[1].value << std::endl;
    
  
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::PositionAction> ac("/go_to_point", true);
    ExperimentalRoboticsLab::PositionGoal goal;

    ac.waitForServer();
    if(msg->parameters[1].value == "marker1"){
      goal.x = -2.4;
      goal.y = 0.1; //shift dued to the chassis
      goal.theta = 3.14/2;
    }
    else if (msg->parameters[1].value == "marker2"){
      goal.x = 2.4;
      goal.y = 0.1; //shift dued to the chassis
      goal.theta = 3.14/2;
    }
    else if (msg->parameters[1].value == "marker3"){
      goal.x = -0.1; //shift dued to the chassis
      goal.y = 2.4;
      goal.theta = 0;
    }
    else if (msg->parameters[1].value == "marker4"){
      goal.x = -0.1; //shift dued to the chassis
      goal.y = -2.4;
      goal.theta = 0;
    }
    else if (msg->parameters[1].value == "oracle"){
      goal.x = 0;
      goal.y = 0;
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
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 10 );
KCL_rosplan::NavigationActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}