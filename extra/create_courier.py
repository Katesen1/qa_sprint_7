from extra import const
from extra import data
import requests

def register_new_courier():
    payload = {
        "login": data.login_random,
        "password": data.password_random,
        "firstName": data.first_name_random
    }

    response = requests.post(const.BASE_URL+const.COURIER_HANDLE, data=payload)
    return response
