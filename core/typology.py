# -*- coding: utf-8 -*-
"""
class definition
"""

class resident:
    number_resident=0
    def __init__(self, id_resident, parameter_resident_1):
        self.id_resident=id_resident
        resident.number_resident +=1
        self.parameter_resident_1=parameter_resident_1

class room:
    number_room=0
    def __init__(self,id_room,list_id_resident, parameter_room_1):
        self.id_room = id_room
        room.number_room+=1
        self.list_id_resident=list_id_resident
        self.parameter_room_1=parameter_room_1

class grouping:
    number_grouping=0
    def __init__(self,id_grouping,list_id_room):
        grouping.id_grouping=id_grouping
        grouping.number_grouping+=1
        self.size=len(list_id_room)
        self.list_id_room=list_id_room

class building:
    number_building=0
    def __init__(self, id_buildint, list_id_grouping):
        building.id_buildint=id_buildint
        building.list_id_grouping=list_id_grouping

class residence:
    def __init__(self, list_id_room):
        residence.list_id_rooming=list_id_room


        
        


