def log(func):
    def wrapper(a, b):
        print(f"Викликано '{func.name}' з a={a}, b={b}")
        result = func(a, b)
        print(f"'{func.name}' поверне {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

result = add(3, 5)