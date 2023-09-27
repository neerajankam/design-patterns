"""
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

The Iterator pattern offers several benefits in software design, particularly when dealing with collections of data. Here are four key benefits of using the Iterator pattern:

1. **Encapsulation of Traversal Logic:** The Iterator pattern encapsulates the logic for traversing a collection within an iterator object. 
This separation of concerns isolates the traversal code from the client code, making both easier to maintain and modify independently. 
It also abstracts the underlying data structure, allowing clients to focus on processing elements without worrying about the traversal details.

2. **Consistent Interface:** Iterator objects provide a uniform interface for accessing elements within a collection, regardless of the collection's underlying structure (e.g., array, linked list, tree). 
This consistent interface simplifies client code by ensuring that the same methods (e.g., `__next__` and `has_next`) are used regardless of the specific collection type.

3. **Support for Different Iteration Strategies:** By encapsulating the traversal logic, the Iterator pattern allows you to implement various iteration strategies.
 For example, you can create different iterators for forward, backward, or filtered traversal, providing flexibility in how clients access and process data within the collection.

4. **Enhanced Reusability:** Iterators can be reused across different parts of an application or in different applications altogether. 
Once an iterator is implemented for a specific collection type, it can be used to traverse similar collections with minimal modification. 
This reusability promotes code efficiency and reduces redundancy.

These benefits make the Iterator pattern a valuable tool for simplifying the traversal of collections, enhancing code modularity, and promoting the separation of concerns 
in software design. It is commonly used in various programming scenarios, including data access layers, user interface components, and data processing applications.
"""
from collections.abc import Iterator


class FinancialIterator(Iterator):
    def __init__(self, financial_data):
        self._data = financial_data
        self._index = 0

    def __next__(self):
        try:
            transaction = self._data[self._index]
            self._index += 1
            return transaction
        except IndexError:
            raise StopIteration("No more data!")


class FinancialData:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def create_iterator(self):
        return FinancialIterator(self.transactions)


if __name__ == "__main__":
    financial_data = FinancialData()
    financial_data.add_transaction("Buy AAPL shares")
    financial_data.add_transaction("Sell GOOGL shares")
    financial_data.add_transaction("Deposit $1000")

    iterator = financial_data.create_iterator()

    print("Financial Transactions:")
    for transaction in iterator:
        print(transaction)
