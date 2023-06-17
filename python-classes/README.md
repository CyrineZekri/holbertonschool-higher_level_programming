  # Python - Classes and Objects

This repository contains examples and exercises related to Python classes and objects.

## Description

The "Python - Classes and Objects" project provides a collection of examples and exercises to help you understand and practice object-oriented programming concepts in Python. It covers topics such as class definition, instance attributes, properties, and methods.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Exercise](#exercise)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/CyrineZekri/holbertonschool-higher_level_programming/tree/main/python-classes
```

## Usage

Navigate to the project directory:

```
cd Python-Classes-and-Objects
```

Execute the Python scripts to run the examples or complete the exercises.

## Examples

The project includes various examples that demonstrate different aspects of classes and objects in Python. Each example is self-contained and can be executed independently.

## Exercise

In addition to the examples, the project provides an exercise to practice creating a class called `Square`:

- Private instance attribute: `size`
  - Property `size(self)`: to retrieve the size
  - Property setter `size(self, value)`: to set the size
    - Raises a `TypeError` if the value is not an integer with the message "size must be an integer"
    - Raises a `ValueError` if the value is less than 0 with the message "size must be >= 0"

- Private instance attribute: `position`
  - Property `position(self)`: to retrieve the position
  - Property setter `position(self, value)`: to set the position
    - Raises a `TypeError` if the value is not a tuple of 2 positive integers with the message "position must be a tuple of 2 positive integers"

- Instantiation with optional size and optional position: `__init__(self, size=0, position=(0, 0))`

- Public instance method: `area(self)`: returns the current square area

- Public instance method: `my_print(self)`: prints the square with the character '#' in stdout
  - If size is equal to 0, an empty line is printed
  - Position is used to determine the starting position of the square, using spaces

## Contributing

Contributions to the project are always welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
