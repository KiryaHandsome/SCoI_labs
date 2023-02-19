import random


def generate_numbers():
    return random.sample(range(1, 10000), random.randint(5, 15))

