#! /usr/bin/env python

## @package ExperimentalRoboticsLab
# \file investigation.py
# \brief node implementing the investigation part of the robot
# \author  Enzo Ubaldo Petrocco
# \version 1.0
# \date 15/05/2022
# \details
#
# ServiceServer:<BR>
#   /reasoner (ExperimentalRoboticsLab.srv.Reasoner)
#
#
# Description:
#
# reasoner.py is a script which implements the reasoner part of the 
# algorithm. Since it is a 'custom' reasoner, it is implemented a custom
# hypothesis class and a reasoner class which creates a list of hypotheses
# and reasoner about them
# 
##

import rospy
from ExperimentalRoboticsLab.srv import ReasonerResponse, Reasoner

## Hypothesis class
class Hypothesis:
    def __init__(self, id="", person="", weapon="", place=""):
        """!
        /__init__ function of Hypothesis class
        It initialize the Hypothesis class.
        Hypothesis is composed by and id, a list of weapon, a list of
        places a list of people.
        """
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
    ## people exist check
    def people_exist(self):
        """!
        /people_exist function of Hypothesis class.
        This function check if an hypothesis contains people
        """
        if len(self.people)>0:
            return True
        return False
    ## places exist check
    def places_exist(self):
        """!
        /places_exist function of Hypothesis class.
        This function check if an hypothesis contains places
        """
        if len(self.places)>0:
            return True
        return False
    ## weapons exist check
    def weapons_exist(self):
        """!
        /weapons_exist function of Hypothesis class.
        This function check if an hypothesis contains weapons
        """
        if len(self.weapons)>0:
            return True
        return False
    ## completed check
    def is_completed(self):
        """!
        /is_completed function of Hypothesis class.
        This function check if an hypothesis is completed. This happens
        when people, places and weapons list have at least one element.
        """
        if len(self.people)>0 and len(self.places)>0 and len(self.weapons)>0:
            return True
        return False
    ## inconsistent check
    def is_inconsistent(self):
        """!
        /is_inconsistent function of Hypothesis class.
        This function check if an hypothesis is inconsistent. This
        happens when a least one among people, places and weapons
        have more than one element
        """
        if len(self.people)>1 or len(self.places)>1 or len(self.weapons)>1:
            return True
        return False
    ## add place function
    def add_place(self, place):
        """!
        /add_place function of Hypothesis class.
        This function adds a place in the places list
        /param place (string)
        """
        self.places.append(place)
    ## add weapon function
    def add_weapon(self, weapon):
        """!
        /add_weapon function of Hypothesis class.
        This function adds a weapon in the weapons list
        /param weapon (string)
        """
        self.weapons.append(weapon)
    ## add person function
    def add_person(self, person):
        """!
        /add_person function of Hypothesis class.
        This function adds a person in the people list
        /param person (string)
        """
        self.people.append(person)
## ReasonerClass class
class ReasonerClass:
    def __init__(self):
        """!
        /__init__ function of ReasonerClass class.
        This function initialize the ReasonerClass class, it creates
        a list of six Hypotheses since the possible hypotheses in this program
        are six.
        """
        self.hints = []
        for i in range(6):
            hint = Hypothesis(i)
            self.hints.append(hint)
    ## add hint function
    def add_hint(self, id, value, type):
        """!
        /add_hint function of ReasonerClass class.
        This function adds an hint in the respective Hypothesis.
        Note that an hint could be a weapon, a place or a person. So for
        every hint type it has been created a custom function.
        /param id (int)
        /param value (string)
        /param type (string)
        """
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
    ## wuery inconsistent hypotheses
    def query_inconsistent(self):
        """!
        /query_inconsistent function of ReasonerClass class.
        This function retrieves the inconsistent hypotheses
        among the Hypotheses list.
        """
        res = []
        for i in self.hints:
            if i.is_inconsistent():
                res.append(i.id)
        return res
    ## query complete hypotheses
    def query_completed(self):
        """!
        /query_completed function of ReasonerClass class.
        This function queries complete hypotheses of the 
        Hypotheses list.
        """
        res = []
        for i in self.hints:
            if i.is_completed():
                res.append(i.id)
        return res   
    ## reasoner callback
    def reasoner_clbk(self,msg):
        """!
        /reasoner_clbk function of ReasonerClass class.
        This function manages the action that can be performed
        by the reasoner.
        Among them we have: 
            - add: it adds a hint to an Hypothesis;
            - query_inconsistent: it queries inconsistent Hypothesis
            - query_completed: it queries completed Hypothesis
        /param msg (ReasonerRequest)
        /return res (ReasonerResponse)
        """
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
    The function initialize the reasoner node, ReasonerClass and
    reasoner server.
    """
    rospy.init_node('reasoner')
    reasoner = ReasonerClass()
    reasoner_server = rospy.Service("/reasoner", Reasoner, reasoner.reasoner_clbk)

        
    rospy.spin()

if __name__ == '__main__':
    main()
    