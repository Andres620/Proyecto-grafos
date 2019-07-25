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
        self.cityA=pygame.image.load("images/GPS.png")
        
        
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
            pygame.display.update()
            
            
        
    
    def paint(self,graph):
        if not graph is None:
            self.screen.blit(self.cityA,(100,50))
            pygame.display.flip()