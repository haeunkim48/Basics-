def remote_control_next ():
    yield 'cnn'
    yield 'bbc'

# create a generator using Fibonacci
def fib():
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a + b

for f in fib():
    if f > 13:
        break 
    print (f)

#     Create Generator method such that every time it will returns a next square number
def square ():
    a = 1
    while True: 
        yield a*a
        a += 1
        

for s in square ():
    if s > 100:
        break 
    print (s)

     