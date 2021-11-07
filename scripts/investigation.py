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
    print('\nweapons')
    print(weapons)
    for i in weapons:
        print('\ni')
        print(i)
        if i['id'] == hyp_id:
            res.append(i['name'])
    return res

def get_persons_with_id(hyp_id):
    print('\get persons with id')
    res = []
    for i in persons:
        if i['id'] == hyp_id:
            res.append(i['name'])
    return res

def get_places_with_id(hyp_id):
    res = []
    for i in places:
        if i['id'] == hyp_id:
            res.append(i['name'])
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
        print(hypotheses)


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

def reason():
    armor_client.call("REASON", "", "", [])

# Add a new ind
def add_hint(msg):
    global weapons, persons, places
    print("\nadd hint")
    print(msg)
    manage_add_hint_wrt_hypothesis(msg.id)
    reason()
    if msg.id=='' or msg.id=="" or msg.name=='' or msg.name=="":
        return False
    if msg.type == "who":
        return add_person(msg)
    if msg.type == "where":
        return add_place(msg)
    if msg.type == "what":
        return add_weapon(msg)
    reason()
    #add_hypothesis(msg.id)
    return True
   
def query_hp_completeness():
    query = armor_client.call("QUERY", "IND", "CLASS", ['COMPLETED'])
    queried = query.queried_objects
    return queried

def query_hp_inconsistent():
    query = armor_client.call("QUERY", "IND", "CLASS", ['INCONSISTENT'])
    queried = query.queried_objects
    return queried

def retrieve_consistent_hp():
    print('\nretrieve consistent hp')
    complete_hps = []
    complete_hps = query_hp_completeness()
    print('\n complete hps')
    print(complete_hps)
    if complete_hps == []:
        return complete_hps
    inconsistent_hps = query_hp_inconsistent()
    print('\ninconsistent hps')
    print(inconsistent_hps)
    if inconsistent_hps == []:
        return complete_hps
    for i in complete_hps:
        for j in inconsistent_hps:
            if i == j:
                complete_hps.remove(i)
    print('\ncomplete hps final')
    print(complete_hps)
    return complete_hps

def retrieve_hypothesis(id):
    object = {'id': '','where' : '', 'what': '', 'who': '' }
    weap = get_weapons_with_id(id)
    print('\nweap')
    print(weap)
    pla = get_places_with_id(id)
    per = get_persons_with_id(id)
    if len(weap)==1 and len(pla)==1 and len(per)==1:
        object = {
            'id': id,
            'where' : pla[0],
            'what' : weap[0],
            'who' : per[0]
        }
    return object
        

def create_json_hypothesis(id, file):
    print('\ncreate_json_hypothesis')
    print('file: ')
    print(file)
    print('\nhypotheses ')
    print(file['hypotheses'])
    for i in file['hypotheses']:
        print('\ncreate_json_hypothesis')
        print(i)
        if i['id'] == id:
            return file
    hp_object_to_append = retrieve_hypothesis(id)
    print('hp_object_to_append')
    print(hp_object_to_append)
    hypotheses = file['hypotheses']
    hypotheses.append(hp_object_to_append)
    file['hypotheses'] = hypotheses
    return file

def investigate(msg):
    print('\nInvestigating...')
    rospy.wait_for_service('/send_hint')
    hint = hint_client()
    add_hint(hint)
    # TODO: write in the file the consistent hypotheses
    file_hypotheses_string = rospy.get_param('/consistent_hypotheses')
    file_hypotheses = json.loads(file_hypotheses_string)
    complete_hps = retrieve_consistent_hp()
    if complete_hps == []:
        print('\nconsistent hypotheses list is empty')
        return True
    for i in complete_hps:
        print(i)
        id = i.split('#')[1][:3]
        print(id)
        file_hypotheses = create_json_hypothesis(id, file_hypotheses)
        print(file_hypotheses)
    
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
    