#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \investigation.py
# \brief node implementing the investigation part of the robot
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date November 2021
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   /investigate (ExperimentalRoboticsLab.srv.Investigate)
#
# ServiceCline:<BR>
#   /armor_client (Armor client is given through armor_api_scripts)
#   /send_hint (ExperimentalRoboticsLab.srv.Hint)
#
# ActionServer:<BR>
#   None
#
#
# Description:
#
# investigate.py is a script which manages the communication between the
# armor client and the robot. 
# It asks the oracle for a hint and then reason in order to get complete hypotheses,
# if it get them, it writes them in a file: 'consistent_hypotheses.json'
# 
# 
##

import rospy
from geometry_msgs.msg import Point
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
from armor_client import ArmorClient
#from armor_py_api.scripts.armor_api.armor_client import ArmorClient

## Global variables
armor_client = None
weapons = []
persons = []
places = []
hypotheses = []

## Function that check if an hypothesis does not exists
def check_hypothesis_not_exist(hyp_id):
    """!
        /check_hypothesis_not_exist function
        The function returns true if an hypothesis has been added to the
        local list previously or not
        /param hyp_id (string)
        /return bool
        """
    if hypotheses == []:
        return True
    for i in hypotheses:
        if i == hyp_id:
            return False
    return True
## Function that gets the weapons with id
def get_weapons_with_id(hyp_id):
    """!
        /get_weapons_with_id function
        It gets the weapons from the local list with id
        identical to hyp_id
        /param hyp_id (string)
        /return weapon object({id,name})
        """
    res = []
    for i in weapons:
        if i['id'] == hyp_id:
            res.append(i['name'])
    return res
## Function that gets the persons with id
def get_persons_with_id(hyp_id):
    """!
        /get_persons_with_id function
        It gets the persons from the local list with id
        identical to hyp_id
        /param hyp_id (string)
        /return person object ({id, name})
        """
    res = []
    for i in persons:
        if i['id'] == hyp_id:
            res.append(i['name'])
    return res
## Function that gets the places with id
def get_places_with_id(hyp_id):
    """!
        /get_places_with_id function
        It gets the places from the local list with id
        identical to hyp_id
        /param hyp_id (string)
        /return place object ({id,name})
        """
    res = []
    for i in places:
        if i['id'] == hyp_id:
            res.append(i['name'])
    return res
## Manage add hint function w.r.t. hypothesis 
def manage_add_hint_wrt_hypothesis(hyp_id):
    """!
    /manage_add_hint_wrt_hypothesis function
    if an hypothesis does not exists it appends the name
    to the local list
    /param hyp_id (string)
    """
    global hypotheses
    if check_hypothesis_not_exist(hyp_id):
        hypotheses.append(hyp_id)
## Disjoint person in armor
def disjoint_person(ind):
    """!
    /disjoint_person
    The function tells armor that this ind is different
    from any other ind of the same class
    /param ind (armor ind object)
    """
    res = None
    for i in persons:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res
## Disjoint weapon in armor
def disjoint_weapon(ind):
    """!
    /disjoint_weapon function
    The function tells armor that this ind is different
    from any other ind of the same class
    /param ind (armor ind object)
    """
    res = None
    for i in weapons:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res
## Disjoint place in armor
def disjoint_place(ind):
    """!
    /disjoint_weapon function
    The function tells armor that this ind is different
    from any other ind of the same class
    /param ind (armor ind object)
    """
    res = None
    for i in places:
        res = armor_client.call("DISJOINT", "IND", "", [ind, i['name']])
    return res
## Add person in armor
def add_person(msg):
    """!
    /add_person function
    The function adds to armor the person defined in the message
    /param msg ({id, name, type})
    """
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
## Add weapon in armor
def add_weapon(msg):
    """!
    /add_weapon function
    The function adds to armor the weapon defined in the message
    /param msg ({id, name, type})
    """
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
## Add place in armor
def add_place(msg):
    """!
    /add_place function
    The function adds to armor the place defined in the message
    /param msg ({id, name, type})
    """
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
## Reason function
def reason():
    """!
    /reason function
    The function calls reason armor client function
    """
    armor_client.call("REASON", "", "", [])

