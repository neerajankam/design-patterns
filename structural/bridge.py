"""
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two
separate hierarchies—abstraction and implementation—which can be developed independently of each other.

The Bridge Design Pattern offers several benefits, including:

1. Decoupling of abstraction and implementation: The pattern separates the abstraction from its implementation, which means that changes made to one will not affect the other. This decoupling can help to reduce code complexity and make the code more maintainable and extensible.

2. Hiding implementation details: The pattern allows you to hide the implementation details from the client code, which means that the client code only interacts with the abstraction. This can help to reduce the complexity of the client code and make it easier to understand.

3. Flexibility: The pattern provides flexibility by allowing you to swap different implementations of an abstraction at runtime. This means that you can change the behavior of your application without having to modify the code.

4. Scalability: The pattern provides scalability by allowing you to add new abstractions and implementations without affecting the existing code. This means that you can easily add new features to your application as your requirements change.

5. Reusability: The pattern promotes reusability by allowing you to reuse existing abstractions and implementations in other parts of your code or in other applications.

Overall, the Bridge Design Pattern can help to improve the maintainability, flexibility, scalability, and reusability of your code.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print(f"Drawing Circle with {self._color.fill()} color")


class Square(Shape):
    def draw(self):
        print(f"Drawing Square with {self._color.fill()} color")


class Color:
    def fill(self):
        pass


class RedColor(Color):
    def fill(self):
        return "Red"


class BlueColor(Color):
    def fill(self):
        return "Blue"


if __name__ == "__main__":
    circle = Circle(RedColor())
    circle.draw()

    square = Square(BlueColor())
    square.draw()
