#!/usr/bin/python3
"""New Module contains Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if  not all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        area = self.size * self.size
        return area

    def my_print(self):
        if self.size == 0:
            print()
            return
        
        # vertical padding (position[1])
        for i in range(self.position[1]):
            print()

        # square with hosrizontal padding (position[0])
        for j in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)



Square(3).my_print()
print("--")

Square(3, (1, 1)).my_print()
print("--")

Square(3, (3, 0)).my_print()

Square(0, (0,0)).my_print()
