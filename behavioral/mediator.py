"""
Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications
between the objects and forces them to collaborate only via a mediator object.

The Mediator pattern offers several benefits in software design and architecture, especially when dealing with complex systems and interactions between multiple objects. Here are five key benefits of using the Mediator pattern:

1. **Decoupling of Components:** The Mediator pattern promotes loose coupling between objects by centralizing communication and reducing direct dependencies. This leads to a more modular and maintainable codebase, as changes to one component are less likely to affect others.

2. **Centralized Control:** It provides a centralized point of control for coordinating interactions between objects. This centralization simplifies the management of complex interactions and ensures that communication flows through a controlled and organized channel.

3. **Simplified Communication:** The Mediator pattern simplifies communication between objects by encapsulating complex communication logic within the mediator. Objects only need to know how to communicate with the mediator, not with each other, leading to cleaner and more focused code.

4. **Flexibility and Extensibility:** Adding new components or modifying existing ones becomes easier because changes are localized to the mediator. You can introduce new mediators for specific scenarios or extend the existing mediator without affecting the entire system.

5. **Promotes Reusability:** The Mediator pattern encourages the reuse of mediators across different parts of the application. This reusability reduces redundant code and ensures a consistent and well-structured approach to managing object interactions.

These benefits make the Mediator pattern a valuable choice when dealing with complex systems, especially in scenarios where many objects need to communicate or coordinate their actions. It enhances code maintainability, scalability, and flexibility while promoting a clean separation of concerns.

"""
from abc import ABC, abstractmethod


class StockExchangeMediator(ABC):
    @abstractmethod
    def execute_order(self, trader, order):
        pass


class StockExchange(StockExchangeMediator):
    def __init__(self):
        self.orders = []

    def execute_order(self, trader, order):
        print(f"Stock Exchange: {order} received from {trader.name}")
        self.orders.append(order)


class Trader:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def buy(self, stock_symbol, quantity):
        order = f"Buy {quantity} shares of {stock_symbol}"
        self.mediator.execute_order(self, order)

    def sell(self, stock_symbol, quantity):
        order = f"Sell {quantity} shares of {stock_symbol}"
        self.mediator.execute_order(self, order)


if __name__ == "__main__":
    exchange = StockExchange()

    trader1 = Trader("Alice", exchange)
    trader2 = Trader("Bob", exchange)

    trader1.buy("AAPL", 100)
    trader2.sell("GOOGL", 50)

    print("\nOrder Log:")
    for order in exchange.orders:
        print(order)
