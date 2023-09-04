"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

The Factory Design Pattern offers several benefits:

1. Encapsulation: The creation of objects is encapsulated in a single class, the factory class, making it easier to manage and maintain the creation logic.

2. Decoupling: The Factory Design Pattern decouples the client code from the creation logic of objects, allowing you to modify the creation logic without affecting the client code.

3. Abstraction: The Factory Design Pattern abstracts the process of object creation, making it easier to create different types of objects and switch between them without changing the client code.

4. Flexibility: The Factory Design Pattern provides flexibility in object creation. You can create objects dynamically at runtime based on some input conditions.

5. Reusability: The Factory Design Pattern promotes reusability by allowing you to create objects with common interfaces or behaviors.

Overall, the Factory Design Pattern promotes better code organization, scalability, and maintainability, making it a popular choice for complex software systems.
"""
from abc import ABC, abstractmethod


class OSInterface(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Windows(OSInterface):
    def __init__(self, name):
        self.name = "Windows"

    def get_name(self):
        return self.name


class Linux(OSInterface):
    def __init__(self, name):
        self.name = "Linux"

    def get_name(self):
        return self.name


class MacOS(OSInterface):
    def __init__(self, name):
        self.name = "MacOS"

    def get_name(self):
        return self.name


class Factory:
    def produce_object(self, os_name):
        if os_name == "Windows":
            return Windows(os_name)
        elif os_name == "Linux":
            return Linux(os_name)
        elif os_name == "MacOS":
            return MacOS(os_name)
        else:
            raise ValueError(f"The inputted OS: {os_name} does not exist")


if __name__ == "__main__":
    factory = Factory()
    windows = factory.produce_object("Windows")
    print(windows.get_name())
