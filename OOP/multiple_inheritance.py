class A:
    def __init__(self, x, y, z, *args, **kwargs):
        print(f"A's constructor called: x={x}, y={y}, z={z}")
        super().__init__(*args, **kwargs)

class B:
    def __init__(self, age, salary, *args, **kwargs):
        print(f"B's constructor called: age={age}, salary={salary}")
        super().__init__(*args, **kwargs)

class C(A, B):
    def __init__(self, x, y, z, age, salary):
        print("C's constructor called")
        super().__init__(x, y, z, age, salary)  # Passing all arguments in order

# Create an instance
c = C(1, 2, 3, 25, 50000)
