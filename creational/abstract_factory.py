"""
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

The Abstract Factory pattern offers several benefits in software design and architecture, making it a valuable tool for creating families of related or dependent objects. Here are five key benefits of using the Abstract Factory pattern:

1. **Abstracts Object Creation:** The Abstract Factory pattern abstracts the process of object creation. It provides an interface for creating families of related objects without specifying their concrete classes. This abstraction allows for flexibility in choosing and configuring object implementations at runtime.

2. **Consistency Within Families:** It ensures that the objects created by a specific factory are consistent and compatible with each other. This is crucial when dealing with complex systems where objects need to work together cohesively, such as user interfaces or product families in manufacturing.

3. **Encapsulation of Knowledge:** The pattern encapsulates the knowledge of which classes belong to a particular family of objects within the factory implementations. This encapsulation reduces code duplication and ensures that clients remain unaware of the specific implementation details.

4. **Easy Substitution:** The Abstract Factory pattern simplifies the substitution of entire families of objects. By changing the concrete factory, you can switch the entire set of related objects used in an application, making it easier to adapt the system to different requirements or environments.

5. **Promotes Design Principles:** It encourages adherence to design principles like the Open-Closed Principle (OCP) and the Dependency Inversion Principle (DIP). The pattern makes it easier to extend the system by introducing new families of objects without modifying existing code, fostering maintainability and scalability.

Overall, the Abstract Factory pattern is valuable when designing systems that involve multiple families of related objects, ensuring consistency, maintainability, and flexibility in object creation and usage.
"""
from abc import ABC, abstractmethod


class Portfolio(ABC):
    @abstractmethod
    def describe(self):
        pass


class StockPortfolio(Portfolio):
    def describe(self):
        return "Stock Portfolio"


class BondPortfolio(Portfolio):
    def describe(self):
        return "Bond Portfolio"


class InvestmentFactory(ABC):
    @abstractmethod
    def create_portfolio(self):
        pass


class StockInvestmentFactory(InvestmentFactory):
    def create_portfolio(self):
        return StockPortfolio()


class BondInvestmentFactory(InvestmentFactory):
    def create_portfolio(self):
        return BondPortfolio()


def create_investment(factory):
    portfolio = factory.create_portfolio()
    print(f"Created {portfolio.describe()}")


if __name__ == "__main__":
    stock_factory = StockInvestmentFactory()
    bond_factory = BondInvestmentFactory()

    create_investment(stock_factory)
    create_investment(bond_factory)
