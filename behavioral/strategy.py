"""
The Strategy Design Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.
It allows you to change the behavior of an object without changing its implementation.

The Strategy design pattern offers several benefits, making it a valuable tool in software design and architecture. Here are some of the key advantages:

1. **Encapsulation of Algorithms:** The Strategy pattern encapsulates algorithms or behaviors into separate classes, known as strategies. This encapsulation allows you to modify, extend, or replace algorithms independently of the context that uses them. It promotes clean separation of concerns by isolating different strategies.

2. **Flexibility and Extensibility:** With the Strategy pattern, you can add new strategies without modifying existing code. This flexibility is particularly valuable when you have a family of related algorithms or behaviors that can evolve over time. You can create new strategies and plug them into the system as needed.

3. **Promotes Open-Closed Principle:** The Strategy pattern aligns with the Open-Closed Principle (OCP), one of the SOLID principles. OCP states that software entities (classes, modules, functions) should be open for extension but closed for modification. By using strategies, you can extend the behavior of a class without changing its source code.

4. **Simplifies Testing:** Strategies can be tested in isolation. This makes it easier to write unit tests for individual strategies, ensuring that they work correctly. Additionally, testing the context that uses strategies becomes more straightforward as it's decoupled from specific algorithm implementations.

5. **Easier Maintenance:** Code that uses the Strategy pattern is typically more maintainable. When a change is required, you only need to modify the relevant strategy or add a new one, keeping the existing codebase intact. This reduces the risk of introducing bugs in other parts of the system.

6. **Better Code Organization:** Strategies help organize code by grouping related algorithms into separate classes. This separation improves code readability and maintainability, making it clear which algorithm is used in a given context.

7. **Run-Time Switching:** The Strategy pattern allows you to switch between strategies at run time. This dynamic behavior is useful when you need to adapt to changing requirements or user preferences without restarting the application.

8. **Promotes Code Reuse:** Strategies can be reused across different parts of the application or even in entirely different projects. This promotes code reuse and ensures consistency in algorithm implementations.

9. **Simplified Conditional Logic:** In situations where you might have used extensive conditional statements to select among different algorithms, the Strategy pattern provides a cleaner alternative. It eliminates the need for complex branching and simplifies the code's flow.

10. **Improved Collaboration:** The Strategy pattern promotes collaboration among team members by providing a clear structure for introducing and managing new strategies. Team members can work on different strategies independently.

In summary, the Strategy design pattern offers a powerful way to manage algorithms, behaviors, and variations within a system. It promotes flexibility, maintainability, and code organization while adhering to fundamental software design principles like the Open-Closed Principle. When used appropriately, the Strategy pattern can enhance the robustness and adaptability of software systems.
"""

from abc import ABC, abstractmethod


class InvestInterface:
    @abstractmethod
    def invest(self):
        pass


class LessRiskInvesting(InvestInterface):
    def __init__(self, wealth):
        self.wealth = wealth
        self.assets = {"bonds": 40, "real estate": 40, "stocks": 20}

    def invest(self):
        print(
            "I'm going to invest 40% of my wealth in bonds, 40% in real estate and 20% in stocks."
        )


class MediumRiskInvesting(InvestInterface):
    def __init__(self, wealth):
        self.wealth = wealth
        self.assets = {"stocks": 40, "real estate": 30, "gold": 20, "cryptos": 10}

    def invest(self):
        print(
            "I'm going to invest 40% of my wealth in stocks, 30% in real estate, 20% in gold and 10% in cryptos."
        )


class HighRiskInvesting(InvestInterface):
    def __init__(self, wealth):
        self.wealth = wealth
        self.assets = {"cryptos": 40, "stocks": 30, "real estate": 20, "gold": 10}

    def invest(self):
        print(
            "I'm going to invest 40% of my wealth in cryptos, 30% in stocks, 20% in real estate and 10% in gold."
        )


class InvestingApp:
    def __init__(self, investing_strategy):
        self.investing_strategy = investing_strategy

    def invest(self):
        self.investing_strategy.invest()


if __name__ == "__main__":
    app_instance = InvestingApp(LessRiskInvesting(100000))
    app_instance.invest()
