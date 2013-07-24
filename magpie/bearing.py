#!/usr/bin/env python
from textcad import *
import magpie.utility


class BallBearing(element.Primitive):

    def __init__(self,
                 size="608zz",
                 negative=False,
                 radiusTolerance=0,
                 widthTolerance=0):
        element.Primitive.__init__(self, name="ballbearing")
        self.size = size
        self.innerDiameter = 0
        self.outerDiameter = 0
        self.width = 0
        self.widthTolerance = widthTolerance
        self.radiusTolerance = radiusTolerance
        magpie.utility.get_dimensions(size=size,
                                      name="ballBearing",
                                      obj=self)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        if not negative:
            self.construction = self.positiveConstruction()
        else:
            self.construction = self.negativeConstruction()

    def positiveConstruction(self):
        outer = element.Cylinder(radius=self.outerDiameter/2,
                                 height=self.width)
        inner = element.Cylinder(radius=self.innerDiameter/2,
                                 height=self.width+0.2)
        inner.location = [0, 0, -0.1]
        return outer - inner

    def negativeConstruction(self):
        mock = element.Hole(radius=self.outerDiameter/2,
                            height=self.width+self.widthTolerance,
                            tolerance=self.radiusTolerance)
        mock.location = [0, 0, -self.widthTolerance/2]
        return mock


class LinearBallBearing(element.Primitive):

    def __init__(self,
                 size="LM8UU",
                 negative=False,
                 radiusTolerance=0,
                 lengthTolerance=0):
        element.Primitive.__init__(self, name="linearballbearing")
        self.size = size
        self.innerDiameter = 0
        self.outerDiameter = 0
        self.length = 0
        self.radiusTolerance = radiusTolerance
        self.lengthTolerance = lengthTolerance
        magpie.utility.get_dimensions(size=size,
                                      name="linearBallBearing",
                                      obj=self)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        if not negative:
            self.construction = self.positiveConstruction()
        else:
            self.construction = self.negativeConstruction()

    def positiveConstruction(self):
        outer = element.Cylinder(radius=self.outerDiameter/2,
                                 height=self.length)
        inner = element.Cylinder(radius=self.innerDiameter/2,
                                 height=self.length+0.2)
        inner.location = [0, 0, -0.1]
        return outer - inner

    def negativeConstruction(self):
        mock = element.Hole(radius=self.outerDiameter/2,
                            height=self.length+self.lengthTolerance,
                            tolerance=self.radiusTolerance)
        mock.location = [0, 0, -self.lengthTolerance/2]
        return mock

if __name__ == "__main__":
    import subprocess
    utility.export(BallBearing(size="625zz"), "ballbearing.json")
    subprocess.Popen("textcad -o ballbearing.scad -s ballbearing.json".split())
    utility.export(LinearBallBearing(size="LM5UU"), "linearballbearing.json")
    subprocess.Popen(("textcad -o linearballbearing.scad"
                     + " -s linearballbearing.json").split())
