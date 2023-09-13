"""
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Here are five key benefits of using the Builder pattern:

1. **Separation of Concerns:** The Builder pattern separates the construction of an object from its representation. This separation allows you to vary the object's internal representation independently of how it's constructed. It's particularly useful when an object can have multiple representations.

2. **Complex Object Construction:** It simplifies the construction of complex objects by breaking it down into a series of steps. Each step is encapsulated within a builder, making the overall process more manageable and understandable. This is especially beneficial when an object has many optional components or configuration settings.

3. **Fluent Interface:** Builders often use a fluent interface, which allows for a more readable and expressive code style. With method chaining, you can set multiple attributes or properties in a single line of code, making it easier to configure objects.

4. **Immutability:** Builders can be designed to create immutable objects, ensuring that once an object is constructed, its state cannot be changed. This is valuable for creating objects that are thread-safe and free from unexpected modifications.

5. **Parameterized Construction:** Builders enable you to create objects with different configurations using the same construction process. You can create multiple builder instances with different settings, providing flexibility in constructing objects tailored to specific use cases.

In summary, the Builder pattern simplifies the construction of complex objects, promotes a separation of concerns between construction and representation, and offers a fluent and flexible way to create objects with different configurations. It is particularly useful when dealing with objects that have many optional components or need to be constructed in a specific sequence.
"""


class Pizza:
    def __init__(self):
        self.__crust = ""
        self.__toppings = []

    def set_crust(self, crust):
        self.__crust = crust

    def add_topping(self, topping):
        self.__toppings.append(topping)

    def __str__(self):
        return f"Pizza with {', '.join(self.__toppings)} toppings and {self.__crust} crust."


class PizzaBuilder:
    def __init__(self):
        self.__pizza = Pizza()

    def add_cheese(self):
        self.__pizza.add_topping("cheese")
        return self

    def add_pepperoni(self):
        self.__pizza.add_topping("pepperoni")
        return self

    def add_mushrooms(self):
        self.__pizza.add_topping("mushrooms")
        return self

    def set_thick_crust(self):
        self.__pizza.set_crust("thick")
        return self

    def set_thin_crust(self):
        self.__pizza.set_crust("thin")
        return self

    def build(self):
        return self.__pizza


if __name__ == "__main__":
    builder = PizzaBuilder()
    pizza = builder.add_cheese().add_pepperoni().set_thin_crust().build()

    print(pizza)
