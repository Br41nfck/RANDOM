import random


def random_names():
    with open("texts/names.txt", encoding = 'utf-8') as file:
        names = file.readlines()
        return random.choice(names)


ans = random_names()
print(ans)
