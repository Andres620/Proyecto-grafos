# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:50:52 2019

@author: ayuwoki
"""

import pygame
from pygame.locals import RESIZABLE
import sys

class GUI:
    
    def __init__(self,graph):
        self.graph=graph
        self.sWIDTH = 1180    #screen width
        self.sHEIGHT = 600    #screen height
        self.font=None
        self.screen=None
        
        
    def window(self):
        pygame.init()
        pygame.display.set_caption("Árbol NArio")
        self.screen=pygame.display.set_mode((self.sWIDTH, self.sHEIGHT),RESIZABLE)
        self.screen.fill((254,245,231))
        self.font = pygame.font.SysFont("Arial", 12)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
            pygame.display.update()
            
            
        
    
    def paint(self,graph):
        if not graph is None:
            for h in graph.places:
                h.assingColor()
                pygame.display.flip()
            for h in graph.places:
                self.paint(h)