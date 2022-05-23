/**
* \file reason.cpp
* \brief reason action
* \author Enzo Ubaldo Petrocco
* \version 1.0
* \date 15/05/2022
*
* ServiceClient: <BR>
*   /investigate
* Publisher: <BR>
*   /replan
*
* Description :
* This node implements PDDL action/ReasonActionInterface
* where it reason about the hints it received. If there is a consistent hypothesos
* the action succeds.
*
**/
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

// Global Variables
ros::ServiceClient investigate_client;
ros::Publisher replan_pub;

/// ReasonActionInterface PDDL Reason Action implementation 
namespace KCL_rosplan {
  ReasonActionInterface::ReasonActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool ReasonActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Reason about the hint. " << std::endl;
    ExperimentalRoboticsLab::Investigate srv;
    srv.request.investigate = false;
    investigate_client.call(srv);
    
    if(srv.response.IDs.size() > 0 ){
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

///Main initialize node, nodehandle, ReasonActionInterface, replan publisher and investigate client
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_reason", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 100 );
investigate_client = nh.serviceClient<ExperimentalRoboticsLab::Investigate>("/investigate");
KCL_rosplan::ReasonActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}