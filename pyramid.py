from shapes3d import Shape3d
from memory import remember


class Pyramid(Shape3d):
    @remember
    def __init__(self, width: int, height: int, depth: int):
        Shape3d.__init__(self, width, height, depth)

    def __str__(self):
        return f"Class: Pyramid. Width: {self.width}. Height: {self.height}. Depth: {self.depth}"
    
    def __mul__(self, other):
        return Pyramid(self.width * other.width, self.width * other.width, self.depth * other.depth)
    
    def volume(self) -> float:
        return (1/3 * self.width * self.height * self.depth)