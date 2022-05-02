//#include <unistd.h>
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

ros::Publisher replan_pub;


ExperimentalRoboticsLab::HintGoal define_goal(ExperimentalRoboticsLab::HintGoal goal ,std::string str, std::float_t altitude){
  ROS_INFO("define goal with certain altitude");
  if(str == "marker1"){
      goal.x_pos = -3.0;
      goal.y_pos = 0.0;
      goal.z_pos = altitude;
      goal.x_quat = 0;
      goal.y_quat = 0;
      goal.z_quat = 0;
      goal.w_quat = 0;
    }
    else if (str == "marker2"){
      goal.x_pos = 3.0;
      goal.y_pos = 0.0;
      goal.z_pos = altitude;
      goal.x_quat = 0;
      goal.y_quat = 0;
      goal.z_quat = 0;
      goal.w_quat = 0;
    }
    else if (str == "marker3"){
      goal.x_pos = 0.0;
      goal.y_pos = 3.0;
      goal.z_pos = altitude;
      goal.x_quat = 0;
      goal.y_quat = 0;
      goal.z_quat = 0;
      goal.w_quat = 0;
    }
    else if (str == "marker4"){
      goal.x_pos = 0.0;
      goal.y_pos = -3.0;
      goal.z_pos = altitude;
      goal.x_quat = 0;
      goal.y_quat = 0;
      goal.z_quat = 0;
      goal.w_quat = 0;
    }
    else if (str == "oracle"){
      goal.x_pos = 0.0;
      goal.y_pos = 0.0;
      goal.z_pos = altitude;
      goal.x_quat = 0;
      goal.y_quat = 0;
      goal.z_quat = 0;
      goal.w_quat = 0;
    }
    return goal;
}

namespace KCL_rosplan {
  FindHintActionInterface::FindHintActionInterface(ros::NodeHandle &nh) {
    // here the initialization
  ROS_INFO("find_hint node initialized");
  }
  bool FindHintActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Reaching cluedo_joint position in order to find the hint. " << std::endl;

    actionlib::SimpleActionClient<ExperimentalRoboticsLab::CustomTargetAction> ac_pose("/custom_pose", true);
    ExperimentalRoboticsLab::CustomTargetGoal goal_pose;
    ac_pose.waitForServer();
    goal_pose.pose = "home";
    ac_pose.sendGoal(goal_pose);
    ac_pose.waitForResult();
    // Here we need to move the arm to goal position, we can do many attempts because there exist 2 possible locations
    actionlib::SimpleActionClient<ExperimentalRoboticsLab::HintAction> ac("/hint", true);
    ExperimentalRoboticsLab::HintGoal goal;
    ac.waitForServer();

    goal = define_goal(goal, msg->parameters[0].value, 0.75);
    std::cout << "Goal defined " << std::endl;
    //std::cout << "Debug" <<std::endl;
    ac.sendGoal(goal);
    ac.waitForResult();
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
      ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
       return true;
    }
    else {
      sleep(1);
      goal = define_goal(goal, msg->parameters[0].value, 1.25);
      sleep(1);
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
    
    // Here we need to get the hint and to reason
    
    ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
    return true;
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_find_hint", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
replan_pub = nh.advertise<ExperimentalRoboticsLab::Replan>("/replan", 10 );
KCL_rosplan::FindHintActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}