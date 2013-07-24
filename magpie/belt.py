#!/usr/bin/env python
from textcad import *
import magpie.utility


class TimingBelt(component.Element):

    def __init__(self, size="GT2", width=0, make = True):
        component.Element.__init__(self, name="timingbelt")
        self.size = size
        self.width = width
        self.height = 0
        self.toothHeight = 0
        self.pitch = 0
        magpie.utility.get_dimensions(size = size, name = "timingBelt", obj = self)
        if make:
            self.location = [0, 0, 0]
            self.color = [0.5, 0.5, 0.5]
            self.construction = self._construction()

    def _construction(self):
        pass
