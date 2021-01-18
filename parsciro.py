import random
import time
from lifeform import Lifeform
import pygame
import sys

class Parsciro():
    def __init__(self,initial,red,green,blue,energy):
        self.allLife =[]
        self.ROUNDS = initial
        self.INFO = {1:red,2:green,3:blue}
        self.ENERGY = energy
        pygame.init() #STARTS THE PYGAME
        self.SCREENSIZE = (1000,1000) #HEIGHT, WIDTH OF THE SCREEN
        self.SCREEN = pygame.display.set_mode(self.SCREENSIZE) #CREATE A SCREEN -> screen
        
    def initialize_life(self):
        for i in range(self.ROUNDS):
            firstForm = Lifeform(1,self.INFO[1],self.ENERGY)
            secondForm = Lifeform(2,self.INFO[2],self.ENERGY)
            thirdForm = Lifeform(3,self.INFO[3],self.ENERGY)
            firstForm.set_random_coords()
            secondForm.set_random_coords()
            thirdForm.set_random_coords()
            self.allLife.append(firstForm)
            self.allLife.append(secondForm)
            self.allLife.append(thirdForm)
            print(firstForm)
        # print(self.allLife)
    def check_collision(self):
        coordinates = [each.get_coords() for each in self.allLife]
        i = 0
        length = len(coordinates)
        while i < length:
            if coordinates[i] in coordinates[i+1:]:
                index = coordinates[i+1:].index(coordinates[i]) + i+1
                self.allLife[i].perform_collision(self.allLife[index])
                if self.allLife[i].get_type() == self.allLife[index].get_type() : 
                    newLife = Lifeform(self.allLife[i].get_type(),self.INFO[self.allLife[i].get_type()],self.ENERGY)
                    newLife.set_random_coords()
                    self.allLife.append(newLife)
                    coordinates.append(newLife.get_coords())
                    length+=1
                    print("NEW LIFe")
            i+=1
    def update_life(self):
        #BACKGROUND COLOR change -> wHITE -> (255,255,255) , black -> (0,0,0)
        self.SCREEN.fill((255,255,255))
        for each in self.allLife:
            if each.get_energy()<=0:
                print(" --->Removed",each)
                self.allLife.remove(each)
                continue
            each.move()
            # imageBase = {1: "nameOfImage.png" ,2 :"nameOfSecondImahge.png",3:"Thirdname.png"}
            # self.SCREEN.asurf =  pygame.image.load("./images/"+imageBase[each.get_type()]) #"/images/nameOfImage.png"
            pygame.draw.circle(self.SCREEN,each.get_color(),each.get_coords(),5)
            print(each)
        pygame.display.update()
        pygame.display.flip()
            
    def life_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    counter = {1:0,2:0,3:0}
                    for each in self.allLife:
                        counter[each.get_type()]+=1
                    NAMES = {1:"Chlorella",2:"Amoeba",3:"Halobacteria"}
                    for each in counter.keys():
                        print(NAMES[each],":",counter[each])
                    sys.exit()
            clock = pygame.time.Clock()
            clock.tick(200)
            self.check_collision()
            self.update_life()
            
            
            # pygame.display.update()
            
            
            # self.SCREEN.Rect(0,0,0)
            time.sleep(0.05)
                
            



if __name__ == "__main__":
    intitialLifeforms = int(input("Enter Initial number of lifeforms : "))
    print("SET MOVEMENT PARAMETERS")
    print("RED Movement, Enter single integer ")
    red = int(input())
    print("GREEN Movement, Enter single integer ")
    green = int(input())
    print("BLUE Movement, Enter single integer ")
    blue = int(input())
    energy = int(input("Enter Initial energy level "))
    World = Parsciro(intitialLifeforms,red,green,blue,energy)
    World.initialize_life()
    World.life_loop()
