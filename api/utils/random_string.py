import string
import random

print(
    "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(64)
    )
)
