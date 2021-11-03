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

#people=['Col.Mustard', 'Miss.Scarlett', 'Mrs.Peacock', 'Mrs.White', 'Prof.Plum', 'Rev.Green']
#places=['Ballroom', 'Biliard_Room', 'Conservatory', 'Dining_Room', 'Hall', 'Kitchen', 'Library', 'Lounge','Study']
#weapons=['Candlestick', 'Dagger','LeadPipe', 'Revolver', 'Rope', 'Spanner']
solution = None
environment_description = None

def initialization(environment_description):
    global solution
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
    #print('\nIm in the send hint')
    hint_sent_string = rospy.get_param('/hint_sent')
    hint_sent = json.loads(hint_sent_string)
    hints_sent_list = hint_sent["hints_sent_list"]
    hint_already_sent = False
    while hint_already_sent == False:
        #print('\nIm in the while loop of send hint')
        index = random.randint(0,len(environment_description)-1)
        index_string = "ID"+ str(index)
        #print('\nIndex_string: ' + index_string)
        hypothesis = environment_description[index_string]
        #print('\nHypotesis')
        #print(hypothesis)
        type = random_select_type()
        #print('\nType:')
        #print(type)
        hints = hypothesis[type]
        #print('\nHints:')
        #print(hints)
        if len(hints)>0:
            if len(hints)==1:
                hint = hints[0]
            else:
                hint = hints[random.randint(0, len(hints))]
            #print('\nHint:')
            #print(hint)
            if check_hint(hint, hints_sent_list):
                hint_already_sent = True
                #print('\nHint_sent inside if')
        #print(hint_already_sent)
        #print('\nHint_sent')
        #print(hint_already_sent)
        time.sleep(5)
    #print(hint["name"])
    update_hint = {
        "id" : index_string,
        "name" : hint["name"]
    }
    #print("\nupdate_hint: ")
    #print(update_hint)
    hints_sent_list.append(update_hint)
    #print('\nhints_sent_list: ')
    #print(hints_sent_list)
    json_stored = {
        "hints_sent_list" : hints_sent_list
    }
    hint_sent_string = json.dumps(json_stored)
    #print('\nhints_sent_string: ')
    #print(hint_sent_string)
    rospy.set_param('/hint_sent', hint_sent_string)
    #res = Hint(
    #    type= type,
    #    name= hint["name"],
    #    x = 0,
    #    y = 0,
    #    theta = 0
    #)
    res = {
        "type" : type,
        "name" : hint["name"],
        "x" : 0,
        "y" : 0,
        "theta" : 0
    }
    if type == "where":
        #res.x = hint["x"]
        #res.y = hint["y"]
        #res.theta = hint["theta"]
        res["x"] = hint["x"]
        res["y"] = hint["y"]
        res["theta"] = hint["theta"]
    print('\nres')
    print(res)
    return res


def main():
    global random_position_client, solution, environment_description
    rospy.init_node('oracle')
    
    environment_description_string = rospy.get_param('/environment_description')
    environment_description = json.loads(environment_description_string)
    initialization(environment_description)
    
    hint_server = rospy.Service('/send_hint', Hint, send_hint)

    # Wait for ctrl-c to stop the application 
    rospy.spin()
   

if __name__ == '__main__':
    main()