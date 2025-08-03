from manim import *
import numpy as np

class waves(Scene):
    def construct(self):
        a = Axes(x_range=[-10,10], y_range=[-2,2])
        
        self.add(a)