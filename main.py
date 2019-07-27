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
        gr.printPlaces()
        gr.printTransport()
        
        print("\n prueba ------------------------------------")
        
        
            
            
        print('hola mundo')
        gui.window()
        
if __name__== "__main__":
    main()