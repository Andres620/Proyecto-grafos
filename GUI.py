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
        self.cityA=pygame.image.load("images/cityA.png")
        
        
    def window(self):
        pygame.init()
        pygame.display.set_caption("Soy el mapa")
        self.screen=pygame.display.set_mode((self.sWIDTH, self.sHEIGHT),RESIZABLE)
        self.screen.fill((254,245,231))
        self.font = pygame.font.SysFont("Arial", 12)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                    
            self.paint(self.graph)
            self.paintLines(self.graph)
            pygame.display.update()
            
            
        
    
    def paint(self,graph):
        if not graph is None:
            for h in graph.places:
                self.screen.blit(self.cityA,(h['posX'],h['posY']))
                pygame.display.flip()
                
    def paintLines(self,graph):
         for h in self.graph.places:
            for j in h['goingTo']:
                x1=h['posX']+20
                y1=h['posY']+20
                x2=self.graph.returnPlace(j['label'])['posX']+20
                y2=self.graph.returnPlace(j['label'])['posY']+20
                pygame.draw.line(self.screen,(200, 0, 0),(x1,y1),(x2,y2))
