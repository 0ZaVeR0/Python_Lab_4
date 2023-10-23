class Shape3d:
    def __init__(self, width: int, height: int, depth: int):
        if self.is_correct_size(width):
            self.__width = width
        else:
            print("Incorrect width")

        if self.is_correct_size(height):
            self.__height = height
        else:
            print("Incorrect height")
            
        if self.is_correct_size(depth):
            self.__depth = depth
        else:
            print("Incorrect depth")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if self.is_correct_size(width):
            self.__width = width
        else:
            print("Incorrect width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if self.is_correct_size(height):
            self.__height = height
        else:
            print("Incorrect height")

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth: int):
        if self.is_correct_size(depth):
            self.__depth = depth
        else:
            print("Incorrect depth")

    def is_correct_size(self, size: int) -> bool:
        return isinstance(size, int) and size >= 0
    
    def volume(self)-> int:
        return (self.width * self.height * self.depth)
