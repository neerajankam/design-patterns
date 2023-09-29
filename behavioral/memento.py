"""
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.


The Memento pattern provides several benefits in software design, especially when it comes to managing and restoring the state of objects.
Here are three key benefits of the Memento pattern:

1) State Preservation: The primary purpose of the Memento pattern is to capture and preserve the internal state of an object without exposing its internal structure.
This allows you to save an object's state at a specific point in time, which can be valuable for implementing features like undo/redo functionality or checkpoints in applications. It ensures that you can restore an object to a previous state if needed.

2) Separation of Concerns: The Memento pattern promotes a clean separation of concerns by isolating the state-saving and state-restoring functionality into
separate classes. This separation ensures that the core business logic of an object isn't cluttered with state management code.
It adheres to the Single Responsibility Principle (SRP), making the codebase more maintainable and modular.

3) Undo/Redo Functionality: One of the most common use cases of the Memento pattern is implementing undo and redo functionality.
By saving a series of Mementos as the user performs actions, you can easily revert to previous states when the user requests an undo operation.
This feature enhances the user experience in applications where users expect the ability to reverse their actions.
"""


class EditorMemento:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class Editor:
    def __init__(self):
        self.content = ""
        self.mementos = []
        self.current = 0

    def write(self, words):
        self.content += words

    def save(self):
        memento = EditorMemento(self.content)
        self.mementos.append(memento)
        self.current += 1
        return memento

    def restore(self, index):
        memento = self.mementos[index]
        self.content = memento.get_content()

    def undo(self):
        if self.current > 0:
            self.current -= 1
            memento = self.mementos[self.current]
            self.content = memento.get_content()


if __name__ == "__main__":
    editor = Editor()

    editor.write("Hello ")
    editor.save()

    editor.write("world!")
    m2 = editor.save()

    editor.write(" This is second sentence.")
    m3 = editor.save()

    editor.write(" This is third sentence.")
    print(
        editor.content
    )  # Hello world! This is second sentence. This is third sentence.

    editor.undo()
    print(editor.content)  # Hello world! This is second sentence.

    editor.undo()
    print(editor.content)  # Hello world!
