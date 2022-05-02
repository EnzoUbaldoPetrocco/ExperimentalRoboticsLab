//#include <unistd.h>
#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <rosplan_interface/reason.h>
#include <ExperimentalRoboticsLab/PositionAction.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <ExperimentalRoboticsLab/Replan.h>
#include <std_msgs/String.h>
#include <ExperimentalRoboticsLab/Investigate.h>

ros::ServiceClient investigate_client;
ros::Publisher replan_pub;
namespace KCL_rosplan {
  ReasonActionInterface::ReasonActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool ReasonActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Reason about the hint. " << std::endl;
    ExperimentalRoboticsLab::Investigate srv;
    if(investigate_client.call(srv)){
      ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
      return true;
    }else{
      std_msgs::String message;
      message.data = msg->parameters[2].value;
      replan_pub.publish(message);
      return false;
    }
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_reason", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 10 );
ros::ServiceClient investigate_client = nh.serviceClient<ExperimentalRoboticsLab::Investigate>("/investigate");
KCL_rosplan::ReasonActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}