#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file investigation.py
# \brief node implementing the investigation part of the robot
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date 15/05/2022
# \details
#
# Publishes to:<BR>
#   None
#
# ServiceServer:<BR>
#   /investigate (ExperimentalRoboticsLab.srv.Investigate)
#
# ServiceCline:<BR>
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
# if it get them, it send it to the node it asked for them
# 
# 
##

import rospy
from ExperimentalRoboticsLab.srv import Hint
from ExperimentalRoboticsLab.srv import Reasoner, ReasonerRequest
from ExperimentalRoboticsLab.srv import Investigate, InvestigateResponse
from ExperimentalRoboticsLab.msg import ErlOracle
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

## Global variables
reasoner_client = None
weapons = []
persons = []
places = []
hypotheses = []
tried_hypotheses = []

available_person = {"missScarlett", "colonelMustard", "mrsWhite", "mrGreen", "mrsPeacock", "profPlum"}
available_weapon = {"candlestick", "dagger", "leadPipe", "revolver", "rope", "spanner"}
available_place = {"conservatory", "lounge", "kitchen", "library", "hall", "study", "bathroom", "diningRoom", "billiardRoom"}
available_key = {"who", "what", "where"}
## Function that check if an person with the value given exists
def check_value_person(value):
    """!
        /def check_value_person function
        The function returns true if the value is an
        admissible person value
        /param value (string)
        /return bool
        """
    for i in available_person:
        if i==value:
            return True
    return False
## Function that check if a weapon with the value given exists
def check_value_weapon(value):
    """!
        /def check_value_weapon function
        The function returns true if the value is an
        admissible weapon value
        /param value (string)
        /return bool
        """
    for i in available_weapon:
        if i==value:
            return True
    return False
## Function that check if a place with the value given exists
def check_value_place(value):
    """!
        /def check_value_place function
        The function returns true if the value is an
        admissible place value
        /param value (string)
        /return bool
        """
    for i in available_place:
        if i==value:
            return True
    return False
## Function that check if an object with the value given exists
def check_values(value):
    """!
        /def check_values function
        The function returns true if the value is an
        admissible value
        /param value (string)
        /return bool
        """
    b = check_value_person(value) or check_value_weapon(value) or check_value_place(value)
    return b
## Function that check if the key is correct
def check_key(value):
    """!
        /def check_key function
        The function returns true if the value is an
        admissible key value
        /param value (string)
        /return bool
        """
    for i in available_key:
        if i==value:
            return True
    return False
## Function that check if an weapon with the value given already exists
def check_weapon_exists(w):
    """!
        /def check_key function
        The function returns true if the value equal to
        an existing weapon value
        /param value (string)
        /return bool
        """
    if len(weapons)==0:
        return False
    for i in weapons:
        if i==w:
            return True
    return False
## Function that check if an person with the value given already exists
def check_people_exists(p):
    """!
        /def check_key function
        The function returns true if the value equal to
        an existing person value
        /param value (string)
        /return bool
        """
    if len(persons)==0:
        return False
    for i in persons:
        if i==p:
            return True
    return False
