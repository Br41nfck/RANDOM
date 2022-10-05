import random


def random_phone_number():
    phone = ""
    for i in range(11):
        phone = phone + "".join(str(random.randint(0, 9)))
    return phone

# ans = random_phone_number()
# print(ans)
