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
    def midPoint(self,x1,y1,x2,y2):
        avgX=(x1+x2)/2
        avgY=(y1+y2)/2
        return (avgX,avgY)
    
    def callObstructVia(self):
        origin=input('Ingrese ID del origen: ')
        destination=input('Ingrese ID del destino: ')
        self.obstructVia(origin,destination)
        
    
    def obstructVia(self,origin,destination):  #sirve para obstruir o desobstruir vias
        for h in self.places:
            if h['label']==origin:
                for j in h['goingTo']:
                    if j['label']==destination:
                        j['obstruction']=not j['obstruction']
                        print(j['obstruction'])
                        pass
                pass
        for h in self.places:
            if h['label']==destination:
                for j in h['goingTo']:
                    if j['label']==origin:
                        j['obstruction']=not j['obstruction']
                        print(j['obstruction'])
                        pass
                pass
        
        
    def prueba(self):
        buscar='A'
        for h in self.places:
            for j in h['goingTo']:
                if buscar == j['label']:
                    print(h['posY'])

       