#!/usr/bin/python3
"""
creating a rectangle class
"""


class Rectangle:
    """defining the Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getting the value of the width"""
        return self.__width

    @property
    def height(self):
        """getting the value of the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setting the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """setting the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
        return self.__height
