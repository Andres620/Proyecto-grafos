# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:01:40 2019

@author: ayuwoki
"""
from places import places
import json

def main():

    with open('format.json') as file:
        data =json.load(file)
        transport=data['transportForm']
        #print(transport)
        graph=data['places']
        #print(graph[1])
        
        gr=places(graph,transport)
        
        gr.printPlaces()
        gr.printTransport()
        
        
        
        
            
            
    print('hola mundo')

if __name__== "__main__":
    main()