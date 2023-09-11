"""
Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

The Visitor pattern offers several benefits in software design and architecture, making it a powerful tool for managing operations on complex object structures. Here are five key benefits of the Visitor pattern:

1. **Separation of Concerns:** The Visitor pattern helps separate the algorithms or operations from the objects on which they operate. This separation promotes a clear division of responsibilities and keeps the code for different operations and object types independent and modular.

2. **Extensibility:** It allows you to add new operations (visitor implementations) to an object structure without modifying the structure's classes. This makes it easy to introduce new features or behaviors without affecting existing code, following the Open-Closed Principle (OCP).

3. **Maintainability:** With the Visitor pattern, each operation is implemented in a separate visitor class. This isolation simplifies maintenance and testing because changes or updates to one operation do not impact others. This leads to more maintainable and reliable code.

4. **Type Safety:** The Visitor pattern provides a way to define specific operations for different object types through method overloading (e.g., `visit_stock`, `visit_bond`). This ensures type safety and compiler checks, reducing the risk of runtime errors.

5. **Double Dispatch:** The Visitor pattern facilitates double dispatch, a mechanism where both the visitor and the visited object determine the actual method to execute. This enables dynamic dispatch based on both the visitor type and the element being visited, allowing for sophisticated operations based on object types and states.

These benefits make the Visitor pattern particularly valuable when dealing with complex object structures where various operations need to be applied to different object types without modifying those types directly. It promotes maintainable, extensible, and well-organized code.
"""

from abc import ABC, abstractmethod


class AssetVisitor(ABC):
    @abstractmethod
    def visit_stock(self, stock):
        pass

    @abstractmethod
    def visit_bond(self, bond):
        pass


class Stock:
    def __init__(self, symbol, shares, price_per_share):
        self.symbol = symbol
        self.shares = shares
        self.price_per_share = price_per_share

    def accept(self, visitor):
        visitor.visit_stock(self)


class Bond:
    def __init__(self, name, face_value, market_price):
        self.name = name
        self.face_value = face_value
        self.market_price = market_price

    def accept(self, visitor):
        visitor.visit_bond(self)


class PortfolioValueVisitor(AssetVisitor):
    def __init__(self):
        self.total_value = 0

    def visit_stock(self, stock):
        self.total_value += stock.shares * stock.price_per_share

    def visit_bond(self, bond):
        self.total_value += bond.market_price


if __name__ == "__main__":
    stock1 = Stock("AAPL", 100, 150.0)
    stock2 = Stock("GOOGL", 50, 2800.0)
    bond1 = Bond("US Treasury Bond", 1000, 1050.0)

    portfolio_visitor = PortfolioValueVisitor()
    stock1.accept(portfolio_visitor)
    stock2.accept(portfolio_visitor)
    bond1.accept(portfolio_visitor)

    total_portfolio_value = portfolio_visitor.total_value
    print(f"Total portfolio value: ${total_portfolio_value:.2f}")
