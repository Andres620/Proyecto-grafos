# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:01:40 2019
/d/Prsnl Fls/2019-1/Estructuras de datos/graphProject
@author: ayuwoki
"""
from places import places
from GUI import GUI
import json

def main():

    with open('format.json') as file:
        data =json.load(file)
        transport=data['transportForm']
        #print(transport)
        graph=data['places']
        #print(graph[1])
        gr=places(graph,transport)
        gui=GUI(gr)
        #gr.printPlaces()
        #gr.printTransport()
        
        #print("\n prueba ------------------------------------")
        #gr.callObstructVia()
        #print(gr.adjacent('A'))
        #print('dineros',gr.returnGoldByKm(4,3))
        #print('tiempos',gr.returnTimeByKm(43,3))
        #print('Prim: ', gr.prim_mst('A')) 
        #print('camino con oro: ',gr.longWayWithGold('A',2500,1))
        #print('\n','camino con tiempo: ',gr.longWayWithTime('A',2500,1))
        #print('\n travel:',gr.travel('A'))
        #print('place:',gr.returnPlace('A'))
        #print('place value: ', gr.returnTransportNode('A','C'))
        #print(gr.returnTranssport(1))
        #print(gr.transportX('G'))
        #print('hola mundo')
        gui.window()
        
if __name__== "__main__":
    main()