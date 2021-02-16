import random
def randInt(min=0, max=100):
    if (min > max):
        num = random.randint(max, min)
        return num
    if (min == max):
        return min
    num = random.randint(min, max)
    return num

print(randInt())
print(randInt(1, 5))
print(randInt(5, 55))
print(randInt(10, 1))
print(randInt(-5, -10))
print(randInt(5, 5))
print(randInt(10, -5))
