"""
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

Certainly! Here are five key benefits of the Proxy design pattern:

1. **Controlled Access:** Proxies can control access to the real object, allowing you to implement access control mechanisms such as permission checks, authentication, and authorization. This helps you restrict or grant access to resources based on specific criteria.

2. **Lazy Loading:** Proxies can defer the creation or loading of the real object until it is actually needed. This is useful for optimizing resource usage, especially when dealing with resource-intensive objects like large files or database connections. Lazy loading can improve application startup times.

3. **Caching:** Proxies can implement caching mechanisms to store and reuse the results of expensive operations performed by the real object. Caching can lead to significant performance improvements by reducing redundant work.

4. **Remote Object Access:** In distributed systems, proxies can represent objects that exist on remote servers. They can handle communication details such as network protocols, serialization, and deserialization, making it easier to work with remote objects as if they were local.

5. **Logging and Monitoring:** Proxies can add logging, monitoring, and profiling capabilities without modifying the real object's code. This allows you to gather valuable information about the real object's behavior and performance.

These benefits make the Proxy design pattern a valuable tool for enhancing the control, efficiency, and security of your software systems.
"""
from abc import ABC, abstractmethod


@abstractmethod
class BankAccountInterface:
    @abstractmethod
    def get_balance(self):
        pass


class BankAccount(BankAccountInterface):
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = "1000$"

    def get_balance(self):
        return self.balance


class Proxy:
    def __init__(self, account_number):
        self.account_number = account_number
        self.real_account = None

    def check_access(self):
        print("User has access!")
        return True

    def get_balance(self):
        print("Check access!")
        if self.check_access():
            if self.real_account is None:
                self.real_account = BankAccount(self.account_number)
            return self.real_account.get_balance()


if __name__ == "__main__":
    proxy = Proxy("12345")
    bank_balance = proxy.get_balance()
    print(bank_balance)
