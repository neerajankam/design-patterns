"""
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

The State pattern offers several benefits in software design, particularly when managing the behavior of objects that transition between different states.
Here are four key benefits of using the State pattern:

1. **Modularity and Separation of Concerns:** The State pattern promotes a clean separation of concerns by encapsulating the behavior associated with each state
in separate state classes. This modularity makes it easier to understand, maintain, and extend the codebase. Each state class focuses on a specific aspect
of an object's behavior, reducing complexity.

2. **Flexibility and Extensibility:** Adding new states or modifying existing ones is relatively easy with the State pattern. You can introduce new state classes
without altering the context class (the object that changes its state), which means that you can extend the behavior of an object without affecting other parts of the code. This makes the pattern highly adaptable to changing requirements.

3. **Simplified Conditional Logic:** Without the State pattern, objects in various states may require complex conditional statements to manage their behavior.
The State pattern replaces these conditionals with polymorphism, as each state class encapsulates its own behavior. This results in cleaner and more maintainable code.

4. **Improved Code Readability:** When using the State pattern, client code interacts with the context class (e.g., the document or investment) through a common interface,
making it easy to understand the available operations. The code becomes more self-explanatory, as the behavior of each state is encapsulated within its respective class.
This can lead to more readable and maintainable code.

Overall, the State pattern helps manage the behavior of objects in a flexible and modular way, making it suitable for scenarios where objects can transition between
different states and exhibit varying behaviors. It encourages good design principles like the Single Responsibility Principle and enhances code maintainability and readability.
"""
from abc import ABC, abstractmethod


class DocumentState(ABC):
    @abstractmethod
    def handle(self):
        pass


class DraftState(DocumentState):
    def handle(self):
        return "Document is in the draft state"


class ModeratedState(DocumentState):
    def handle(self):
        return "Document is in moderation"


class PublishedState(DocumentState):
    def handle(self):
        return "Document has been published"


class Document:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def perform_action(self):
        return self.state.handle()


if __name__ == "__main__":
    document = Document()

    draft_state = DraftState()
    document.set_state(draft_state)
    print(document.perform_action())  # Output: Document is in the draft state

    moderated_state = ModeratedState()
    document.set_state(moderated_state)
    print(document.perform_action())  # Output: Document is in moderation

    published_state = PublishedState()
    document.set_state(published_state)
    print(document.perform_action())  # Output: Document has been published
