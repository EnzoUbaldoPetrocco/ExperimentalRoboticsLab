#! /usr/bin/env python

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

stop = True

class FakeMsg:
    def __init__(self, at):
        self.at = at

def update_knowledge_predicate(is_positive, predicate_name, keys):
    '''Updates state of a predicate of my problem'''
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

def update_knowledge_goal(is_positive, predicate_name,keys):
    '''Add a goal to my problem'''
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
    

def update_knowledge_instance(name,instanceType):
    '''Add a instance to my problem'''
    global update_knowledge_client
    update_req=rosplan_knowledge_msgs.srv.KnowledgeUpdateServiceRequest()
    update_req.update_type=0
    update_req.knowledge.knowledge_type=0
    update_req.knowledge.instance_name=name
    update_req.knowledge.instance_type=instanceType
    result=update_knowledge_client(update_req)

def init_no_same_location():
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

def init_common_predicates():
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

def init_common_goal():
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'game'
    predicate.value = 'gm'
    predicates.append(predicate)
    update_knowledge_goal(True, 'game_finished', predicates)

def initialize_predicates():
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
    
def initialize_instances():
    update_knowledge_instance('marker1','location')
    update_knowledge_instance('marker2','location')
    update_knowledge_instance('oracle','location')
    update_knowledge_instance('nav','navigation_token')
    update_knowledge_instance('hnt','hint')
    update_knowledge_instance('hyp','hypothesis')
    update_knowledge_instance('gm','game')

def initialize_goal():
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker1'
    predicates.append(predicate)
    update_knowledge_goal(True, 'not_at', predicates)
    init_common_goal()

def re_init(msg):
    global clear_knowledge, stop, cancel_dispatch
    #cancel current dispatch
    try:
        ok=cancel_dispatch()
        if ok:
            print('dispatch cancelled')
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


    
    clear_knowledge()
    init_common_goal()
    init_common_predicates()
    initialize_instances()
    init_no_same_location()
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
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker1'
    predicates.append(predicate)
    update_knowledge_goal(True, 'not_at', predicates)
    predicates = []
    predicate = diagnostic_msgs.msg.KeyValue()
    predicate.key= 'loc'
    predicate.value = 'marker1'
    predicates.append(predicate)
    update_knowledge_goal(True, 'not_at', predicates)
    running_rosplan_procedure()

    rospy.spin()

    
def running_rosplan_procedure():
    global prob_gen_client, plan_client, parse_client, dispatch_client
    print("Generating the problem")
    prob_gen_client()
    time.sleep(3)
    print("Calling planning client")
    plan_client()
    time.sleep(3)
    print("Calling plan parsing client")
    parse_client()
    time.sleep(3)
    print("Dispatch the plan")
    try:
        dispatchRes=dispatch_client()
        print(dispatchRes)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
    return True

def print_plan(msg):
    print(msg)

def replan_callback(req):
    """"Callback of replan_service"""
    #cancel current dispatch
    try:
        ok=cancel_dispatch()
        if ok:
            print('dispatch cancelled')
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
    return True



def main():
    global update_knowledge_client, prob_gen_client, plan_client, parse_client, dispatch_client, clear_knowledge, cancel_dispatch, stop
    rospy.init_node('rosplan_management',anonymous=True)
    replan = rospy.Subscriber('/replan', Replan, re_init)

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

    time.sleep(20)
    #rospy.wait_for_service('rosplan_knowledge_base/propositions', 'predicate')
    clear_knowledge()
    time.sleep(3)
    initialize_predicates()
    time.sleep(3)
    initialize_instances()
    time.sleep(3)
    initialize_goal()
    time.sleep(3)
    running_rosplan_procedure()
    
    rospy.spin()


if __name__ == '__main__':
    main()