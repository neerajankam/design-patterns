"""
Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state
between multiple objects instead of keeping all of the data in each object.

The main benefit of the Flyweight pattern is memory optimization. This pattern is particularly useful when you have a large number of objects with shared or intrinsic state,
and it allows you to reduce memory consumption by sharing that state among multiple objects. Here's how it achieves this benefit:

1. **Shared State:** The Flyweight pattern separates objects into intrinsic (shared) and extrinsic (unique) states. Intrinsic state is the portion of an object's state
that can be shared among multiple objects, while extrinsic state is unique to each object. By sharing the intrinsic state, you avoid redundant storage of the same data
for multiple objects.

2. **Object Reusability:** The pattern promotes the reuse of existing objects instead of creating new ones. When a client requests an object with a specific intrinsic state,
the Flyweight factory either returns an existing object with that state or creates a new one if it doesn't exist. This minimizes the creation of redundant objects in memory.

3. **Reduced Memory Overhead:** By sharing common state and reusing objects, the Flyweight pattern reduces memory overhead, making it efficient when dealing with a
large number of similar objects. It's particularly valuable in scenarios where memory is a limited resource.

4. **Improved Performance:** Reduced memory consumption can lead to improved performance, as it reduces the time and resources required for object creation and garbage collection. 
This can be especially important in applications that need to be memory-efficient and responsive.

Overall, the Flyweight pattern's primary benefit lies in its ability to optimize memory usage while still allowing you to work with a large number of objects.
It's a valuable tool for scenarios where memory efficiency is a concern, such as in graphical applications, simulations, or systems dealing with a high volume of data.
"""

from dataclasses import dataclass


@dataclass
class Stock:
    ticker: str
    name: str
    price: int

    def display(self):
        print(f"Stock: {self.ticker}, Name: {self.name}, Price: {self.price}")


class StockFactory:
    _available_stocks = {}

    @staticmethod
    def get_stock(ticker, name, price):
        if ticker not in StockFactory._available_stocks:
            StockFactory._available_stocks[ticker] = Stock(ticker, name, price)
        return StockFactory._available_stocks[ticker]


if __name__ == "__main__":
    # Client code
    apple_1 = StockFactory.get_stock("AAPL", "Apple Inc.", 150.0)
    google = StockFactory.get_stock("GOOGL", "Alphabet Inc.", 2500.0)
    apple_2 = StockFactory.get_stock("AAPL", "Apple Inc.", 150.0)

    stocks = [apple_1, google, apple_2]

    for stock in stocks:
        stock.display()
    print(apple_1 is apple_2)
