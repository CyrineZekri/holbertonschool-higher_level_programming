# Python - More Classes and Objects

This project focuses on further exploring the concepts of object-oriented programming (OOP) in Python. We will be creating a class called "Rectangle" that defines a rectangle and provides various functionalities related to its attributes and methods.

## Class Details

### Private instance attributes:
- `width`: Represents the width of the rectangle.
- `height`: Represents the height of the rectangle.

### Properties:
- `width`: Retrieves the value of the width attribute.
- `width` (setter): Sets the value of the width attribute. Raises a TypeError if the value is not an integer and raises a ValueError if the value is less than 0.
- `height`: Retrieves the value of the height attribute.
- `height` (setter): Sets the value of the height attribute. Raises a TypeError if the value is not an integer and raises a ValueError if the value is less than 0.

### Public class attributes:
- `number_of_instances`: Represents the number of instances of the Rectangle class. It is initialized to 0 and incremented during each new instance instantiation. It is decremented during each instance deletion.
- `print_symbol`: Represents the symbol used for string representation of the rectangle. It can be any type.

### Instantiation:
- The class can be instantiated with optional width and height parameters using the `__init__(self, width=0, height=0)` method.

### Public instance methods:
- `area(self)`: Computes and returns the area of the rectangle.
- `perimeter(self)`: Computes and returns the perimeter of the rectangle. If either the width or height is equal to 0, the perimeter is considered to be 0.
- `__str__(self)`: Returns a string representation of the rectangle using the symbol defined in `print_symbol`. If the width or height is equal to 0, an empty string is returned.
- `__repr__(self)`: Returns a string representation of the rectangle to be able to recreate a new instance using `eval()`.
- `__del__(self)`: Prints the message "Bye rectangle..." when an instance of Rectangle is deleted.

### Static method:
- `bigger_or_equal(rect_1, rect_2)`: Compares two Rectangle instances and returns the rectangle with the biggest area. Raises a TypeError if either `rect_1` or `rect_2` is not an instance of Rectangle.

### Class method:
- `square(cls, size=0)`: Creates and returns a new Rectangle instance where the width and height are both equal to `size`.

## Contributing
Contributions to the project are always welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Author 
Made with Love by: Cyrine Zekri:heart: