import random
sum = 0
count = 0
for x in range(2, 101, 2):
    if x % 4 == 0:
        count += 1
        # print('This value:%d is eligible',x)
        sum += x
print('The first time sum:%d, count:%d' % (sum, count))

sum = 0
while sum < 100:
    sum += random.randint(1, 100)
print('sum:%d' % sum)