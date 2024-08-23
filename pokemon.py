#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:05:03 2024
"""
#This error message occurs bc the name attributes does not exist in the "pokemon_level"class
#how to fix this?
class Pokemon_level:
    """Everything about pokemon's level"""
    def __init__(self,name, level = 1): # so the default value is 1
        """Initialize pokemon's level"""
        self.level = level
        self.name = name #create a nenw attribute indie the pokemon name 

    def check_level(self):
        """Check your pokemon's current level"""
        print(f"the current level of {self.name} is {self.level}.")
        
    def update_level(self, level):
        """Update the level of your pokemon"""
        if level <=0 or level!= int(level):
            print(f"level has to be a positive integer!")
        else:
            self.level = level

class Pokemon: # classes are usually defined with capitalized names
    """Class to create pokemons"""

    def __init__(self, name, ptype):
        """Initialize name and type attributes"""
        self.name = name
        self.ptype = ptype
        self.level = Pokemon_level() #So everything about the level is initialized here
        
    def greeting(self):
        """Make your pokemon say hi to you"""
        print(f"{self.name} is saying hi to you!")

    def dance(self):
        """Make your pokemon dance"""
        print(f"{self.name} is dancing now!")
        
        #pikachu has name, ptype and level(level,check_level, update_level)



