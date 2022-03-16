#include <ros/ros.h>
#include "rosplan_action_interface/RPActionInterface.h"

namespace KCL_rosplan {
	
	class NavigationActionInterface: public RPActionInterface
		{
		private:
		
		public:
			/* constructor */
			NavigationActionInterface(ros::NodeHandle &nh);
			/* listen to and process action_dispatch topic */
			bool concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg);
    };
}