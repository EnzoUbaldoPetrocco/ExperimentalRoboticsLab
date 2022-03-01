#include <ros/ros.h>

// MoveIt
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

std::vector<ExperimentalRoboticsLab::ErlOracle> oracle_msgs;

class MyMoveIt{
  public:
  //members
  bool found;
  //methods
  MyMoveIt();
  void move_to_the_pose(geometry_msgs::Pose pose);
  void move_to_custom_pose(std::string str);
  void hint_found(const ExperimentalRoboticsLab::ErlOracle::ConstPtr& msg);
  void find_hint(const ExperimentalRoboticsLab::FindHint::ConstPtr& msg);
};
void MyMoveIt::hint_found(const ExperimentalRoboticsLab::ErlOracle::ConstPtr& msg){
  this->found = true;
};

void MyMoveIt::find_hint(const ExperimentalRoboticsLab::FindHint::ConstPtr& msg){
  this->move_to_custom_pose("check");
  sleep(10);
  geometry_msgs::Pose pose;
  pose.position.x = msg->x_pos;
  pose.position.y = msg->y_pos;
  pose.position.z = msg->z_pos;
  pose.orientation.x = msg->x_quat;
  pose.orientation.y = msg->y_quat;
  pose.orientation.z = msg->z_quat;
  pose.orientation.w = msg->w_quat;
  this->move_to_the_pose(pose);
  while(this->found == false){
    sleep(1);
  }
  this->found = false;
}


MyMoveIt::MyMoveIt(){
  // We start by instantiating a
  // `RobotModelLoader`_
  // object, which will look up
  // the robot description on the ROS parameter server and construct a
  // :moveit_core:`RobotModel` for us to use.
  //
  // .. _RobotModelLoader:
  //     http://docs.ros.org/noetic/api/moveit_ros_planning/html/classrobot__model__loader_1_1RobotModelLoader.html
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  // Using the :moveit_core:`RobotModel`, we can construct a
  // :moveit_core:`RobotState` that maintains the configuration
  // of the robot. We will set all joints in the state to their
  // default values. We can then get a
  // :moveit_core:`JointModelGroup`, which represents the robot
  // model for a particular group, e.g. the "panda_arm" of the Panda
  // robot.
  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();
}

void MyMoveIt::move_to_custom_pose(std::string str){
  ROS_INFO("MyMoveIt::move_to_custom_pose"); // We start by instantiating a
  // `RobotModelLoader`_
  // object, which will look up
  // the robot description on the ROS parameter server and construct a
  // :moveit_core:`RobotModel` for us to use.
  //
  // .. _RobotModelLoader:
  //     http://docs.ros.org/noetic/api/moveit_ros_planning/html/classrobot__model__loader_1_1RobotModelLoader.html
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  // Using the :moveit_core:`RobotModel`, we can construct a
  // :moveit_core:`RobotState` that maintains the configuration
  // of the robot. We will set all joints in the state to their
  // default values. We can then get a
  // :moveit_core:`JointModelGroup`, which represents the robot
  // model for a particular group, e.g. the "panda_arm" of the Panda
  // robot.
  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();
  group.setStartStateToCurrentState();
	group.setNamedTarget(str);
	group.move();  
};

void MyMoveIt::move_to_the_pose(geometry_msgs::Pose pose){
  ROS_INFO("MyMoveIt::move_to_the_pose");
   // We start by instantiating a
  // `RobotModelLoader`_
  // object, which will look up
  // the robot description on the ROS parameter server and construct a
  // :moveit_core:`RobotModel` for us to use.
  //
  // .. _RobotModelLoader:
  //     http://docs.ros.org/noetic/api/moveit_ros_planning/html/classrobot__model__loader_1_1RobotModelLoader.html
  robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
  const moveit::core::RobotModelPtr& kinematic_model = robot_model_loader.getModel();
  ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());

  // Using the :moveit_core:`RobotModel`, we can construct a
  // :moveit_core:`RobotState` that maintains the configuration
  // of the robot. We will set all joints in the state to their
  // default values. We can then get a
  // :moveit_core:`JointModelGroup`, which represents the robot
  // model for a particular group, e.g. the "panda_arm" of the Panda
  // robot.
  moveit::core::RobotStatePtr kinematic_state(new moveit::core::RobotState(kinematic_model));
  kinematic_state->setToDefaultValues();
  const moveit::core::JointModelGroup* joint_model_group = kinematic_model->getJointModelGroup("arm");
  moveit::planning_interface::MoveGroupInterface group("arm");
  const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();

  // Inverse Kinematics
  // ^^^^^^^^^^^^^^^^^^
  // We can now solve inverse kinematics (IK) for the Panda robot.
  // To solve IK, we will need the following:
  //
  //  * The desired pose of the end-effector 
  //  * The timeout: 0.1 s
  group.setStartStateToCurrentState();
  group.setApproximateJointValueTarget(pose, "cluedo_link");
  std::vector<double> joint_values;
  double timeout = 0.1;
  bool found_ik = kinematic_state->setFromIK(joint_model_group, pose, timeout);

  // Now, we can print out the IK solution (if found):
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
  group.setGoalOrientationTolerance(0.01);
  group.setGoalPositionTolerance(0.01);

  // Plan and execute
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  group.plan(my_plan); 
  group.execute(my_plan);
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_moveit");
  ros::NodeHandle nh;
  MyMoveIt move_it = MyMoveIt();
  ros::Subscriber sub_oracle_hint = nh.subscribe("/oracle_hint", 10, &MyMoveIt::hint_found, &move_it );
  ros::Subscriber sub_find_hint = nh.subscribe("/find_hint", 10, &MyMoveIt::find_hint, &move_it );
  sleep(10);
  ros::AsyncSpinner spinner(1);
  spinner.start();

  ros::shutdown();
  return 0;
}
