import random


def color():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    out = "rgb({0},{1},{2})".format(str(x), str(y), str(z))
    return out


ans = color()
print(ans)
