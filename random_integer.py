import random


def random_integer():
    a = input("start:")
    b = input("end:")
    print(random.randint(int(a), int(b)))


random_integer()
