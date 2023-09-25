"""
Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request.
This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

The Command pattern offers several benefits in software design and development, making it a valuable tool for encapsulating and decoupling requests from their receivers. 
Here are five key benefits of using the Command pattern:

1. **Decoupling of Requester and Receiver:** The Command pattern decouples the object that issues a request (the sender or requester) from the object that performs the action (the receiver). 
This separation of concerns reduces the direct dependencies between sender and receiver, promoting flexibility and maintainability.

2. **Parameterization of Objects:** Commands encapsulate requests as objects, allowing you to parameterize clients with different requests. 
This parameterization enables dynamic composition of requests and supports undo/redo functionality, macros, and queuing of requests.

3. **Support for Undo/Redo Operations:** By encapsulating actions as commands, the Command pattern supports undo and redo operations. 
Commands can store the state before execution, enabling you to revert actions and reapply them in a controlled manner.

4. **Queueing and Logging of Requests:** Commands can be easily stored in data structures like queues or lists. 
This enables the creation of command histories, transaction logs, and script-like operations. Queueing commands can also support scheduling and asynchronous processing.

5. **Extensibility and Flexibility:** New commands can be added without modifying existing code, making the system more extensible and adaptable to changing requirements. 
You can introduce new command classes to add functionality or modify existing ones to change behavior without affecting the client code.

These benefits make the Command pattern a powerful tool for managing and abstracting actions, requests, or operations in various applications, including user interfaces, automation systems, and financial software. 
It enhances code modularity, supports undo/redo functionality, and provides a clean separation of concerns.
"""
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class BuyStockCommand(Command):
    def __init__(self, stock, quantity):
        self.stock = stock
        self.quantity = quantity

    def execute(self):
        self.stock.buy(self.quantity)


class SellStockCommand(Command):
    def __init__(self, stock, quantity):
        self.stock = stock
        self.quantity = quantity

    def execute(self):
        self.stock.sell(self.quantity)


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.quantity = 0

    def buy(self, quantity):
        self.quantity += quantity
        print(f"Bought {quantity} shares of {self.symbol}")

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} shares of {self.symbol}")
        else:
            print("Not enough shares to sell.")


if __name__ == "__main__":
    apple_stock = Stock("AAPL")
    google_stock = Stock("GOOGL")

    buy_apple = BuyStockCommand(apple_stock, 100)
    sell_google = SellStockCommand(google_stock, 50)

    buy_apple.execute()
    sell_google.execute()
