def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            print('原函数调用后')
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name,age):
    print(f"Hello, {name}+{age}!")

greet("Alice",18)
