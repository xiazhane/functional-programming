def compose (f,g):
    return lambda *args: f(g(*args))
def add_two(x):
    return x+2
def multiply_by_three(x):
    return x*3
composed_function=compose(multiply_by_three,add_two)
result=composed_function(5)
print(result)