## Function that check if a place with the value given already exists
def check_place_exists(p):
    """!
        /def check_key function
        The function returns true if the value equal to
        an existing place value
        /param value (string)
        /return bool
        """
    if len(places)==0:
        return False
    for i in places:
        if i==p:
            return True
    return False
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
        /return weapon object({id,value})
        """
    res = []
    for i in weapons:
        if i['ID'] == hyp_id:
            res.append(i['value'])
    return res
## Function that gets the persons with id
def get_persons_with_id(hyp_id):
    """!
        /get_persons_with_id function
        It gets the persons from the local list with id
        identical to hyp_id
        /param hyp_id (string)
        /return person object ({id, value})
        """
    res = []
    for i in persons:
        if i['ID'] == hyp_id:
            res.append(i['value'])
    return res
## Function that gets the places with id
def get_places_with_id(hyp_id):
    """!
        /get_places_with_id function
        It gets the places from the local list with id
        identical to hyp_id
        /param hyp_id (string)
        /return place object ({id,value})
        """
    res = []
    for i in places:
        if i['ID'] == hyp_id:
            res.append(i['value'])
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
## Add person in armor
def add_person(msg):
    """!
    /add_person function
    The function adds to armor the person defined in the message
    /param msg ({ID, value, key})
    """
    global reasoner_client
    print(msg.ID)
    print(msg.value)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.id
    req.type = msg.type
    req.value = msg.value
    res = reasoner_client(req)
    if res == False:
        return False
    
    persons.append({
        'value':msg.value,
        'ID': msg.ID
        })
    return res
## Add weapon in armor
def add_weapon(msg):
    """!
    /add_weapon function
    The function adds to armor the weapon defined in the message
    /param msg ({id, value, key})
    """
    global reasoner_client
    print(msg.ID)
    print(msg.value)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.id
    req.type = msg.type
    req.value = msg.value
    res = reasoner_client(req)
    if res == False:
        return False
    weapons.append({
        'value':msg.value,
        'ID': msg.ID
        })
    return res
## Add place in armor
def add_place(msg):
    """!
    /add_place function
    The function adds to armor the place defined in the message
    /param msg ({ID, value, key})
    """
    global reasoner_client
    print(msg.ID)
    print(msg.value)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.id
    req.type = msg.type
    req.value = msg.value
    res = reasoner_client(req)
    if res == False:
        return False
    places.append({
        'value':msg.value,
        'ID': msg.ID
        })
    return res
## Add a new ind
def add_hint(msg):
    """!
    /add_hint callback
    The function manages the add function in armor
    /param msg ({ID, value, key})
    """
    global weapons, persons, places
    manage_add_hint_wrt_hypothesis(msg.ID)
    if msg.ID<0 or msg.ID>6 or (not(check_key(msg.key))) or (not(check_values(msg.value))):
        return False
    if msg.key == "who":
        if check_people_exists(msg.value):
            return True
        return add_person(msg)
    if msg.key == "where":
        if check_place_exists(msg.value):
            return True
        return add_place(msg)
    if msg.key == "what":
        if check_weapon_exists(msg.value):
            return True
        return add_weapon(msg)
    
    return True
## Query complete hypotheses   
def query_hp_completeness():
    """!
    /query_hp_completeness function
    The function retrieves a list of complete hypotheses
    /return list of complete hypotheses
    """
    global reasoner_client
    req = ReasonerRequest()
    req.func = "query_complete"
    res = reasoner_client(req)
    if res == False:
        return False
    queried = res.ids
    return queried
## Query inconsistent hypotheses
def query_hp_inconsistent():
    """!
    /query_hp_inconsistent function
    The function retrieves a list of inconsistent hypotheses
    /return list of inconsistent hypotheses
    """
    global reasoner_client
    req = ReasonerRequest()
    req.func = "query_inconsistent"
    res = reasoner_client(req)
    if res == False:
        return False
    queried = res.ids
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
## Investigate
def investigate(msg):
    """!
    /investigate callback
    This function ask for a hint, add the hint to armor,
    gets consistent hypotheses, adds consistent hypotheses which have
    not been taken into account before and returns it to the client
    /param msg ()
    /returns True
    """
    global tried_hypotheses
    complete_hps = retrieve_consistent_hp()
    IDs = []
    if complete_hps == []:
        return []
    for i in complete_hps:
        id = i.split('#')[1]
        id = id.split('>')[0]
        print(id)
        #file_hypotheses = create_json_hypothesis(id, file_hypotheses)
        IDs.append(int(id))  
    if msg.investigate:
        for i in tried_hypotheses:
            for j in IDs:
                if i==j:
                    IDs.remove(j)
        for i in IDs:
            tried_hypotheses.append(i)
    res = InvestigateResponse(IDs)
    print(res)
    #file_hypotheses_string = json.dumps(file_hypotheses)
    #rospy.set_param('/consistent_hypotheses', file_hypotheses_string)
    return res
## oracle hint callback
def oracle_hint(msg):
    """!
    /oracle hint function
    This function is a callback for get oracle hint
    """
    print(msg)
    add_hint(msg)
    return True
## Main
def main():
    """!
    /main function
    The function represents the initialization of the node
    where armor clients is initialized and also hint client
    and investigate service are initialized.
    """
    global  hint_client, reasoner_client
    rospy.init_node('investigation') 
    reasoner_client = rospy.ServiceProxy("/reasoner", Reasoner)
    hint_client = rospy.ServiceProxy('/send_hint', Hint)
    investigate_service = rospy.Service('/investigate', Investigate, investigate)
    oracle_hint_sub = rospy.Subscriber('/oracle_hint', ErlOracle, oracle_hint)

    

    rospy.spin()

if __name__ == '__main__':
    main()
    