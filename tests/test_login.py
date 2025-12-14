from extra import data
from extra import const
import requests
import pytest
import allure

class TestLogin:
    @allure.title('Проверка логина курьера')
    def test_autorization(self):
        payload = {
            "login": data.login_registered,
            "password": data.password_registered,
        }
        response = requests.post(
            const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload
        )
        assert response.status_code == 200 and "id" in response.text

    @pytest.mark.parametrize(
        "login, password", [(data.login_registered, ""), ("", data.password_registered)]
    )
    def test_autorization_without_field(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload)
        assert response.status_code == 400

    @pytest.mark.parametrize(
        "login, password",
        [("katapes1", data.password_registered), (data.login_registered, "1234")],
    )
    def test_wrong_inputs(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload)
        assert response.status_code == 404
