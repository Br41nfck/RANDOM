import random


def random_shows():
    with open("texts/shows.txt", encoding = 'utf-8') as file:
        shows = file.readlines()
        return random.choice(shows)


ans = random_shows()
print(ans)
