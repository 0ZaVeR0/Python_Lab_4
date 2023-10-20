from shapes2d import Shape2d
from memory import remember


class Squre(Shape2d):
    @remember
    def __init__(self, side: int, color: str):
        Shape2d.__init__(self, side, side, color)

    def __str__(self):
        return f"Class: Squre. Width: {self.width}. Height: {self.height}."
