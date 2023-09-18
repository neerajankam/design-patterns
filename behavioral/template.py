"""
Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses
override specific steps of the algorithm without changing its structure.

Benefits of the Template Method Pattern:

1) Code Reuse: The Template Method pattern promotes code reuse by defining a common algorithm in a base class and allowing subclasses to implement specific steps. This reduces code duplication and maintains a consistent structure across subclasses.

2) Enforced Structure: It enforces a specific structure or sequence of steps in an algorithm, ensuring that certain operations are always performed in a particular order. This is valuable for maintaining a consistent behavior across different implementations.

3) Extensibility: Subclasses can easily extend or customize the behavior of the template method by implementing the abstract custom operation. This flexibility allows for variations of the algorithm while keeping the core structure intact.

4) Reduced Complexity: The pattern simplifies complex algorithms by breaking them into smaller, manageable steps. Each step can be implemented and tested separately, making the code more maintainable and understandable.

5) Framework for Frameworks: The Template Method pattern is often used to build frameworks or libraries where the overall structure of an algorithm is defined, but the specific behavior is left to be defined by users or subclasses. This approach is commonly used in GUI frameworks, game engines, and more.

Overall, the Template Method pattern is valuable for creating reusable and extensible algorithms while maintaining a consistent structure. It encourages good design practices such as code reuse, separation of concerns, and modularity.
"""
from abc import ABC, abstractmethod


class TemplateClass(ABC):
    def algorithm(self):
        self.common_operation1()
        self.custom_operation()
        self.common_operation2()

    def common_operation1(self):
        print("This is the first common operation.")

    def common_operation2(self):
        print("This is the second common operation.")

    @abstractmethod
    def custom_operation(self):
        pass


class ConcreteClassA(TemplateClass):
    def custom_operation(self):
        print("This is custom operation in ConcreteClassA.")


class ConcreteClassB(TemplateClass):
    def custom_operation(self):
        print("This is custom operation in ConcreteClassB.")


if __name__ == "__main__":
    print("\nRunning algorithm using class A")
    class_a = ConcreteClassA()
    class_a.algorithm()
    print("\nRunning algorithm using class B")
    class_b = ConcreteClassB()
    class_b.algorithm()
