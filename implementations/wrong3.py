import random
import string


# missing specials
def generate_password(
    length=0, include_uppercase=True, include_digits=True, include_special=True
):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))