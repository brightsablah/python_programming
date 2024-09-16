#!/usr/bin/python3
"""New Module contains Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # Use setter for validation
        self.position = position  # Use setter for validation

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
        # Validate that value is a tuple and has 2 elements
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Validate that both elements are integers and >= 0
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
            return
        
        # Print the vertical padding (position[1])
        for _ in range(self.position[1]):
            print()

        # Print the square with horizontal padding (position[0])
        for i in range(self.size):
            print(" " * self.position[0], end="")  # Print spaces for position[0]
            print("#" * self.size)  # Print the square row




Square(5).my_print()
print("--")

Square(3, (1, 1)).my_print()
print("--")

Square(3, (3, 0)).my_print()

Square(-9, (0,3)).my_print()