## Add a new ind
def add_hint(msg):
    """!
    /add_hint callback
    The function manages the add function in armor
    /param msg ({id, name, type})
    """
    global weapons, persons, places
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
    return True
## Query complete hypotheses   
def query_hp_completeness():
    """!
    /query_hp_completeness function
    The function retrieves a list of complete hypotheses
    /return list of complete hypotheses
    """
    query = armor_client.call("QUERY", "IND", "CLASS", ['COMPLETED'])
    queried = query.queried_objects
    return queried
## Query inconsistent hypotheses
def query_hp_inconsistent():
    """!
    /query_hp_inconsistent function
    The function retrieves a list of inconsistent hypotheses
    /return list of inconsistent hypotheses
    """
    query = armor_client.call("QUERY", "IND", "CLASS", ['INCONSISTENT'])
    queried = query.queried_objects
    return queried
## Retrieve consistent hypothesis
def retrieve_consistent_hp():
    """!
    /query_hp_consistent function
    The function retrieves a list of consistent hypotheses
    and writes them in the file
    /return list of consistent hypotheses
    """
    complete_hps = []
    complete_hps = query_hp_completeness()
    if complete_hps == []:
        return complete_hps
    inconsistent_hps = query_hp_inconsistent()
    if inconsistent_hps == []:
        return complete_hps
    for i in complete_hps:
        for j in inconsistent_hps:
            if i == j:
                complete_hps.remove(i)
    return complete_hps
## Retrieve hypothesis
def retrieve_hypothesis(id):
    """!
    /retrieve_hypothesis function
    The function retrieves an integer hypothesis with
    a specific id
    /param id (string)
    /return hypothesis object ({id,where,what,who,tried})
    """
    object = {'id': '','where' : '', 'what': '', 'who': '' }
    weap = get_weapons_with_id(id)
    pla = get_places_with_id(id)
    per = get_persons_with_id(id)
    if len(weap)==1 and len(pla)==1 and len(per)==1:
        object = {
            'id': id,
            'where' : pla[0],
            'what' : weap[0],
            'who' : per[0],
            'tried' : False
        }
    return object   
## Create json hypothesis
def create_json_hypothesis(id, file):
    """!
    /create_json_hypothesis function
    Create the json hypothesis from the file
    /param id (string)
    /param file (file object)
    /return file
    """
    for i in file['hypotheses']:
        if i['id'] == id:
            return file
    hp_object_to_append = retrieve_hypothesis(id)
    hypotheses = file['hypotheses']
    hypotheses.append(hp_object_to_append)
    file['hypotheses'] = hypotheses
    return file
## Investigate
def investigate(msg):
    """!
    /investigate callback
    This function ask for a hint, add the hint to armor,
    gets consistent hypotheses, adds consistent hypotheses which have
    not been taken into account before and set them into a json file
    /param msg ()
    /returns True
    """
    rospy.wait_for_service('/send_hint')
    hint = hint_client()
    add_hint(hint)
    # TODO: write in the file the consistent hypotheses
    file_hypotheses_string = rospy.get_param('/consistent_hypotheses')
    file_hypotheses = json.loads(file_hypotheses_string)
    complete_hps = retrieve_consistent_hp()
    if complete_hps == []:
        return True
    for i in complete_hps:
        id = i.split('#')[1][:3]
        file_hypotheses = create_json_hypothesis(id, file_hypotheses)
    
    file_hypotheses_string = json.dumps(file_hypotheses)
    rospy.set_param('/consistent_hypotheses', file_hypotheses_string)
    return True
## Main
def main():
    """!
    /main function
    The function represents the initialization of the node
    where armor clients is initialized and also hint client
    and investigate service are initialized.
    """
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
    