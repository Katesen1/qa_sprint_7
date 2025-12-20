import random
import string 

login_registered = 'kotopes1'
password_registered = '12345'
first_name_registered = 'kot'

login_random = ''.join(random.choices(string.ascii_lowercase, k=5))
password_random = random.randint(10000, 90000)
first_name_random = ''.join(random.choices(string.ascii_lowercase, k=5))

COMMON_ORDER_DATA = {
    "firstName": "Test",
    "lastName": "User", 
    "address": "Test Address",
    "metroStation": 4,
    "phone": "+79998887766",
    "rentTime": 3,
    "deliveryDate": "2024-12-25",
    "comment": "Test order"
}

COLOR = [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []]