#Password generator


import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

chosen = random.sample(characters,6)
password = "".join(chosen)
print(password)