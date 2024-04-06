#приклад функції 
def function (name):
    print(f"Hello, {name}")

function("Romko")

#передача функції як аргумент
def square(x):
    return x * x

def a (func, y):
    return func(y)

result = a(square, 4)


