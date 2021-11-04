#! /usr/bin/env python

import roslib
import rospy
from geometry_msgs.msg import Point
import math
import time
import actionlib
import ExperimentalRoboticsLab.msg
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



def add_person(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["who", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "PERSON"])
    if res == False:
        return False
    persons.append(msg.name)

def add_weapon(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["what", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "WEAPON"])
    if res == False:
        return False
    weapons.append(msg.name)

def add_place(msg):
    res = armor_client.call("ADD", "OBJECTPROP", "IND", ["where", msg.id, msg.name])
    if res == False:
        return False
    res = armor_client.call("ADD", "IND", "CLASS", [msg.name, "PLACE"])
    if res == False:
        return False
    places.append(msg.name)

# Add a new ind
def add_hint(msg):
    global weapons, persons, places
    if msg.id=='' or msg.id=="" or msg.name=='' or msg.name=="":
        return False
    if msg.type == "who":
        add_person(msg)
    if msg.type == "where":
        add_place(msg)
    if msg.type == "what":
        add_weapon(msg)
    
   
    

def main():
    global armor_client
    rospy.init_node('investigation') 
    armor_client = ArmorClient("client", "reference")
    armor_client.utils.load_ref_from_file(ontology_path, "http://www.emarolab.it/cluedo-ontology",
                                True, "PELLET", True)  # initializing with buffered manipulation and reasoning
    armor_client.utils.mount_on_ref()
    armor_client.utils.set_log_to_terminal(True)
    rospy.spin()


if __name__ == '__main__':
    main()
    