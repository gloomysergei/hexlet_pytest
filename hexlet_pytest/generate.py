import random
import string


# BEGIN (write your solution here)
def generate_password(lenght=5, include_uppercase=False, include_digits=False, include_special=False):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars_uppercase = string.ascii_uppercase
        chars += chars_uppercase + 10
    if include_digits:
        chars_digits = string.digits
        chars += chars_digits
    if include_special:
        chars_special = string.punctuation
        chars += chars_special
    password = ''.join(random.choice(chars) for _ in range(lenght))
    return password
# END