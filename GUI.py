# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:50:52 2019

@author: ayuwoki
"""

import pygame
from pygame.locals import RESIZABLE
from pygame.locals import K_1
import sys

class GUI:
    
    def __init__(self,graph):
        self.graph=graph
        self.sWIDTH = 1180    #screen width
        self.sHEIGHT = 600    #screen height
        self.font=None
        self.screen=None
        self.cityA=pygame.image.load("images/cityA.png")
        self.deadDonkey=pygame.image.load("images/deadDonkey.png")
        
        
    def window(self):
        pygame.init()
        pygame.display.set_caption("Soy el mapa")
        self.screen=pygame.display.set_mode((self.sWIDTH, self.sHEIGHT),RESIZABLE)
        self.screen.fill((254,245,231))
        self.font = pygame.font.SysFont("Arial", 12)
        self.paintLines(self.graph) #lo saco del while trye para que no titile
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        print('Obstruir via')
                        self.graph.callObstructVia()
                        self.screen.fill((254,245,231))
                        self.paintLines(self.graph)
            self.paint(self.graph)

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
                if not j['obstruction']:
                    pygame.draw.line(self.screen,(26,8,242),(x1,y1),(x2,y2),5)
                else:
                    pygame.draw.line(self.screen,(200, 0, 0),(x1,y1),(x2,y2),5)
                    avgPosX,avgPosY=self.graph.midPoint(x1,y1,x2,y2)
                    self.screen.blit(self.deadDonkey,(avgPosX,avgPosY-30))
                    pygame.display.flip()
         pygame.display.flip()
