import string
import random


def print_string(range: int):
    print(
        "".join(
            random.SystemRandom().choice(string.ascii_letters + string.digits)
            for _ in range(64)
        )
    )


def get_string(range: int) -> str:
    return "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(64)
    )
