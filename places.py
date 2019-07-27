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
        print('Transportes:  ',self.transport ,"\n")
        
    def printPlaces(self):
        print('Lugares:  ', self.places[0]) #solo imprime el primer lugar
        
    def returnPlace(self,label):        #retorna los datos de la ciudad que tenga ese label
        for h in self.places:
            if h['label']==label:
                return h
        
    def prueba(self):
        buscar='A'
        for h in self.places:
            for j in h['goingTo']:
                if buscar == h['label']:
                    print(h['posY'])

       