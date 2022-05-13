/**
* \file my_moveit.cpp
* \brief move arm node
* \author Enzo Ubaldo Petrocco
* \version 1.0
* \date 15/05/2022
*
* ActionServer : <BR>
*    /hint
* ActionServer : <BR>
*    /custom_pose
* Subscriber: <BR>
*   /oracle_hint
*
* Description :
* This node manages the actual arm movement in order to reach a custom pose,
* or to reach a given pose
*
**/

#include <ros/ros.h>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/robot_model_loader/robot_model_loader.h>
#include <moveit/robot_model/robot_model.h>
#include <moveit/robot_state/robot_state.h>
#include <string.h>
#include <ExperimentalRoboticsLab/ErlOracle.h>
#include <ExperimentalRoboticsLab/FindHint.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <actionlib/server/simple_action_server.h>
#include <ExperimentalRoboticsLab/HintAction.h>
#include <ExperimentalRoboticsLab/HintActionResult.h>
#include <ExperimentalRoboticsLab/CustomTargetAction.h>
#include <ExperimentalRoboticsLab/CustomTargetActionResult.h>

// Global Variables
std::vector<ExperimentalRoboticsLab::ErlOracle> oracle_msgs;

/**
 * MyMoveIt is the class that implements the interface 
 * between moveit and the game implementation.
 * 
 **/
class MyMoveIt{
  public:
  /// members
  bool found;
  actionlib::SimpleActionServer<ExperimentalRoboticsLab::HintAction> sub_find_hint;
  actionlib::SimpleActionServer<ExperimentalRoboticsLab::CustomTargetAction> sub_custom_pose;
  ros::NodeHandle nh;
  /// methods
  MyMoveIt(ros::NodeHandle nh);
  void move_to_the_pose(geometry_msgs::Pose pose);
  void move_to_custom_pose(std::string str);
  void hint_found(const ExperimentalRoboticsLab::ErlOracle::ConstPtr& msg);
  void custom_pose_clbk(const ExperimentalRoboticsLab::CustomTargetGoalConstPtr& msg);
  void find_hint(const ExperimentalRoboticsLab::HintGoalConstPtr& msg);
};
/// Constructor of the class, where it initialize the subscriber to the actions, and the essential for moveit.
MyMoveIt::MyMoveIt(ros::NodeHandle nh):
sub_find_hint(nh, "/hint", boost::bind(&MyMoveIt::find_hint, this, _1 ), false),
sub_custom_pose(nh, "/custom_pose", boost::bind(&MyMoveIt::custom_pose_clbk, this, _1 ), false)
{
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();

}
/// This is simply a callback for using the function move_to_custom_pose. Since it is not trivial this function
/// is used, then it has been preferred to discouple them. 
void MyMoveIt::custom_pose_clbk(const ExperimentalRoboticsLab::CustomTargetGoalConstPtr& msg){
  this->move_to_custom_pose(msg->pose);
  
    sub_custom_pose.setSucceeded();
   
  
};
/// When the hint is found, a boolean variable is set to true
void MyMoveIt::hint_found(const ExperimentalRoboticsLab::ErlOracle::ConstPtr& msg){
  ROS_INFO("Hint found");
  this->found = true;
};
/// This is simply a callback for using the function move_to_custom_pose. Since it is not trivial this function
/// is used, then it has been preferred to discouple them. If the hint is found, the action succeed.
void MyMoveIt::find_hint(const ExperimentalRoboticsLab::HintGoalConstPtr& msg){
  
  this->move_to_custom_pose(msg->pose);
  sleep(2);
  if(found == true){
    sub_find_hint.setSucceeded();
    found = false;
  }
  else{
    sub_find_hint.setAborted();
  }
}
/// This function implements the custom arm pose management
void MyMoveIt::move_to_custom_pose(std::string str){
  ROS_INFO("MyMoveIt::move_to_custom_pose"); 
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();
  group.setStartStateToCurrentState();
	group.setNamedTarget(str);
  
  group.setGoalOrientationTolerance(0.1);
  group.setGoalPositionTolerance(0.1);

	group.move();  
  sleep(1);
};
/// Thanks to this function a user can tell to the robot the pose the cluedo_link must reach
void MyMoveIt::move_to_the_pose(geometry_msgs::Pose pose){
  ROS_INFO("MyMoveIt::move_to_the_pose");
  
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();

  group.setStartStateToCurrentState();
  group.setApproximateJointValueTarget(pose, "cluedo_link");
  std::vector<double> joint_values;
  double timeout = 1;
  bool found_ik = kinematic_state->setFromIK(joint_model_group, pose, timeout);

  if (found_ik)
  {
    kinematic_state->copyJointGroupPositions(joint_model_group, joint_values);
    for (std::size_t i = 0; i < joint_names.size(); ++i)
    {
      ROS_INFO("Joint %s: %f", joint_names[i].c_str(), joint_values[i]);
    }
  }
  else
  {
    ROS_INFO("Did not find IK solution");
  }
  group.setJointValueTarget(joint_values);
  group.setStartStateToCurrentState();
  group.setGoalOrientationTolerance(3.14*2);
  group.setGoalPositionTolerance(0.2);

  // Plan and execute
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  group.plan(my_plan); 
  group.execute(my_plan);
  sleep(1);
};
///Main function where a subscriber to the oracle hint, the node, nodehandle and servers are initialized
int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_moveit");
  ros::NodeHandle nh;
  MyMoveIt move_it(nh);
  ros::Subscriber sub_oracle_hint = nh.subscribe("/oracle_hint", 10, &MyMoveIt::hint_found, &move_it );
  move_it.sub_find_hint.start();
  move_it.sub_custom_pose.start();
  ros::spin();

  return 0;
}
