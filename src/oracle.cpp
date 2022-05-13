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
#include <ExperimentalRoboticsLab/Replan.h>
#include <std_msgs/String.h>
#include <ExperimentalRoboticsLab/Investigate.h>
#include <ExperimentalRoboticsLab/Replan.h>
#include <ExperimentalRoboticsLab/Oracle.h>

ros::Publisher replan_pub;
ros::ServiceClient investigate_client;
ros::ServiceClient oracle_client;


namespace KCL_rosplan {
  OracleActionInterface::OracleActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool OracleActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Oracle relations " << std::endl;
    
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::PositionAction> ac("/go_to_point", true);
    ExperimentalRoboticsLab::PositionGoal goal;
    ac.waitForServer();
    goal.x = 0; 
    goal.y = 0;
    goal.theta = 0;
    ac.sendGoal(goal);
    ac.waitForResult();
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
      ExperimentalRoboticsLab::Investigate srv;
    
      investigate_client.call(srv);
    if(srv.response.IDs.size() > 0 ){

      //Here i ask to the oracle if an ID is correct
      ExperimentalRoboticsLab::Oracle or_srv;
      oracle_client.call(or_srv);
      for(int i=0;i<srv.response.IDs.size()-1;i++){
        if(srv.response.IDs[i]==or_srv.response.ID){
          ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
          return true;
        }
      }
      std_msgs::String message;
      message.data = msg->parameters[2].value;
      replan_pub.publish(message);
      return false;
      
    }
    else{
      std_msgs::String message;
      message.data = msg->parameters[2].value;
      replan_pub.publish(message);
      return false;
    }
    }
    else {
      std_msgs::String message;
      message.data = msg->parameters[2].value;
      replan_pub.publish(message);
      return false;
    }
    
    ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
    return true;
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_oracle", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
KCL_rosplan::OracleActionInterface my_aci(nh);
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 100 );
ros::ServiceClient investigate_client = nh.serviceClient<ExperimentalRoboticsLab::Investigate>("/investigate");
oracle_client = nh.serviceClient<ExperimentalRoboticsLab::Oracle>("/oracle_solution");
my_aci.runActionInterface();
return 0;
}