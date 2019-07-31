# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:02:08 2019

@author: ayuwoki
"""

class traveler:
    
    def __init__(self,money):
        self.timeTravel=0
        self.localTime=0
        self.gold=money
        self.auxGold=money
        self.hungry=False
        self.sleep=False
        self.auxHungry=18
        self.auxSleep=0
        self.report={}
        
    def estimate(self):
        if self.gold< (self.auxGold*0.4):
            return True
    
    def goToEat(self):
        if self.auxHungry>=18:
            self.auxHungry=True
            return True
            
    def goToSleep(self):
        if self.auxSleep>=6:
            self.sleep=True
            return True
        
    def readReport(self):
        for h in self.report:
            print('reporte de la ciudad: ',h)
            for j in self.report[h]:
                print(j+'-->')
            #    for k in self.report[h][j]: #esto debe mostrar el reporte
             #       print(k)
            
        
