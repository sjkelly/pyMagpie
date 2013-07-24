#!/usr/bin/env python
from textcad import *
import magpie.utility
import magpie.hardware


class Stepper(component.Element):

    def __init__(self,
                 size="GenericNEMA17",
                 negative=False,
                 negativeLength=10):
        component.Element.__init__(self, name="stepper")
        self.size = size
        self.width = 0
        self.length = 0
        self.mountSpacing = 0
        self.mountScrew = ""
        self.flangeDiameter = 0
        self.flangeHeight = 0
        self.shaftLength = 0
        self.shaftDiameter = 0
        self.negative = negative
        self.negativeLength = negativeLength
        magpie.utility.get_dimensions(size=size, name="stepperMotor", obj=self)
        self.holeLocations = [[self.mountSpacing/2, self.mountSpacing/2, 0],
                              [self.mountSpacing/2, -self.mountSpacing/2, 0],
                              [-self.mountSpacing/2, self.mountSpacing/2, 0],
                              [-self.mountSpacing/2, -self.mountSpacing/2, 0]]
        self.screw = magpie.hardware.CapScrew(size=self.mountScrew)
        self.location = [0, 0, 0]
        self.color = [0.5, 0.5, 0.5]
        self.construction = self._construction()

    def _construction(self):
        body = element.Cube([self.width, self.width, self.length])
        body.center = [True, True, False]
        body.location = [0, 0, -self.length]
        flange = element.Cylinder(radius=self.flangeDiameter/2,
                                  height=self.flangeHeight)
        shaft = element.Cylinder(radius=self.shaftDiameter/2,
                                 height=self.shaftLength+self.flangeHeight)
        asm = body + flange + shaft
        if self.negative:
            # Flange
            asm += element.Hole(radius=self.flangeDiameter/2,
                                height=self.negativeLength)
            # Mount holes
            for hole in self.holeLocations:
                s = element.Hole(radius=self.screw.outerDiameter/2,
                                 height=self.negativeLength)
                s.location = hole
                asm += s
        return asm
