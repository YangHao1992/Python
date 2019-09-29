def func(*args):
    total = 0
    for val in args:
        total += val
    return total

print('func():%d' % func())
print('func(1):%d' % func(1))
print('func(1, 2):%d' % func(1, 2))