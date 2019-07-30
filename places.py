# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:03:49 2019

@author: ayuwoki
"""
from heapq import heappop, heappush
from traveler import  traveler

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
        
    def printPlaces(self,label):
        for h in self.places:
            if h['label']==label:
                return h
        
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
    
    def callObstructVia(self):  #este se llama
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
                if self.adjacentObstruct(d)[ady]: continue
                heappush(Q,(weight,d,ady))
        return path
    
    def adjacentObstruct(self,label):
        adjacent={}
        for h in self.places:
            if h['label']==label:
                for j in h['goingTo']:
                    adjacent[j['label']]=j['obstruction']
        return adjacent
    
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


    def travel(self,origin):
        gold=int(input('Ingresar oro del mochilero: '))
        backpacker=traveler(gold)
        if backpacker.estimate==True:
            print('Oro por debajo del 40% inicial, por favor seleccionar trabajo')
            aux=self.Jobs(origin)
            backpacker.auxHungry+=aux[1]
            backpacker.auxSleep+=aux[1]
            backpacker.gold+=aux[0]
            
        print('valor ',backpacker.auxHungry )
        print('oro', backpacker.gold)
        
        return True
            
            
            
    def Jobs(self,label):
        city=self.returnPlace(label)
        time=0
        gold=0
        auxPrint=''
        c=0
        for h in city['jobs']:
            c+=1
            auxPrint +='\nTrabajos ciudad'+city['label']+ ': ' + 'Presione ({})'.format(c) + h['name'] + ' gain: ' +  str(h['gain']) + ' time: ' + str(h['time'])
        print(auxPrint)
        val=int(input('---> '))
        cant=int(input('cantidad de veces que va a realizar el trabajo --> '))
        time=city['jobs'][val-1]['time']*cant
        gold=city['jobs'][val-1]['gain']*cant
        return gold, time
            
            