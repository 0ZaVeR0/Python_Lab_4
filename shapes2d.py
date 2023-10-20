class Shape2d:
    def __init__(self, width: int, height: int, color: str):
        self.__width = width
        self.__height = height
        self.__color = color

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

    def is_correct_size(self, size: int) -> bool:
        return isinstance(size, int) and size >= 0
