//#include <unistd.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <rosplan_interface/my_action_interface.h>
#include <ExperimentalRoboticsLab/PositionAction.h>

namespace KCL_rosplan {
  MyActionInterface::MyActionInterface(ros::NodeHandle &nh) {
    // here the initialization

  }
  bool MyActionInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
    // here the implementation of the action
    std::cout << "Reaching cluedo_joint position in order to find the hint. " << std::endl;
    
    
    ROS_INFO("Action (%s) performed: completed!", msg->name.c_str());
    return true;
  }
}

///This node move the robot to the correct waypoint
int main(int argc, char **argv) {
ros::init(argc, argv, "rosplan_interface_find_hint", ros::init_options::AnonymousName);
ros::NodeHandle nh("~");
KCL_rosplan::MyActionInterface my_aci(nh);
my_aci.runActionInterface();
return 0;
}