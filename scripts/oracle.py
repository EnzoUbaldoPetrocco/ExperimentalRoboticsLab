#! /usr/bin/env python

import actionlib
import roslib
import rospy
from rospy.core import loginfo
from rospy.impl.tcpros_service import Service, ServiceProxy
import smach
import smach_ros
import time
import random
from datetime import datetime
from geometry_msgs.msg import Point
import ExperimentalRoboticsLab.msg
import ExperimentalRoboticsLab.msg._PositionAction
import json
from ExperimentalRoboticsLab.srv import Hint
from ExperimentalRoboticsLab.srv import TrySolution
#people=['Col.Mustard', 'Miss.Scarlett', 'Mrs.Peacock', 'Mrs.White', 'Prof.Plum', 'Rev.Green']
#places=['Ballroom', 'Biliard_Room', 'Conservatory', 'Dining_Room', 'Hall', 'Kitchen', 'Library', 'Lounge','Study']
#weapons=['Candlestick', 'Dagger','LeadPipe', 'Revolver', 'Rope', 'Spanner']
solution = None
environment_description = None
n_hints = 0
solution_complete_of_id = None

def initialization(environment_description):
    global solution, n_hints, solution_complete_of_id

    random.seed(datetime.now())
    completed_solution_found = False
    while completed_solution_found == False:
        index = random.randint(0,len(environment_description)-1)
        index_string = "ID"+ str(index)
        solution = environment_description[index_string]
        #print(solution)
        condition_who = len(solution["who"]) == 1
        condition_where = len(solution["where"]) == 1
        condition_what = len(solution["what"]) == 1
        if condition_where and condition_what and condition_who:
            completed_solution_found = True
        solution_complete_of_id = {
            "id": index_string,
            "solution" : solution
        }
    n_hints = 0
    for i in environment_description:
        for j in environment_description[i]["where"]:
            n_hints = n_hints +1
        for j in environment_description[i]["who"]:
            n_hints = n_hints +1
        for j in environment_description[i]["what"]:
            n_hints = n_hints +1
    #print("\nNumber of hints")
    #print(n_hints)
        
    #print(solution)
    #print("\nA murdered has happened")

def random_select_type():
    integer = random.randint(0,2)
    if integer == 0:
        return "who"
    if integer == 1:
        return "what"
    return "where"

def check_hint(hint, hint_sent):
    if len(hint)>0:
        i = 0
        while i<len(hint_sent) and hint_sent[i] is not None:
            if hint["name"] == hint_sent[i]["name"]:
                return False
            i = i + 1
        return True
    return False

def send_hint(req):
    global environment_description
    print('\nIm in the send hint')
    hint_sent_string = rospy.get_param('/hint_sent')
    hint_sent = json.loads(hint_sent_string)
    hints_sent_list = hint_sent["hints_sent_list"]
    if len(hints_sent_list) == n_hints:
        return {
            "type" : "",
            "name" : "",
            "x" : 0,
            "y" : 0,
            "theta" : 0,
            "id" : ""

        }
    hint_already_sent = False
    while hint_already_sent == False:
        index = random.randint(0,len(environment_description)-1)
        index_string = "ID"+ str(index)
        hypothesis = environment_description[index_string]
        type = random_select_type()
        hints = hypothesis[type]
        if len(hints)>0:
            if len(hints)==1:
                hint = hints[0]
            else:
                hint = hints[random.randint(0, len(hints)-1)]
            if check_hint(hint, hints_sent_list):
                hint_already_sent = True
        #time.sleep(3)
    update_hint = {
        "id" : index_string,
        "name" : hint["name"]
    }
    hints_sent_list.append(update_hint)
    json_stored = {
        "hints_sent_list" : hints_sent_list
    }
    hint_sent_string = json.dumps(json_stored)
    rospy.set_param('/hint_sent', hint_sent_string)
    res = {
        "type" : type,
        "name" : hint["name"],
        "x" : 0,
        "y" : 0,
        "theta" : 0,
        "id" : index_string
    }
    if type == "where":
        res["x"] = hint["x"]
        res["y"] = hint["y"]
        res["theta"] = hint["theta"]
    return res

def check_if_solution_is_correct(msg):
    if msg.id == solution_complete_of_id["id"]:
        print ("The solution is correct, congratulations")
        return True
    else:
        print("Try again")
        return False

def main():
    global random_position_client, solution, environment_description
    rospy.init_node('oracle')
    
    environment_description_string = rospy.get_param('/environment_description')
    environment_description = json.loads(environment_description_string)
    initialization(environment_description)
    
    hint_server = rospy.Service('/send_hint', Hint, send_hint)
    game_server = rospy.Service('/ask_solution', TrySolution ,check_if_solution_is_correct)
    # Wait for ctrl-c to stop the application 
    rospy.spin()
   

if __name__ == '__main__':
    main()