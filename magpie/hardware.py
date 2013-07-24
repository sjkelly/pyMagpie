#!/usr/bin/env python
from textcad import *
import magpie.utility

class Hardware(component.Element):
    def __init__(self, name):
        component.Element.__init__(self, name = name)
    def size_from_diameter():
        pass

class CapScrew(component.Element):

    def __init__(self, size="M3", length=10):
        component.Element.__init__(self, name="capscrew")
        self.size = size
        self.length = length
        self.outerDiameter = 0
        self.headHeight = 0
        self.headDiameter = 0
        self.keySize = 0
        self.keyDepth = 0
        magpie.utility.get_dimensions(size = size, name = "capScrew", obj = self)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        self.construction = self._construction()

    def _construction(self):
        head = element.Cylinder(radius=self.headDiameter/2,
                                height=self.headHeight)
        outerThread = element.Cylinder(radius=self.outerDiameter/2,
                                       height=self.headHeight + self.length)
        key = element.Ntube(sides=6, apothem=self.keySize/2, height=self.keyDepth+0.1)
        key.location = [0, 0, -0.1]
        screwConstruction = head + outerThread - key
        return screwConstruction

class Nut(component.Element):

    def __init__(self, size="M3"):
        component.Element.__init__(self, name="nut")
        self.size = size
        self.height = 0
        self.width = 0
        self.diameter = 0
        magpie.utility.get_dimensions(size = size, name = "nut", obj = self)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        self.construction = self._construction()

    def _construction(self):
        hexagon = element.Ntube(sides = 6, apothem = self.width/2, height = self.height)
        hole = element.Cylinder(radius = self.diameter/2, height = self.height + 0.2)
        hole.location = [0, 0, -0.1]
        return hexagon - hole

class LockNut(component.Element):

    def __init__(self, size="M3"):
        component.Element.__init__(self, name="locknut")
        self.size = size
        self.height = 0
        self.wrenchingHeight = 0
        self.width = 0
        self.diameter = 0
        magpie.utility.get_dimensions(size = size, name = "lockNut", obj = self)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        self.construction = self._construction()

    def _construction(self):
        wrenchSection = element.Ntube(sides=6, apothem=self.width/2, height=self.wrenchingHeight)
        bevel = element.Cylinder(radius = self.width/2, height = self.height) #TODO replace with torus 
        hole = element.Cylinder(radius=self.diameter/2, height=self.height + 0.2)
        hole.location = [0, 0, -0.1]
        return wrenchSection + bevel - hole

if __name__=="__main__":
    import subprocess
    utility.export(CapScrew(size="M3", length=10), "capscrew.json")
    utility.export(Nut(size="M3"), "nut.json")
    utility.export(LockNut(size="M3"), "locknut.json")
