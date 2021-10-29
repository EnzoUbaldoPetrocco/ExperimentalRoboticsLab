# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ExperimentalRoboticsLab: 7 messages, 0 services")

set(MSG_I_FLAGS "-IExperimentalRoboticsLab:/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ExperimentalRoboticsLab_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" "ExperimentalRoboticsLab/PositionResult:ExperimentalRoboticsLab/PositionActionGoal:actionlib_msgs/GoalID:ExperimentalRoboticsLab/PositionActionResult:ExperimentalRoboticsLab/PositionActionFeedback:ExperimentalRoboticsLab/PositionFeedback:std_msgs/Header:actionlib_msgs/GoalStatus:ExperimentalRoboticsLab/PositionGoal"
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" "actionlib_msgs/GoalID:ExperimentalRoboticsLab/PositionGoal:std_msgs/Header"
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" "actionlib_msgs/GoalStatus:ExperimentalRoboticsLab/PositionResult:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" "actionlib_msgs/GoalStatus:ExperimentalRoboticsLab/PositionFeedback:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" ""
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" ""
)

get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_custom_target(_ExperimentalRoboticsLab_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ExperimentalRoboticsLab" "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg"
  "${MSG_I_FLAGS}"
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_cpp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
)

### Generating Services

### Generating Module File
_generate_module_cpp(ExperimentalRoboticsLab
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ExperimentalRoboticsLab_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ExperimentalRoboticsLab_generate_messages ExperimentalRoboticsLab_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ExperimentalRoboticsLab_gencpp)
add_dependencies(ExperimentalRoboticsLab_gencpp ExperimentalRoboticsLab_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ExperimentalRoboticsLab_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg"
  "${MSG_I_FLAGS}"
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_eus(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
)

### Generating Services

### Generating Module File
_generate_module_eus(ExperimentalRoboticsLab
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ExperimentalRoboticsLab_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ExperimentalRoboticsLab_generate_messages ExperimentalRoboticsLab_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_eus _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ExperimentalRoboticsLab_geneus)
add_dependencies(ExperimentalRoboticsLab_geneus ExperimentalRoboticsLab_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ExperimentalRoboticsLab_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg"
  "${MSG_I_FLAGS}"
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_lisp(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
)

### Generating Services

### Generating Module File
_generate_module_lisp(ExperimentalRoboticsLab
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ExperimentalRoboticsLab_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ExperimentalRoboticsLab_generate_messages ExperimentalRoboticsLab_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ExperimentalRoboticsLab_genlisp)
add_dependencies(ExperimentalRoboticsLab_genlisp ExperimentalRoboticsLab_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ExperimentalRoboticsLab_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg"
  "${MSG_I_FLAGS}"
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_nodejs(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ExperimentalRoboticsLab
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ExperimentalRoboticsLab_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ExperimentalRoboticsLab_generate_messages ExperimentalRoboticsLab_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ExperimentalRoboticsLab_gennodejs)
add_dependencies(ExperimentalRoboticsLab_gennodejs ExperimentalRoboticsLab_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ExperimentalRoboticsLab_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg"
  "${MSG_I_FLAGS}"
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)
_generate_msg_py(ExperimentalRoboticsLab
  "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
)

### Generating Services

### Generating Module File
_generate_module_py(ExperimentalRoboticsLab
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ExperimentalRoboticsLab_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ExperimentalRoboticsLab_generate_messages ExperimentalRoboticsLab_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionAction.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionActionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionGoal.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionResult.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/enzo/Scrivania/ROS_RT2/ros_ws/src/ExperimentalRoboticsLab/build/devel/share/ExperimentalRoboticsLab/msg/PositionFeedback.msg" NAME_WE)
add_dependencies(ExperimentalRoboticsLab_generate_messages_py _ExperimentalRoboticsLab_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ExperimentalRoboticsLab_genpy)
add_dependencies(ExperimentalRoboticsLab_genpy ExperimentalRoboticsLab_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ExperimentalRoboticsLab_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ExperimentalRoboticsLab
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ExperimentalRoboticsLab
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ExperimentalRoboticsLab
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ExperimentalRoboticsLab
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ExperimentalRoboticsLab
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(ExperimentalRoboticsLab_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
