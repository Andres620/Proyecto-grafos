# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:03:49 2019

@author: ayuwoki
"""

class places:
    places=None
    
    def __init__(self,city,transports):
        self.places=city
        self.transport=transports
        
        
    def printTransport(self):
        print('Transportes:  ',self.transport)
        
    def printPlaces(self):
        print('Lugares:  ', self.places[0])