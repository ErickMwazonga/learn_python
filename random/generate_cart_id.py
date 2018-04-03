import random
import string

used_cart_ids = []

def generate_cart_id():
    cart_id = ''
    # characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghiklmnopqrstuvwxyz1234567890!@#$%^&*()'
    characters = string.ascii_letters + string.punctuation
    cart_id_length = 50

    for i in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]

    return used_cart_ids


print(generate_cart_id())
