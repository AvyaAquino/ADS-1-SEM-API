def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
a = fib()
for i in range(5):
    print (next(a), end = ' ')