"""
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

Benefits of the Chain of Responsibility Pattern:

1) Loose Coupling: The Chain of Responsibility pattern promotes loose coupling between sender and receiver objects. The sender doesn't need to know the specific handler that will process its request, enhancing flexibility and maintainability.

2) Single Responsibility: Each handler has a single responsibility: either handling the request or passing it to the next handler in the chain. This adheres to the Single Responsibility Principle (SRP), making it easier to manage and extend the system.

3) Dynamic Chain: You can easily change the order or composition of the chain at runtime. This flexibility allows you to add, remove, or reorder handlers without modifying client code, promoting the Open-Closed Principle (OCP).

4) Fallback Mechanism: If a handler can't process a request, it can delegate the request to its successor. This creates a fallback mechanism, ensuring that requests are handled gracefully even if the primary handler cannot process them.

5) Avoiding God Objects: The Chain of Responsibility pattern helps prevent the creation of "God objects" that try to do everything. Instead, it encourages breaking down responsibilities into smaller, manageable components (handlers) that can be combined as needed.

Overall, the Chain of Responsibility pattern is a useful design pattern for building flexible and maintainable systems, especially when dealing with scenarios where multiple objects can handle requests, and the exact handler may vary at runtime.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handled by ConcreteHandlerA.")
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handled by ConcreteHandlerB.")
        elif self.successor:
            self.successor.handle_request(request)


if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    handler_a.successor = handler_b

    requests = ["A", "B"]

    for request in requests:
        handler_a.handle_request(request)
