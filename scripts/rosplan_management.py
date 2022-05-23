#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file rosplan_management.py
# \brief node implementing the rosplan part of the robot
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date 15/05/2022
# \details
#
# Subscriber to:<BR>
#   /rosplan_planner_interface/planner_output
#   /replan
#
# ServiceClient:<BR>
#   rosplan_problem_interface/problem_generation_server
#   rosplan_planner_interface/planning_server
#   rosplan_parsing_interface/parse_plan
#   rosplan_plan_dispatcher/dispatch_plan
#   rosplan_knowledge_base/update
#   rosplan_knowledge_base/clear
#   rosplan_plan_dispatcher/cancel_dispatch
#   
#
#
# Description:
#
# rosplan_management.py that runs the rosplan procedure for planning, replanning
# and problem generating.
# 
# 
##

from matplotlib.style import available
import rospy
import rosplan_dispatch_msgs.srv 
import rosplan_knowledge_msgs.srv
from std_msgs.msg import *
from std_srvs.srv import *
import diagnostic_msgs.msg
from ExperimentalRoboticsLab.srv import *
from ExperimentalRoboticsLab.msg import Replan
import time

## Global variables
stop = True

## update_knowledge_predicate function
def update_knowledge_predicate(is_positive, predicate_name, keys):
    """!
        /def check_value_weapon function
        The function updates state of a predicate of the problem
        /param is_positive (bool), predicate_name (string), keys (object list)
        /return
        """
    global update_knowledge_client
    update_req=rosplan_knowledge_msgs.srv.KnowledgeUpdateServiceRequest()
    update_req.knowledge.is_negative=not(is_positive)
    update_req.update_type=0
    update_req.knowledge.knowledge_type=1
    update_req.knowledge.attribute_name=predicate_name
    for i in keys:
        key_value=diagnostic_msgs.msg.KeyValue()
        key_value.key=i.key
        key_value.value=i.value
        update_req.knowledge.values.append(key_value)
    result=update_knowledge_client(update_req)
## update_knowledge_goal function
def update_knowledge_goal(is_positive, predicate_name,keys):
    """!
        /def check_value_weapon function
        The function adds a goal to the problem
        /param is_positive (bool), predicate_name (string), keys (object list)
        /return
        """
    global update_knowledge_client
    update_req=rosplan_knowledge_msgs.srv.KnowledgeUpdateServiceRequest()
    update_req.knowledge.is_negative=not(is_positive)
    update_req.update_type=1
    update_req.knowledge.knowledge_type=1
    update_req.knowledge.attribute_name=predicate_name
    for i in keys:
        key_value=diagnostic_msgs.msg.KeyValue()
        key_value.key=i.key
        key_value.value=i.value
        update_req.knowledge.values.append(key_value)
    result=update_knowledge_client(update_req) 
## update_knowledge_instance function
def update_knowledge_instance(name,instanceType):
    """!
        /def check_value_weapon function
        The function adds a instance to the problem
        /param name (string), instanceType (string)
        /return
        """
    global update_knowledge_client
    update_req=rosplan_knowledge_msgs.srv.KnowledgeUpdateServiceRequest()
    update_req.update_type=0
    update_req.knowledge.knowledge_type=0
    update_req.knowledge.instance_name=name
    update_req.knowledge.instance_type=instanceType
    result=update_knowledge_client(update_req)
## init_no_same_location function
def init_no_same_location():
    """!
        /def initialize no_same_location predicates
        The function initialize no_same_location predicates
        /param
        /return
        """
    predicates = []
    predicate1 = diagnostic_msgs.msg.KeyValue()
    predicate2 = diagnostic_msgs.msg.KeyValue()
    predicate1.key= 'from'
    predicate1.value = 'marker1'
    predicates.append(predicate1)
    predicate2.key= 'to'
    predicate2.value = 'marker2'
    predicates.append(predicate2)
    update_knowledge_predicate(True, 'no_same_location', predicates)
    predicates = []
    predicate1 = diagnostic_msgs.msg.KeyValue()
    predicate2 = diagnostic_msgs.msg.KeyValue()
    predicate1.key= 'from'
    predicate1.value = 'marker1'
    predicates.append(predicate1)
    predicate2.key= 'to'
    predicate2.value = 'oracle'
    predicates.append(predicate2)
    update_knowledge_predicate(True, 'no_same_location', predicates)
## initial_common_predicates function
def init_common_predicates():
    """!
        /def init_common_predicates
        The function initialize common predicates
        /param 
        /return 
        """
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'navigation_token'
    predicate.value = 'nav'
    predicates.append(predicate)
    update_knowledge_predicate(True, 'proceed_investigate', predicates)
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'oracle'
    predicates.append(predicate)
    update_knowledge_predicate(True, 'is_oracle', predicates)
## initialize_common_goal function
def init_common_goal():
    """!
        /def init_common_goal
        The function initialize common goals
        /param 
        /return
        """
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'game'
    predicate.value = 'gm'
    predicates.append(predicate)
    update_knowledge_goal(True, 'game_finished', predicates)
