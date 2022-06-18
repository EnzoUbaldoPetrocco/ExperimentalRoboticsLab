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
#   /hyp_details (ExperimentalRoboticsLab.srv.HypDetails)
#   
#
# ServiceClient:<BR>
#   /send_hint (ExperimentalRoboticsLab.srv.Hint)
#   /reasoner (ExperimentalRoboticsLab.srv.Reasoner)
#   
#
# Subscriber:<BR>
#   /marker_id (Int32)
#   /oracle_hint (ExperimentalRoboticsLab.msg.ErlOracle)
#
# Description:
#
# investigate.py is a script which manages the communication between the
# reasoner and the robot. 
# It asks the oracle for a hint and then reason in order to get complete hypotheses,
# if it get them, it send it to the node it asked for them
# 
# 
##
from std_msgs.msg import *
import rospy
from ExperimentalRoboticsLab.srv import Hint
from ExperimentalRoboticsLab.srv import Reasoner, ReasonerRequest
from ExperimentalRoboticsLab.srv import Investigate, InvestigateResponse
from ExperimentalRoboticsLab.msg import ErlOracle
from ExperimentalRoboticsLab.srv import HypDetails , HypDetailsResponse
from geometry_msgs.msg import *
from ExperimentalRoboticsLab.srv import Marker


## Global variables
reasoner_client = None
weapons = []
persons = []
places = []
hypotheses = []
tried_hypotheses = []
marker_received = []

available_person = {"MissScarlett", "ColonelMustard", "MrsWhite", "MrGreen", "MrsPeacock", "ProfPlum"}
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
        /def check_weapon_exists function
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
        /def check_people_exists function
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
        /def check_place_exists function
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
    if a hypothesis does not exists it appends the name
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
    print(msg)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.ID
    req.type = "person"#msg.key
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
    print(msg)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.ID
    req.type = "weapon"#msg.key
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
    print(msg)
    req = ReasonerRequest()
    req.func = "add"
    req.id = msg.ID
    req.type ="place"#msg.key
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
    req.func = "query_completed"
    res = reasoner_client(req)
    if res == False:
        return False
    #queried = res.ids
    queried = []
    for i in res.ids:
        queried.append(i)
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
    This function gets consistent hypotheses, 
    adds consistent hypotheses which have
    not been taken into account before, if the msg.investigate
    bool is True, and returns it to the client
    /param msg ()
    /returns True
    """
    global tried_hypotheses
    complete_hps = retrieve_consistent_hp()
    IDs = []
    if complete_hps == []:
        return []
    for i in complete_hps:
        IDs.append(i)  
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
    /oracle_hint function
    This function is a callback for get oracle hint
    """
    #print(msg)
    add_hint(msg)
    return True
## Acquire marker hint
def acquired_marker_hint_clbk(markerId):
    """!
    /acquired_marker_hint_clbk function
    This function is a callback for get oracle hint
    """
    global marker_received
    if markerId.data>40:
        return
    response = hint_gen_client(markerId.data)
    for i in marker_received:
        if i == response.oracle_hint:
            return
    
    
    marker_received.append(response.oracle_hint)
    print(response.oracle_hint)
    add_hint(response.oracle_hint)

def get_hyp_details(msg):
    """!
    /get_hyp_details function
    This function is a callback for get hypothesis
    information
    """
    who = get_persons_with_id(msg.id)[0]
    what = get_weapons_with_id(msg.id)[0]
    where = get_places_with_id(msg.id)[0]
    res = HypDetailsResponse()
    res.who = who
    res.what = what
    res.where = where
    return res

## Main
def main():
    """!
    /main function
    The function represents the initialization of the node
    where service client and servers are initialized.
    """
    global   reasoner_client, hint_gen_client
    rospy.init_node('investigation') 
    reasoner_client = rospy.ServiceProxy("/reasoner", Reasoner)
    investigate_service = rospy.Service('/investigate', Investigate, investigate)
    oracle_hint_sub = rospy.Subscriber('/oracle_hint', ErlOracle, oracle_hint)
    hint_sub = rospy.Subscriber('/marker_id',Int32, acquired_marker_hint_clbk)
    hint_gen_client = rospy.ServiceProxy("/oracle_hint",Marker)
    get_hyp_info = rospy.Service('/hyp_details', HypDetails, get_hyp_details)

    rospy.spin()

if __name__ == '__main__':
    main()
    