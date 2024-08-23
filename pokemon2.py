#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:27:28 2024

@author: yutangsong
"""

class Pokemon: # classes are usually defined with capitalized names

    def __init__(self, name, ptype):
        """Initialize name and type attributes"""
        self.name = name
        self.ptype = ptype
           
    def greeting(self):
        """Make your pokemon say hi to you"""
        print(f"{self.name} is saying hi to you!")

    def dance(self):
        """Make your pokemon dance"""
        print(f"{self.name} is dancing now!")