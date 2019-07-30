# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:03:49 2019

@author: ayuwoki
"""
from heapq import heappop, heappush

class places:
    places=None
    
    def __init__(self,city,transports):
        self.places=city
        self.transport=transports
    
    def adjacent(self,label):
        adjacent={}
        for h in self.places:
            if h['label']==label:
                for j in h['goingTo']:
                    adjacent[j['label']]=j['travelDistance']
        return adjacent
                
        
        
    def printTransport(self):
        print('Transportes:  ',self.transport ,"\n")
        
    def printPlaces(self):
        print('Lugares:  ', self.places[0]) #solo imprime el primer lugar
        
    def returnPlace(self,label):        #retorna los datos de la ciudad que tenga ese label
        for h in self.places:
            if h['label']==label:
                return h
    def returnMinTime(self,label):
        for h in self.places:
            if h['label']==label:
                return h['minTimeHere']
            
    def returnPosition(self,label):
        for h in self.places:
            if h['label']==label:
                return h['posX'],h['posY']
        
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
            
            
    def returnGoldByKm(self,km,idTransport):  #retorna la cantidad de oro que se cobra por kms
        if idTransport >=1 and idTransport<=3:
            res=0
            for h in self.transport:
                if h['id']==idTransport:
                    res=km*h['valueByKm']
            return res
        return 0
    
    def returnTimeByKm(self,km,idTransport):  #retorna la cantidad de time que se cobra por kms
        if idTransport >=1 and idTransport<=3:
            res=0
            for h in self.transport:
                if h['id']==idTransport:
                    res=km*h['timeByKm']
            return res
        return 0
    
    def prim_mst(self,origin):  #hace el prim y retorna un diccionario con el camino
        v,path=[],{}
        Q=[(0,None,origin)]
        while Q:
            weight,o,d=heappop(Q)
            if d in v:
                continue
            v.append(d)
            if o is None:
                pass
            elif o in path:
               # print('hola')
                path[d]=[o,weight]
            else:
                #print('hola x2')
                path[o]=[d,weight]
            for ady, weight in self.adjacent(d).items():
                heappush(Q,(weight,d,ady))
        return path
    
    def longWayWithGold(self,origin,gold,idTransport): #mira la mayor cantidad de lugares visitables posibles de pendiendo del oro que tenga
        path={}                                        #Este es el que se llama
        aux=self.prim_mst(origin)
        for h in aux:
            if gold > self.returnGoldByKm(aux[h][1],idTransport):
                print('pruebita ',self.returnGoldByKm(aux[h][1],idTransport))
                gold-=self.returnGoldByKm(aux[h][1],idTransport)
                path[h]=aux[h]
            else:
                return path
        return path
                
    def longWayWithTime(self,origin,time,idTransport): #mira la mayor cantidad de lugares visitables posibles de pendiendo del timepo que tenga
        path={}                                        #Este es el que se llama
        aux=self.prim_mst(origin)
        for h in aux:
            if time > self.returnTimeByKm(aux[h][1],idTransport):
                print('pruebita tiempo ',self.returnTimeByKm(aux[h][1],idTransport))
                time-=self.returnTimeByKm(aux[h][1],idTransport)
                path[h]=aux[h]
            else:
                return path
        return path
    
    
    def prueba(self):
        buscar='A'
        for h in self.places:
            for j in h['goingTo']:
                if buscar == j['label']:
                    print(h['posY'])
    

       