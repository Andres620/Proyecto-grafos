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
    
    def returnTranssport(self,idT):
        for h in self.transport:
            if h['id']==idT:
                return h
        
    def printPlaces(self,label):
        for h in self.places:
            if h['label']==label:
                return h
        
    def returnPlace(self,label):        #retorna los datos de la ciudad que tenga ese label
        for h in self.places:
            if h['label']==label:
                return h
    def returnTransportNode(self,origin,destination):        #retorna los datos de la ciudad que tenga ese label
        for h in self.places:
            if h['label']==origin:
                for j in h['goingTo']:
                    if j['label']==destination:
                        return j['transportForms']
    
    def returnTravelDistanceNode(self,origin,destination):        #retorna los datos de la ciudad que tenga ese label
        for h in self.places:
            if h['label']==origin:
                for j in h['goingTo']:
                    if j['label']==destination:
                        return j['travelDistance']
            
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


    def travel(self,origin,backpacker):   #metodo para viajar
        if backpacker.goToEat()==True:
            aux=self.eat(origin)
            backpacker.gold-=aux[0]
            backpacker.timeTravel+=aux[1]
            backpacker.localTime+=aux[1]
            backpacker.localTime+=aux[1]
            backpacker.auxHungry=0          
        if backpacker.goToSleep()==True:
            aux=self.sleep(origin)
            backpacker.gold-=aux[0]
            backpacker.timeTravel+=aux[1]
            backpacker.localTime+=aux[1]
            print('aux sleep: ', backpacker.auxSleep)
            backpacker.auxSleep=0
            print('oro: ', backpacker.gold)
        if backpacker.estimate()==True:
            print('\nOro por debajo del 40% inicial, por favor seleccionar trabajo')
            aux=self.Jobs(origin)
            backpacker.timeTravel+=aux[1] #aumenta contador de tiempo de viaje
            backpacker.localTime+=aux[1]
            backpacker.auxHungry+=aux[1] #aumenta contador de hambre
            backpacker.auxSleep+=aux[1] #aumenta contador de sueño
            backpacker.gold+=aux[0] #aumenta oro del mochilero
        while True:
            print('tiempo de jugar')
            aux=self.activities(origin)
            backpacker.timeTravel+=aux[1]
            backpacker.localTime+=aux[1]
            backpacker.auxHungry+=aux[1]
            backpacker.auxSleep+=aux[1]
            backpacker.gold-=aux[0]
            inp=int(input('Ingrese 1:realizar otra actividad 2:salir'))
            if inp==2:
                break
            
        if backpacker.localTime<self.returnPlace(origin)['minTimeHere']:
            backpacker.timeTravel+=self.returnPlace(origin)['minTimeHere'] - backpacker.localTime
            backpacker.localTime=0
        
        aux=self.transportX(origin)
        backpacker.timeTravel+=aux[1]
        backpacker.auxHungry+=aux[1]
        backpacker.auxSleep+=aux[1]
        backpacker.gold-=aux[0]
        print('tiempo de viaje',backpacker.timeTravel )
        print('oro', backpacker.gold)
        
        
        
            
            
    
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
    
    def activities(self,label):
        city=self.returnPlace(label)
        time=0
        cost=0
        auxPrint=''
        c=0
        for h in city['things_to_do']:
            if h['type']=='optional':
                c+=1
                auxPrint +='\nActividades ciudad'+city['label']+ ': ' + 'Presione ({})'.format(c) + h['name'] + ' cost: ' +  str(h['cost']) + ' time: ' + str(h['time'])
        print(auxPrint)
        val=int(input('---> '))
        time=city['things_to_do'][val-1]['time']
        cost=city['things_to_do'][val-1]['cost']
        return cost,time
        
    
    def eat(self,label):
        city=self.returnPlace(label)
        time=0
        cost=0
        for h in city['things_to_do']:
            if h['name']=='Eat':
                time=h['time']
                cost=h['cost']
                continue
        return cost,time
                
                
    def sleep(self,label):
        city=self.returnPlace(label)
        time=0
        cost=0
        for h in city['things_to_do']:
            if h['name']=='Sleep':
                time=h['time']
                cost=h['cost']
                continue
        print('DURMIENDO')
        return cost,time
    
    def transportX(self,label):
        path=self.prim_mst(label)
        time=0
        cost=0
        auxPrint=''
        for h in path:
            if h==label:
                transports=self.returnTransportNode(h,path[h][0])
                travelDistance=self.returnTravelDistanceNode(h,path[h][0])
                print(transports)
                pass
        
        print('\nMedios de transporte:' )
        for h in transports:
            print('ht-->',h)
            aux=self.returnTranssport(h)
            print('auxT-->',aux)
            auxPrint +='\nPresione id del transporte ({})'.format(aux['id'])+ 'Tipo:' + aux['name'] + ' valor por km: ' +  str(aux['valueByKm']) + ' tiempo por km: ' + str(aux['timeByKm'])
        print(auxPrint)
        val=int(input('---> '))        
        aux=self.returnTranssport(val)
        print(aux['timeByKm'])
        time=self.returnTimeByKm(travelDistance,val)
        print(time)
        cost=self.returnGoldByKm(travelDistance,val)
        return cost,time
            
            
            
            
            
            
            
            
            
            