import random

nouns = []
adjectives = []


def random_sentence():
    with open("texts/nouns.txt") as fnoun:
        nns = fnoun.readlines()
        fnoun.close()
    with open("texts/adjectives.txt") as fadj:
        adjs = fadj.readlines()
        fadj.close()

    out = random.choice(adjs)[:-1] + " " + random.choice(nns)
    return out


ans = random_sentence()
print(ans)
