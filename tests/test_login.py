from extra import data
from extra import const
from extra import create_courier
import requests
import pytest
import allure


class TestLogin:
    @allure.title("Проверка авторизации курьера")
    def test_autorization(self, delete_courier):
        with allure.step("Создание нового курьера через register_new_courier"):
            response, login, password = create_courier.register_new_courier(delete_courier)
        with allure.step("Подготовка данных"):
            payload = {
                "login": login,
                "password": password,
            }
        with allure.step("Отправка запроса"):
            response = requests.post(const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload)
        with allure.step("Проверка статуса твета и нахождение id в содержании ответа"):
            assert response.status_code == 200 and "id" in response.text

    @pytest.mark.parametrize("login, password", [(data.login_registered, ""), ("", data.password_registered)])
    @allure.title("Проверка возникновения ошибки авторизации при пустом одном поле")
    def test_autorization_without_field(self, login, password):
        with allure.step("Подготовка данных"):
            payload = {"login": login, "password": password}
        with allure.step("Отправка запроса"):
            response = requests.post(const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 400

    @allure.title("Проверка возникновения ошибки при введении неправильных данных")
    @pytest.mark.parametrize(
        "login, password",
        [("katapes1", data.password_registered), (data.login_registered, "1234")],
    )
    def test_wrong_inputs(self, login, password):
        with allure.step("Подготовка данных"):
            payload = {"login": login, "password": password}
        with allure.step("Отправка запроса"):
            response = requests.post(const.BASE_URL + const.LOGIN_COURIER_HANDLE, data=payload)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 404
