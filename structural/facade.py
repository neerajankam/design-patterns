"""
Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

The Facade Design Pattern offers several benefits:

1. **Simplified Interface:** Provides a simplified and user-friendly interface to a complex subsystem.
   
2. **Reduced Complexity:** Hides the intricacies of the subsystem, making client code cleaner and more maintainable.
   
3. **Decoupling:** Promotes loose coupling between clients and subsystems, allowing changes in one without affecting the other.
   
4. **Improved Testing:** Simplifies unit testing by testing the facade rather than multiple subsystems.
   
5. **Encapsulation:** Encapsulates subsystem complexities, promoting separation of concerns and better code organization.
"""


class Extract:
    def extract_data(self, url):
        print(f"I'm going to download the data from {url}")


class Transform:
    def transform_data(self, data):
        print("I'm going to transform the data!")


class Load:
    def load_data(self, data):
        print("I'm going to load the data!")


class Facade:
    def __init__(self):
        self.extract = Extract()
        self.transform = Transform()
        self.load = Load()

    def perform_etl(self):
        data = self.extract.extract_data("https://dummydata.com")
        self.transform.transform_data(data)
        self.load.load_data(data)


if __name__ == "__main__":
    facade = Facade()
    facade.perform_etl()
