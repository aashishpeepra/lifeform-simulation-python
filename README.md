# Lifeform Simulator

## Dependencies
+ Time
+ Sys
+ Pygame
+ Random
 
## Files
1 Lifeform.py - File containting the lifeform class with the logic for each lifeoform object. The state data of each object have following properties
+ COORDS ( private, tuple, x,y coordinates)
+ ENERGY (private, int, energy level)
+ RANGE (private, dict, {x: tuple of range, y: tuple of range})
+ TYPE (private, int, (1 or 2 or 3) is the cateogory of lifeform)
+ COLORS (private, dictionary, set the custom color options for different category)
+ COLOR (private, tuple, color of current category)
+ NAME (private, str, name of category)
 Their motion, type, color, coordinates, energy level, collision logic. All the **state details** are ***encapsulated*** as **private data members** . **Getters and Setters** are used for complete data access and manipulation.  

2 parsciro.py - File containing the Parsciro class. This class ***inherits*** Lifeform class. It uses ***Pygame*** for visualizing the motion of lifeforms. The class have three basic function and a life loop which will run until the pygame pop is not closed. The terminal output will show the details of each lifeform. Managing the collision, updating, initializing lifeforms happens in this file. This is the file which have to be run with **python parsciro.py** command.
