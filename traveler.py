# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:02:08 2019

@author: ayuwoki
"""

class traveler:
    
    def __init__(self,money):
        self.gold=money
        self.auxGold=money
        self.hungry=False
        self.sleep=False
        self.auxHungry=0
        self.auxSleep=0
        
    def estimate(self):
        if self.gold< (self.auxGold*0.4):
            return True
    
    def sleep(self):
        if self.auxHungry>=6:
            self.hungry=True
    
        
