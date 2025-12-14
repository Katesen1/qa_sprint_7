from extra import create_courier
from extra import const
from extra import data
import pytest
import requests
import allure

class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self):
        response = create_courier.register_new_courier()
        assert response.status_code == 201 and response.text == '{"ok":true}'

    def test_same_courier(self):
        payload = {
            "login": data.login_registered,
            "password": data.password_registered,
            "firstName": data.first_name_registered,
        }
        response = requests.post(const.BASE_URL + const.COURIER_HANDLE, data=payload)
        assert response.status_code == 409

    @pytest.mark.parametrize(
        "login, password, first_name",
        [
            pytest.param(data.login_random, "", data.first_name_random, id='without_password'),
            pytest.param("", data.password_random, data.first_name_random, id='without_login'),
            pytest.param(data.login_random, data.password_random, "", id='without_first_name'),
        ],
    )
    def test_without_field(self, login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(const.BASE_URL + const.COURIER_HANDLE, data=payload)
        assert response.status_code == 400
