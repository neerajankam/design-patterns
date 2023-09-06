"""
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

The Singleton design pattern offers several benefits in software design and architecture:

1. **Single Instance:** The primary benefit of the Singleton pattern is that it ensures a class has only one instance. This can be useful when exactly one object is needed to coordinate actions across the system, such as a configuration manager, a database connection pool, or a logging service.

2. **Global Point of Access:** The Singleton provides a single point of access to the instance it manages. This centralized access point simplifies the code and makes it easier to manage resources or state that should be shared across multiple parts of the application.

3. **Lazy Initialization:** Singleton instances can be lazily initialized, meaning they are created only when needed. This can help improve application startup time and reduce memory usage, especially if the singleton object is resource-intensive to create.

4. **Thread Safety:** A well-designed Singleton pattern can provide thread safety, ensuring that multiple threads don't create multiple instances. This is crucial for multithreaded applications, where multiple threads may access the Singleton concurrently.

5. **Reduced Global Variables:** The Singleton pattern offers a structured way to manage global state or resources without relying on global variables. Global variables can make code harder to understand and maintain, while Singletons encapsulate this global behavior within a single class.

6. **Improved Testing:** Singletons can be easier to test than global state or objects that are tightly coupled with other parts of the code. You can create mock or stub implementations of a Singleton for testing, allowing for better isolation of test cases.

7. **Memory Management:** In applications with resource constraints, the Singleton pattern can help manage resources efficiently. For example, a Singleton database connection pool can limit the number of connections created, reducing resource consumption.

8. **Initialization Control:** Singletons provide a controlled way to initialize and manage resources, settings, or services. This control ensures that resources are acquired and released in a predictable manner.

9. **Promotes Good Design Practices:** The Singleton pattern encourages adherence to good design principles such as encapsulation, separation of concerns, and the Single Responsibility Principle (SRP), as it often represents a single point of responsibility within an application.

10. **Consistency:** By providing a single instance, the Singleton pattern ensures that all parts of the application use the same instance of the object, promoting consistency in behavior and data.

It's important to note that while the Singleton pattern offers these benefits, it should be used judiciously. Overusing the Singleton pattern can lead to tight coupling and make code harder to test and maintain. Careful consideration should be given to whether a particular class truly requires a Singleton behavior.
"""


class Singleton:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance():
        return cls.__instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    # Check if they're the same instance
    print(s1 is s2)
