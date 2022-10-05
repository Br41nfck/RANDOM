import random


def random_city():
    with open("texts/list_cities.txt", encoding = 'utf-8') as file:
        city = file.readlines()
        file.close()
        return random.choice(city)


ans = random_city()
print(ans)
