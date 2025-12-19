from extra import const
from extra import data
import requests

def register_new_courier(delete_courier_list):
    payload = {
        "login": data.login_random,
        "password": data.password_random,
        "firstName": data.first_name_random
    }

    response = requests.post(const.BASE_URL+const.COURIER_HANDLE, data=payload)
    delete_courier_list.append((payload["login"], payload["password"]))
    return response, payload["login"], payload["password"]
