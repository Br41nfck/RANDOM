import random


def random_movies():
    with open("texts/movies.txt", encoding = 'utf-8') as file:
        movies = file.readlines()
        return random.choice(movies)


ans = random_movies()
print(ans)
