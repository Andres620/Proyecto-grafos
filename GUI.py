# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:50:52 2019

@author: ayuwoki
"""

import pygame
from time import sleep
from pygame.locals import RESIZABLE
from pygame.locals import K_1,K_2,K_3,K_4,K_r
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
        self.paintLines() #lo saco del while trye para que no titile
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
                        self.paintLines()
                    if event.key == K_2:
                        print('Mayor cantidad de destinos segun la cantidad de oro: ')
                        origin=input('Ingrese nodo origen: ')
                        money=int(input('Ingrese la cantidad de oro del mochilero: '))
                        print('\nElegir transporte: ')
                        idTransport=int(input('1: plane 2:car 3:donkey: '))
                        aux=self.graph.longWayWithGold(origin,money,idTransport)
                        self.paintLines()
                        self.paintPath(aux)
                    if event.key == K_3:
                        print('Mayor cantidad de destinos segun el tiempo')
                        origin=input('Ingrese nodo origen: ')
                        time=int(input('Ingrese el tiempo disponible para el viaje del mochilero: '))
                        print('\nElegir transporte: ')
                        idTransport=int(input('1: plane 2:car 3:donkey: '))
                        aux=self.graph.longWayWithTime(origin,time,idTransport)
                        self.paintLines()
                        self.paintPath(aux)
                    if event.key == K_4:
                        print('ruta con menor gasto')
                        origin=input('Ingrese nodo origen: ')
                        aux=self.graph.prim_mst(origin)
                        self.paintPath(aux)
                    if event.key == K_r:
                        print('refrescar')
                        self.screen.fill((254,245,231))
                        self.paintLines()
                        
                        
            self.paint(self.graph)

            pygame.display.update()
            
            
        
    
    def paint(self,graph):
        if not graph is None:
            for h in graph.places:
                self.screen.blit(self.cityA,(h['posX'],h['posY']))
                textID = self.font.render("City: {}".format(h['label']), 0, (0, 0, 0))
                self.screen.blit(textID, (h['posX']-10, h['posY']-20))
                pygame.display.flip()
                
    def paintLines(self):
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
    
    def paintPath(self,path):  #modificar para mañana, metodo para que dibuje el camino
         if not path is None:
             for h in path:
                 pos1=self.graph.returnPosition(h)
                 pos2=self.graph.returnPosition(path[h][0])
                 pygame.draw.line(self.screen,(46,204,113),(pos1[0]+20,pos1[1]+20),(pos2[0]+20,pos2[1]+20),5)

                 
