#! /usr/bin/env python


## @package ExperimentalRoboticsLab
# \file oracle.py
# \brief node implementing the oracle behavior
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date November 2021
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   /send_hint (ExperimentalRoboticsLab.srv.Hint)
#   /ask_solution (ExperimentalRoboticsLab.srv.TrySolution)
#
# ServiceCline:<BR>
#   None
#
# ActionServer:<BR>
#   None
#
#
# Description:
#
# oracle.py is a script which takes part in the initialization of the 
# environment setting, among the possible ones, the right hypothesis
# Since it is the only one that knows the solution, also it tells the
# robot if it is the right one or not.
##

import rospy
from rospy.core import loginfo
from rospy.impl.tcpros_service import Service, ServiceProxy
import random
from datetime import datetime
from geometry_msgs.msg import Point
import json
from ExperimentalRoboticsLab.srv import Hint
from ExperimentalRoboticsLab.srv import TrySolution
#people=['Col.Mustard', 'Miss.Scarlett', 'Mrs.Peacock', 'Mrs.White', 'Prof.Plum', 'Rev.Green']
#places=['Ballroom', 'Biliard_Room', 'Conservatory', 'Dining_Room', 'Hall', 'Kitchen', 'Library', 'Lounge','Study']
#weapons=['Candlestick', 'Dagger','LeadPipe', 'Revolver', 'Rope', 'Spanner']
## solution saved locally
solution = None
## json which containts all the possible hypotheses
environment_description = None
## number of hints
n_hints = 0
## the id of the solution
solution_complete_of_id = None

## initialization of the environment
def initialization(environment_description):
    """!
    /initialization function
    This function is called at the beginning
    of the program, since it must select one of the possible solutions
    randomly.
    /param environment_description (json)
    """
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

## random_select_type
def random_select_type():
    """!
    /random_select_type it selects a type
    for the generation of the random hint
    also this is done randomly
    """
    integer = random.randint(0,2)
    if integer == 0:
        return "who"
    if integer == 1:
        return "what"
    return "where"

## check_hint
def check_hint(hint, hint_sent):
    """!
    /check_hint function
    It checks if the hint is a well formed hint
    and checks if the hint is already sent
    /return bool
    """
    if len(hint)>0:
        i = 0
        while i<len(hint_sent) and hint_sent[i] is not None:
            if hint["name"] == hint_sent[i]["name"]:
                return False
            i = i + 1
        return True
    return False

## send_hint
def send_hint(req):
    """!
    /send_hint callback
    It is a callback that send a random hint
    among all possible hints
    /param req
    /return hint object (Hint)
    """
    global environment_description
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
    print('\nMaybe ' + hint["name"] + '\n')
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

## check_if_solution_is_correct
def check_if_solution_is_correct(msg):
    """!
    /check_if_solution_is_correct callback
    This function responde to the robot if the solution
    that he sent is correct
    /param msg (string)
    /return bool
    """
    if msg.id == solution_complete_of_id["id"]:
        print ("The solution is correct, congratulations")
        return True
    else:
        print("Try again")
        return False

## main function
def main():
    """!
    /main function
    This function initialize the oracle node and 
    gets the environment description which describes all the hypotheses
    """
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