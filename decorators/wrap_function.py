def wrap(func):
    def wrapped_function(*args, **kwargs):
        print("Antes de ejecutar la función")
        result = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return result
    return wrapped_function

@wrap
def say_hello(name):
    print(f"Hola, {name}!")

say_hello("Mundo")


def wrap_2(func):
    def wrapped_function(*args, **kwargs):
        print("Antes de ejecutar la función")
        result = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return result
    return wrapped_function

def say_hello_2(name):
    print(f"Hola, {name}!")

wrapped_say_hello = wrap_2(say_hello_2)
wrapped_say_hello("Mundo")
