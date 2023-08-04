#!/usr/bin/python3
"""Square module"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """method constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """representation method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
