import random
from datetime import datetime, timedelta


def random_datetime(min_year=1, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days = 365 * years)

    out = str(start + (end - start) * random.random())
    out = out[:10][::-1] + out[10:-7]
    return out


print(random_datetime())
