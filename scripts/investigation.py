#! /usr/bin/env python

import roslib
import rospy
from geometry_msgs.msg import Point
import math
import time
import actionlib
import ExperimentalRoboticsLab.msg
from ExperimentalRoboticsLab.srv import Hint
from ExperimentalRoboticsLab.srv import Investigate
import json
from os.path import dirname, realpath
import sys
# getting path to file
file_path = dirname(realpath(__file__))
file_path_size = len(file_path)
package_directory = file_path[:file_path_size-7]
# cutting scripts part which contains 7 character and replacing it with cluedo_ontology.owl
ontology_path = package_directory+"cluedo_ontology.owl"
src_directory = package_directory[:len(package_directory)-len("ExperimentalRoboticsLab")-1]
armor_api_path = src_directory+ "armor_py_api/scripts/armor_api"
sys.path.append(armor_api_path)
print(armor_api_path)
from armor_client import ArmorClient
#from armor_py_api.scripts.armor_api.armor_client import ArmorClient


armor_client = None
weapons = []
persons = []
places = []
hypotheses = []

def check_hypothesis_not_exist(hyp_id):
    if hypotheses == []:
        return True
    for i in hypotheses:
        if i == hyp_id:
            return False
    return True

def get_weapons_with_id(hyp_id):
    res = []
    for i in weapons:
        if i['id'] == hyp_id:
            res.append[i['name']]
    return res

def get_persons_with_id(hyp_id):
    res = []
    for i in persons:
        if i['id'] == hyp_id:
            res.append[i['name']]
    return res

def get_places_with_id(hyp_id):
    res = []
    for i in places:
        if i['id'] == hyp_id:
            res.append[i['name']]
    return res

def add_hypothesis(hyp_id):
    weapons_id = get_weapons_with_id(hyp_id)
    persons_id = get_persons_with_id(hyp_id)
    places_id = get_places_with_id(hyp_id)
    for i in weapons_id:
        armor_client.call('ADD', 'OBJECTPROP', 'IND', ['what',hyp_id,i])
    for i in persons_id:
        armor_client.call('ADD', 'OBJECTPROP', 'IND', ['who',hyp_id,i])
    for i in places_id:
        armor_client.call('ADD', 'OBJECTPROP', 'IND', ['what',hyp_id,i])
    

def manage_add_hint_wrt_hypothesis(hyp_id):
    global hypotheses
    if check_hypothesis_not_exist(hyp_id):
        hypotheses.append(hyp_id)


def disjoint_person(ind):
    res = None
    for i in persons:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res

def disjoint_weapon(ind):
    res = None
    for i in weapons:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res

def disjoint_place(ind):
    res = None
    for i in places:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res

def add_person(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["who", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "PERSON"])
    if res == False:
        return False
    res = disjoint_person(msg.name)
    persons.append({
        'name':msg.name,
        'id': msg.id
        })
    return res

def add_weapon(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["what", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "WEAPON"])
    if res == False:
        return False
    res = disjoint_weapon(msg.name)
    weapons.append({
        'name':msg.name,
        'id': msg.id
        })
    return res

def add_place(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["where", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "PLACE"])
    if res == False:
        return False
    res = disjoint_place(msg.name)
    places.append({
        'name':msg.name,
        'id': msg.id
        })
    return res

# Add a new ind
def add_hint(msg):
    global weapons, persons, places
    print("add hint")
    print(msg)
    manage_add_hint_wrt_hypothesis(msg.id)
    if msg.id=='' or msg.id=="" or msg.name=='' or msg.name=="":
        return False
    if msg.type == "who":
        return add_person(msg)
    if msg.type == "where":
        return add_place(msg)
    if msg.type == "what":
        return add_weapon(msg)
    armor_client.call("REASON", "", "", [])
    add_hypothesis(msg.id)
    return True
   
def query_hp_completeness():
    query = armor_client.call("QUERY", "IND", "CLASS", ['COMPLETED'])
    print(query)
    return query

def query_hp_inconsistent():
    query = armor_client.call("QUERY", "IND", "CLASS", ['INCONSISTENT'])
    print(query)
    return query

def retrieve_consistent_hp():
    complete_hps = []
    complete_hps = query_hp_completeness().queried_objects
    print(complete_hps)
    if complete_hps == []:
        return complete_hps
    inconsistent_hps = query_hp_inconsistent().queried_objects
    print(inconsistent_hps)
    for i in complete_hps:
        for j in inconsistent_hps:
            if i == j:
                complete_hps.remove(i)
    return complete_hps

def investigate(msg):
    print('\nInvestigating...')
    rospy.wait_for_service('/send_hint')
    hint = hint_client()
    add_hint(hint)
    # TODO: write in the file the consistent hypotheses
    file_hypotheses_string = rospy.get_param('/consistent_hypotheses')
    file_hypotheses = json.loads(file_hypotheses_string)
    complete_hps = retrieve_consistent_hp()
    for i in complete_hps:
        print(i)
    
    file_hypotheses_string = json.dumps(file_hypotheses)
    rospy.set_param('/consistent_hypotheses', file_hypotheses_string)

    #res = {
    #    "id" : "",
    #    "where" : "",
    #    "who" : "", 
    #    "what" : ""
    #}
    return True

def main():
    global armor_client, hint_client
    rospy.init_node('investigation') 
    armor_client = ArmorClient("client", "reference")
    armor_client.utils.load_ref_from_file(ontology_path, "http://www.emarolab.it/cluedo-ontology",
                                True, "PELLET", True)  # initializing with buffered manipulation and reasoning
    armor_client.utils.mount_on_ref()
    armor_client.utils.set_log_to_terminal(True)
    hint_client = rospy.ServiceProxy('/send_hint', Hint)
    investigate_service = rospy.Service('/investigate', Investigate, investigate)
    rospy.spin()


if __name__ == '__main__':
    main()
    