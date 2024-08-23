#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:27:24 2024

@author: yutangsong
"""

from pokemon2 import Pokemon

class Pokemon_new(Pokemon):
    """Class for the new version of Pokemon game."""

    def __init__(self, name, ptype):
        """Initialize attributes of the parent class."""
        #self.name =mname 
        #self.ptype=ptype
        super().__init__(name, ptype) # super refers to the parent class, or Pokemon here.
        
    def add_height(self,height_increase):
        self.height=self.height + height_increase
        
    #override preexsiting methods
    def dance(self):
        print(f"{self.name}is dancing frevently!")