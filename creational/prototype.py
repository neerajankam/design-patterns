"""
Prototype is a creational design pattern that allows cloning objects, even complex ones, without coupling to their specific classes.


The Prototype pattern offers several benefits in software design and development, making it a valuable tool for creating objects. Here are five key benefits of using the Prototype pattern:

1. **Efficient Object Creation:** The Prototype pattern allows you to create new objects by copying existing ones, often referred to as prototypes. This can be more efficient than creating objects from scratch, especially when object initialization is resource-intensive or complex.

2. **Reduced Subclass Proliferation:** It reduces the need for creating subclasses of an object to represent variations. Instead of creating subclasses for each variant, you can clone a prototype and customize it as needed. This helps avoid a large number of subclasses and simplifies class hierarchies.

3. **Runtime Flexibility:** The ability to create new objects at runtime by cloning prototypes provides flexibility in designing and configuring objects. You can change the type and state of objects dynamically based on application requirements, user input, or configuration settings.

4. **Preservation of Object State:** Cloning a prototype creates a new object with the same initial state as the original. This can be beneficial when you want to preserve the state of an object, especially in situations where you want to reset an object to its initial state without reinitializing it manually.

5. **Enhanced Performance:** In scenarios where object creation is time-consuming or resource-intensive, using prototypes can significantly improve application performance. Objects can be created once and then cloned as needed, reducing the overhead of object creation.

These benefits make the Prototype pattern a valuable choice when you need to efficiently create and configure objects, reduce class proliferation, and adapt objects at runtime to meet changing requirements.
"""
import copy
from abc import ABC, abstractmethod


class PrototypeInterface(ABC):
    @abstractmethod
    def clone(self):
        pass


class Vehicle(PrototypeInterface):
    def __init__(self, brand, model, engine_capacity):
        self.brand = brand
        self.model = model
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(
            f"Brand: {self.brand}, Model: {self.model}, Engine Capacity: {self.engine_capacity}"
        )

    def clone(self):
        print("Cloning the object!")
        return copy.deepcopy(self)


class Car(Vehicle):
    def __init__(self, brand, model, engine_capacity, num_doors):
        super().__init__(brand, model, engine_capacity)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


if __name__ == "__main__":
    camry = Car("Toyota", "Camry", 2.5, 4)
    camry_clone = camry.clone()
    print(camry is camry_clone)
    camry_clone.display_info()
