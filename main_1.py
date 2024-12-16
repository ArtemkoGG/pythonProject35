def limit(max_calls):
    def decorator(func):
        calls = [0]
        def wrapper(a, b):
            if calls[0] < max_calls:
                calls[0] += 1
                return func(a, b)
            print(f"Досягнуто Лімі викликів ({max_calls}).")
        return wrapper
    return decorator

@limit(3)
def dobavlyaemo(a, b):
    return a + b

print(dobavlyaemo(3, 5))
print(dobavlyaemo(2, 4))
print(dobavlyaemo(1, 1))
print(dobavlyaemo(3, 2))