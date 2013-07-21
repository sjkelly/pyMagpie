#!/usr/bin/env python
from textcad import *
import magpie.utility


class BallBearing(component.Element):

    def __init__(self, size="608zz", make = True):
        component.Element.__init__(self, name="ballbearing")
        self.size = size
        self.innerDiameter = 0
        self.outerDiameter = 0
        self.width = 0
        magpie.utility.get_dimensions(size = size, name = "ballBearing", obj = self)
        if make:
            self.location = [0, 0, 0]
            self.color = [0.5, 0.5, 0.5]
            self.construction = self._construction()

    def _construction(self):
        outer = element.Cylinder(radius=self.outerDiameter/2, height=self.width)
        inner = element.Cylinder(radius=self.innerDiameter/2, height=self.width+0.2)
        inner.location = [0, 0, -0.1]
        return outer - inner

class LinearBallBearing(element.Primitive):

    def __init__(self, size="LM8UU", make = True, negative=False):
        element.Primitive.__init__(self, name="linearballbearing")
        self.size = size
        self.innerDiameter = 0
        self.outerDiameter = 0
        self.length = 0
        magpie.utility.get_dimensions(size = size, name = "linearBallBearing", obj = self)
        if make:
            self.location = [0, 0, 0]
            self.color = [0.5, 0.5, 0.5]
            if not negative:
                self.construction = self.positiveConstruction()
            else:
                self.construction = self.negativeConstruction()

    def positiveConstruction(self):
        outer = element.Cylinder(radius=self.outerDiameter/2, height=self.length)
        inner = element.Cylinder(radius=self.innerDiameter/2, height=self.length+0.2)
        inner.location = [0, 0, -0.1]
        return outer - inner

    def negativeConstruction(self):
        return element.Hole(radius=self.outerDiameter/2, height=self.length)

if __name__=="__main__":
    utility.export(BallBearing(size="625zz"), "ballbearing.json")
    utility.export(LinearBallBearing(size="LM5UU"), "linearballbearing.json")
