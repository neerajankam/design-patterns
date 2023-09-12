"""
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

Here are five key benefits of the Decorator design pattern:

1. **Open-Closed Principle**: The Decorator pattern follows the open-closed principle, which means you can extend the behavior of a class without modifying its source code. This promotes code stability and reduces the risk of introducing bugs when making changes.

2. **Flexibility**: Decorators can be stacked or combined in various ways to create new combinations of behavior. This flexibility allows you to mix and match decorators to achieve different effects, making it easy to tailor the behavior of objects to specific requirements.

3. **Single Responsibility Principle**: Each decorator class has a single responsibility, which is to add a specific behavior or feature to the component it decorates. This promotes a clean and modular design by separating concerns and ensuring that each class has a well-defined purpose.

4. **Reusable Components**: Decorators are reusable components that can be applied to different objects of the same interface or base class. This reusability can lead to a more efficient and maintainable codebase, as decorators can be used across multiple parts of an application.

5. **Maintains Interface Compatibility**: Decorators implement the same interface as the components they decorate. This ensures that clients (code that uses the objects) can treat decorated objects and original objects interchangeably. This simplifies the code and makes it easier to work with decorated objects without needing to know their specific details.

In summary, the Decorator design pattern provides a flexible and reusable way to add behavior to objects, promotes good design principles, and allows for the extension of functionality without modifying existing code.
"""

from abc import ABC, abstractmethod


class FinancialProduct(ABC):
    @abstractmethod
    def cost(self):
        pass


class BasicInvestment(FinancialProduct):
    def cost(self):
        return 1000


class FeatureDecorator(FinancialProduct):
    def __init__(self, product):
        self._product = product

    @abstractmethod
    def cost(self):
        pass


class TaxDecorator(FeatureDecorator):
    def cost(self):
        return self._product.cost() + 50  # Add a $50 tax


class InsuranceDecorator(FeatureDecorator):
    def cost(self):
        return self._product.cost() + 100  # Add a $100 insurance fee


basic_investment = BasicInvestment()
print("Basic Investment Cost: $" + str(basic_investment.cost()))

investment_with_tax = TaxDecorator(basic_investment)
print("Investment with Tax Cost: $" + str(investment_with_tax.cost()))

investment_with_insurance = InsuranceDecorator(basic_investment)
print("Investment with Insurance Cost: $" + str(investment_with_insurance.cost()))

investment_with_tax_and_insurance = InsuranceDecorator(TaxDecorator(basic_investment))
print(
    "Investment with Tax and Insurance Cost: $"
    + str(investment_with_tax_and_insurance.cost())
)
