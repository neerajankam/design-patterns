"""
Composite is a structural design pattern that allows composing objects into a tree-like structure and work with the it as if it was a singular object.

The Composite pattern offers several benefits in software design, making it a valuable tool for creating tree-like structures composed of objects. 
Here are five key benefits of using the Composite pattern:

1. **Hierarchy and Structure:** The Composite pattern allows you to create hierarchies and structures of objects that represent part-whole relationships. 
This simplifies the modeling of complex systems, as it enables you to treat individual objects and compositions of objects uniformly.

2. **Flexibility and Extensibility:** You can add and remove objects from the composition at runtime, allowing for dynamic changes in the structure. 
This flexibility and extensibility make it easy to create and modify complex object hierarchies to meet changing requirements.

3. **Uniform Interface:** The pattern enforces a uniform interface for both leaf and composite objects through a common component interface or base class. 
This uniformity simplifies client code, as it can work with objects at any level of the hierarchy without needing to distinguish between leaf and composite objects.

4. **Code Reusability:** By using a common interface, you can reuse client code for processing individual objects when dealing with composite structures. 
This reduces code duplication and promotes maintainability.

5. **Recursive Operations:** The Composite pattern supports recursive operations on the entire object hierarchy. 
Operations can be applied to individual objects or propagated through composite objects, making it easy to implement functions like traversal, calculation of values, and printing of structured data.

These benefits make the Composite pattern a powerful tool for designing and managing complex structures of objects, such as user interfaces, 
organizational hierarchies, file systems, and financial portfolios. It simplifies code, enhances flexibility, and allows you to work with hierarchical data 
structures in a more intuitive and consistent way.
"""
from abc import ABC, abstractmethod


class Investment(ABC):
    @abstractmethod
    def get_value(self):
        pass


class Stock(Investment):
    def __init__(self, symbol, quantity, price_per_share):
        self.symbol = symbol
        self.quantity = quantity
        self.price_per_share = price_per_share

    def get_value(self):
        return self.quantity * self.price_per_share


class Bond(Investment):
    def __init__(self, name, face_value, market_value):
        self.name = name
        self.face_value = face_value
        self.market_value = market_value

    def get_value(self):
        return self.market_value


class Portfolio(Investment):
    def __init__(self, name):
        self.name = name
        self.investments = []

    def add_investment(self, investment):
        self.investments.append(investment)

    def get_value(self):
        total_value = 0
        for investment in self.investments:
            total_value += investment.get_value()
        return total_value


if __name__ == "__main__":
    apple_stock = Stock("AAPL", 100, 150.0)
    microsoft_stock = Stock("MSFT", 50, 200.0)
    government_bond = Bond("US Treasury Bond", 1000.0, 1050.0)

    tech_portfolio = Portfolio("Tech Investments")
    tech_portfolio.add_investment(apple_stock)
    tech_portfolio.add_investment(microsoft_stock)

    global_portfolio = Portfolio("Global Portfolio")
    global_portfolio.add_investment(tech_portfolio)
    global_portfolio.add_investment(government_bond)

    total_value = global_portfolio.get_value()
    print(f"Investments in {global_portfolio.name} are: ")
    for investment in global_portfolio.investments:
        print(investment.name)

    print(f"Total value: ${total_value}")
