#HW6

arg = 'asd'
def find_class():
    print(type(arg))

find_class()

arg1 = 7778
def trans_float():
    return float(arg1)

try:
    print(trans_float())
except ValueError:
    print(0)

x = 'asd'
y = 4
def operation_with_arg():
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        return x - y
    if isinstance(x, str) and isinstance(y, str):
        return f'{x}{y}'
    elif isinstance(x, str) and not isinstance(y, str):
        result = {x: y}
    else:
        result = (x, y)
    return result

print(operation_with_arg())