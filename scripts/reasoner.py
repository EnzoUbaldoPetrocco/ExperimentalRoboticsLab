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
# if it get them, it send it to the node it asked for them
# 
# 
##

import rospy
from ExperimentalRoboticsLab.srv import ReasonerResponse, Reasoner

class Hypothesis:
    def __init__(self, id="", person="", weapon="", place=""):
        self.id = id
        self.people = []
        self.weapons = []
        self.places = []
        if person != "":
            self.people.append(person)
        if weapon != "":
            self.weapons.append(weapon)
        if place != "":
            self.places.append(place)
    
    def people_exist(self):
        if len(self.people)>0:
            return True
        return False
    def places_exist(self):
        if len(self.places)>0:
            return True
        return False
    def weapons_exist(self):
        if len(self.weapons)>0:
            return True
        return False
    def is_completed(self):
        if len(self.people)>0 and len(self.places)>0 and len(self.weapons)>0:
            return True
        return False
    def is_inconsistent(self):
        if len(self.people)>1 or len(self.places)>1 or len(self.weapons)>1:
            return True
        return False
    def add_place(self, place):
        self.places.append(place)
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    def add_person(self, person):
        self.people.append(person)

class ReasonerClass:
    def __init__(self):
        self.hints = []
        for i in range(6):
            hint = Hypothesis(i)
            self.hints.append(hint)
    
    def add_hint(self, id, value, type):
        for i in self.hints:
            if i.id == id:
                if type=="weapon":
                    i.add_weapon(value)
                    return True
                if type=="person":
                    i.add_person(value)
                    return True
                if type=="place":
                    i.add_place(value)
                    return True
        return False

    def query_inconsistent(self):
        res = []
        for i in self.hints:
            if i.is_inconsistent():
                res.append(i.id)
        return res
    
    def query_completed(self):
        res = []
        for i in self.hints:
            if i.is_completed():
                res.append(i.id)
        return res   

    def reasoner_clbk(self,msg):
        res = ReasonerResponse()
        res.ids = []
        res.result = False
        if msg.func == "add":
            self.add_hint(msg.id, msg.value, msg.type)
        if msg.func == "query_inconsistent":
            inconsistent = self.query_inconsistent()
            res.ids = inconsistent
        if msg.func == "query_completed":
            completed = self.query_completed()
            res.ids = completed
        print("Reasoner response:")
        print(res)
        return res

        
        


## Main
def main():
    """!
    /main function
    The function represents the initialization of the node
    where armor clients is initialized and also hint client
    and investigate service are initialized.
    """
    rospy.init_node('reasoner')
    reasoner = ReasonerClass()
    reasoner_server = rospy.Service("/reasoner", Reasoner, reasoner.reasoner_clbk)

        
    rospy.spin()

if __name__ == '__main__':
    main()
    