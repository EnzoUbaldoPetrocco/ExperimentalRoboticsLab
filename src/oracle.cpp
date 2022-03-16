//#include <unistd.h>
#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <rosplan_interface/oracle.h>
#include <ExperimentalRoboticsLab/PositionAction.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>

namespace KCL_rosplan {
  OracleActionInterface::OracleActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool OracleActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Oracle relations " << std::endl;
    
    
    ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
    return true;
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_oracle", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
KCL_rosplan::OracleActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}