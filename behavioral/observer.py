"""
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

The Observer pattern offers several benefits in software design and development, making it a valuable tool for implementing event-driven and reactive systems. Here are five key benefits of using the Observer pattern:

1. **Decoupling of Components:** The Observer pattern promotes loose coupling between the subject (observable) and its observers (subscribers). Observers are not directly aware of each other, and changes to one component don't necessitate changes in others. This reduces interdependencies and enhances maintainability.

2. **Flexibility and Extensibility:** New observers can be added easily without modifying the subject or existing observers. This flexibility allows you to introduce new functionality or behavior to a system incrementally, making it easier to extend and adapt to changing requirements.

3. **Support for Event-Driven Architectures:** The Observer pattern is a fundamental component of event-driven architectures. It enables the creation of systems that respond dynamically to events or state changes, such as user interactions, sensor data updates, or data model changes.

4. **Customized Notification:** Observers can subscribe to specific events or types of notifications from the subject. This fine-grained control allows observers to receive only the information relevant to their concerns, improving efficiency and reducing unnecessary processing.

5. **Maintains Consistency:** The Observer pattern ensures that all interested observers are notified of changes in the subject's state. This consistency is crucial in scenarios where multiple components rely on accurate and up-to-date information, such as user interfaces, distributed systems, and real-time applications.

These benefits make the Observer pattern a powerful and versatile design pattern for building systems that need to propagate changes and events efficiently while maintaining modularity and flexibility.
"""
from abc import ABC, abstractmethod


class StockMarket:
    def __init__(self):
        self._observers = []
        self._stock_price = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_stock_price(self, price):
        self._stock_price = price
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._stock_price)


class Investor(ABC):
    @abstractmethod
    def update(self, price):
        pass


class StockInvestor(Investor):
    def __init__(self, name):
        self._name = name

    def update(self, price):
        print(f"Investor {self._name} received new stock price: {price}")


if __name__ == "__main__":
    # Step 4: Client code
    market = StockMarket()

    investor1 = StockInvestor("Alice")
    investor2 = StockInvestor("Bob")

    market.attach(investor1)
    market.attach(investor2)

    market.set_stock_price(100.0)
    # Update stock price
    market.set_stock_price(120.0)
