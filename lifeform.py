import random

class Lifeform():
    def __init__(self,type,range,energy):
        self.__COORDS = (0,0)
        self.__ENERGY = energy
        self.__RANGE = {"x" :(-range,range), "y" : (-range,range)} #x : (-5,5), y: (-10,10)
        self.__TYPE = 1 #1,2,3
        self.__COLORS = { 1 : (255,0,0) ,2 : (0,255,0), 3 : (0,0,255)}
        self.__COLOR = "red"
        self.__NAME = ""
        self.set_type(type)
    def set_coords(self,coords):
        self.__COORDS=coords
    def set_range(self,range):
        self.__RANGE = range
    def move(self):
        # boundry condition
        if self.__COORDS[0] >1000 or self.__COORDS[0]<0:
            self.__COORDS = (0,self.__COORDS[1])
        if self.__COORDS[1] > 1000 or self.__COORDS[1] < 0:
            self.__COORDS = (self.__COORDS[0],0)
        self.__COORDS = (random.randint(self.__RANGE["x"][0],self.__RANGE["x"][1])+self.__COORDS[0],random.randint(self.__RANGE["y"][0],self.__RANGE["y"][1]) + self.__COORDS[1])
    def set_random_coords(self):
        self.__COORDS = (random.randint(self.__RANGE["x"][0],self.__RANGE["x"][1]),random.randint(self.__RANGE["y"][0],self.__RANGE["y"][1]))
    def set_type(self,type):
        """
        This function sets the category for this lifeform.
            Parameters: 
                type (int) : Integer value between 1 to 3
            Returns:
                null : this function returns null
        """
        self.__TYPE = type
        self.__COLOR = self.__COLORS[type]
        #name of the lifeforms
        self.__NAMES = {1 : "Chlorella" ,2 : "Amoeba", 3 : "Halobacteria"}
        self.__NAME = self.__NAMES[type]
        if type == 1:
            self.__RANGE = {"x" :(-50,50), "y" : (-50,50)}
        elif type == 2:
            self.__RANGE = {"x" :(-30,30), "y" : (-30,30)}
        elif type == 3:
            self.__RANGE = {"x" :(-10,10), "y" : (-10,10)}
    def set_energy(self,energy):
        self.__ENERGY += energy
    def get_color(self):
        return self.__COLOR
    def get_type(self):
        return self.__TYPE
    def get_energy(self):
        return self.__ENERGY
    def get_coords(self):
        return self.__COORDS
    def __str__(self):
        return "{} , COORDS : ({},{}) , ENERGY : {}".format(self.__NAME,self.__COORDS[0],self.__COORDS[1],self.__ENERGY)
    def perform_collision(self,lifeObject):
        """
        This function performs the collision between this and lifeObject.
            Parameters:
                lifeObject (Lifeform) : A Lifeform Object
            Returns:
                null : This function returns null
        """
        print("Collided")
        typeConfig = self.__TYPE + lifeObject.get_type()
        if self.__TYPE == lifeObject.get_type(): #self
            self.__ENERGY -= 3
            lifeObject.set_energy(-3)
            self.__COORDS = (-30,self.__COORDS[1])
            lifeObject.set_coords((random.randint(-30,30),random.randint(-30,30)))
        elif typeConfig == 3: # 1 and 2
            self.__ENERGY -= 3
            lifeObject.set_energy(-4)
            self.__COORDS = (-30,self.__COORDS[1])
            lifeObject.set_coords((random.randint(-30,30),random.randint(-30,30)))
        elif typeConfig == 4: # 3  and 1
            self.__ENERGY -= 4
            lifeObject.set_energy(-5)
            self.__COORDS = (-30,self.__COORDS[1])
            lifeObject.set_coords((random.randint(-30,30),random.randint(-30,30)))
        elif typeConfig == 5: # 3 and 2
            self.__ENERGY -= 5
            lifeObject.set_energy(-4)
            self.__COORDS = (-30,self.__COORDS[1])
            lifeObject.set_coords((random.randint(-30,30),random.randint(-30,30)))
        # type -> 1 , 2, 3 -> 
        #BOUNCE AFTER COLISSION
        
            


            