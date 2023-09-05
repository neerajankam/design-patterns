"""
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

The Adapter Design Pattern offers several benefits:

1. **Compatibility:** The Adapter pattern allows you to make incompatible classes or interfaces work together, enabling seamless collaboration between components that would otherwise not be able to communicate.

2. **Reusability:** Adapters can be reused to connect different pairs of incompatible classes or interfaces, reducing the need for custom integration code and promoting code reusability.

3. **Maintainability:** By encapsulating integration logic within adapters, you can keep the client code separate from the adaptee code. This separation enhances code maintainability, making it easier to modify, extend, and troubleshoot.

4. **Open-Closed Principle (OCP):** The Adapter pattern aligns with the Open-Closed Principle (OCP) from the SOLID principles. It allows you to introduce new adapters without modifying existing client or adaptee code, promoting extensibility.

5. **Pattern Recognition:** The Adapter pattern provides a recognizable and standardized solution for handling interface or class incompatibilities. Team members and developers familiar with the pattern can quickly understand how integrations work, promoting consistency in design and implementation.
"""
from abc import ABC, abstractmethod


class OldPaymentProcessor:
    # Adaptee
    def initiate_payment(self):
        print("Initiated payment using the old processor.")


class NewPaymentInterface(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class NewPaymentProcessor(NewPaymentInterface):
    def process_payment(self):
        print("Initiated payment using the new processor.")


class OldPaymentAdapter(NewPaymentInterface):
    # Adapter
    def __init__(self, old_payment_processor):
        self.old_payment_processor = old_payment_processor

    def process_payment(self):
        print("The adapter is calling the old processor to initiate payment.")
        self.old_payment_processor.initiate_payment()


if __name__ == "__main__":
    adaptee = OldPaymentProcessor()
    adapter = OldPaymentAdapter(adaptee)
    adapter.process_payment()
