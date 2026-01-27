import random
import string


# missing digits
def generate_password(
    length=5, include_uppercase=False, include_digits=False, include_special=False
):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special:
        characters += string.special

    return "".join(random.choice(characters) for _ in range(length))