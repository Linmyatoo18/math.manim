from manim import *
import numpy as np

class waves(Scene):
    def construct(self):
        a = Axes(x_range=[-10,10], y_range=[-2,2])
        graph = a.plot(lambda x: np.sin(x), color=RED)
        self.add(a)