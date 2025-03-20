
"""
Does Python support Compile-Time Polymorphism (Method Overloading)?
No, Python does NOT support true method overloading like Java or C++.

In languages like Java, you can define multiple methods with the same name but different parameters.
Python doesn’t allow this. If you define multiple methods with the same name in a class, only the last one is kept.
✅ Example: Python does NOT support method overloading

"""

class Example:
    def show(self, x):
        print(f"Single argument: {x}")

    def show(self, x, y):  # This will overwrite the previous `show` method
        print(f"Two arguments: {x}, {y}")

obj = Example()
# obj.show(10)  # ❌ Error! (The first method is overwritten)
obj.show(10, 20)  # ✅ Works because only the last method exists


"""
How can we achieve similar behavior in Python?
Python handles this using default arguments or *args (variable arguments).
"""

class Example:
    def show(self, x, y=None):  # Default argument allows optional parameter
        if y is None:
            print(f"Single argument: {x}")
        else:
            print(f"Two arguments: {x}, {y}")

obj = Example()
obj.show(10)        # ✅ Works
obj.show(10, 20)    # ✅ Works

"""
Run-Time Polymorphism (Method Overriding)
Python does support method overriding, which is Run-Time Polymorphism.
"""


class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):  # Overriding Parent method
        print("This is Child class")

obj = Child()
obj.show()  # ✅ Calls the overridden method in Child class


"""
🎯 Key Takeaways:
Python does NOT support true method overloading. You can use default arguments or *args instead.
Python supports method overriding (Run-Time Polymorphism).
Overloading in Python is simulated using dynamic typing. Functions can accept different argument types without needing multiple method definitions.
"""