## initialize_predicates function 
def initialize_predicates():
    """!
        /def initialize_predicates function
        The function initialize predicates
        /param 
        /return
        """
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker1'
    predicates.append(predicate)
    update_knowledge_predicate(True, 'at', predicates)
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker2'
    predicates.append(predicate)
    update_knowledge_predicate(True, 'not_at', predicates)
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'oracle'
    predicates.append(predicate)
    update_knowledge_predicate(True, 'not_at', predicates)
    init_no_same_location()
    init_common_predicates()
## initialize_instances function
def initialize_instances():
    """!
        /def initialize_instances 
        The function updates knowledge instances
        /param 
        /return
        """
    update_knowledge_instance('marker1','location')
    update_knowledge_instance('marker2','location')
    update_knowledge_instance('oracle','location')
    update_knowledge_instance('nav','navigation_token')
    update_knowledge_instance('hnt','hint')
    update_knowledge_instance('hyp','hypothesis')
    update_knowledge_instance('gm','game')
## initialize_goal function
def initialize_goal():
    """!
        /def initialize_goal function
        The function update knowledge goal
        /param 
        /return 
        """
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker1'
    predicates.append(predicate)
    update_knowledge_goal(True, 'not_at', predicates)
    init_common_goal()
 ## running rosplan procedure function
def running_rosplan_procedure():
    """!
        /def running rosplan procedure
        The function generates the problem, calls planning client,
        calls plan parser and tries plan dispatcher
        /param 
        /return dispatchRes response of the plan dispatcher
        """
    global prob_gen_client, plan_client, parse_client, dispatch_client
    print("Generating the problem")
    prob_gen_client()
    time.sleep(4)
    print("Calling planning client")
    plan_client()
    time.sleep(4)
    print("Calling plan parsing client")
    parse_client()
    time.sleep(4)
    print("Dispatch the plan")
    try:
        dispatchRes=dispatch_client()
        print(dispatchRes)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
    return dispatchRes
## print plan callback
def print_plan(msg):
    """!
        /def print plan function
        The function callback simply prints the plan
        /param 
        /return 
        """
    print(msg)
## Callback that cancel current dispatch and returns true if it manages
def replan_callback(req):
    """!
        /def callback of /replan service
        The function returns true if it manages to cancel
        current dispatch
        /param req (Replan.msg)
        /return bool
        """
    #cancel current dispatch
    try:
        ok=cancel_dispatch()
        if ok:
            print('dispatch cancelled')
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    #running_rosplan_procedure()
    return True
## Main Function where services are initialized and infinite loop runs
def main():
    """!
        /def main function
        The function returns if theplan is completed
        /param 
        /return 
        """
    global update_knowledge_client, prob_gen_client, plan_client, parse_client, dispatch_client, clear_knowledge, cancel_dispatch, stop
    rospy.init_node('rosplan_management',anonymous=True)
    replan = rospy.Subscriber('/replan', Replan, replan_callback)

    # Wait for all services
    rospy.wait_for_service('rosplan_problem_interface/problem_generation_server')
    rospy.wait_for_service('rosplan_planner_interface/planning_server')
    rospy.wait_for_service('rosplan_parsing_interface/parse_plan')
    rospy.wait_for_service('rosplan_plan_dispatcher/dispatch_plan')
    rospy.wait_for_service('rosplan_knowledge_base/update')
    rospy.wait_for_service('rosplan_knowledge_base/update')
    rospy.wait_for_service('rosplan_knowledge_base/clear')
    rospy.wait_for_service('/rosplan_plan_dispatcher/cancel_dispatch')

    rospy.Subscriber("/rosplan_planner_interface/planner_output", String, print_plan)

    prob_gen_client=rospy.ServiceProxy('rosplan_problem_interface/problem_generation_server', Empty)  
    plan_client=rospy.ServiceProxy('rosplan_planner_interface/planning_server',Empty) 
    parse_client=rospy.ServiceProxy('rosplan_parsing_interface/parse_plan',Empty)
    dispatch_client=rospy.ServiceProxy('rosplan_plan_dispatcher/dispatch_plan',rosplan_dispatch_msgs.srv.DispatchService) 
    update_knowledge_client=rospy.ServiceProxy('rosplan_knowledge_base/update',rosplan_knowledge_msgs.srv.KnowledgeUpdateService) 
    clear_knowledge=rospy.ServiceProxy('rosplan_knowledge_base/clear',Empty) 
    cancel_dispatch = rospy.ServiceProxy('/rosplan_plan_dispatcher/cancel_dispatch', Empty)

    going_on= True
    time.sleep(15)
    while going_on:
        time.sleep(3)
        #rospy.wait_for_service('rosplan_knowledge_base/propositions', 'predicate')
        clear_knowledge()
        time.sleep(3)
        initialize_instances()
        time.sleep(2)
        initialize_predicates()
        time.sleep(2)
        initialize_goal()
        time.sleep(2)
        response = running_rosplan_procedure()
        if response.goal_achieved:
            print('You won')
            going_on = False
        else:
            print('Keep playing')

if __name__ == '__main__':
    main()