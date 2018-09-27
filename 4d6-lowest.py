import random

for x in range(6):
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)
    print(a, b, c, d)
    total = a + b + c + d - min(a, b, c, d)
    print(total)

