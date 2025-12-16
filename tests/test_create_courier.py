from extra import create_courier
from extra import const
from extra import data
import pytest
import requests
import allure

class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self, delete_courier):
        with allure.step("Создание нового курьера через register_new_courier"):
            response, login, password = create_courier.register_new_courier()
        with allure.step("Проверка статус кода ответа и тела ответа"):
            assert response.status_code == 201 and response.text == '{"ok":true}'
        with allure.step("Удаление тестовых данных"):
            delete_courier(login, password)

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_same_courier(self, delete_courier):
        with allure.step("Подготовка тестовых данных"):
         payload = {
            "login": data.login_registered,
            "password": data.password_registered,
            "firstName": data.first_name_registered,
        }
        with allure.step("Отправка запроса на создание курьера"):
         response = requests.post(const.BASE_URL + const.COURIER_HANDLE, data=payload)
        with allure.step("Отправка запроса на создание курьера с существующими данными"):
         response = requests.post(const.BASE_URL + const.COURIER_HANDLE, data=payload)
        with allure.step("Проверка статус кода ответа"): 
          assert response.status_code == 409


    @allure.title('Проверка, что если одного из полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize(
        "login, password, first_name",
        [
            pytest.param(data.login_random, "", data.first_name_random, id='without_password'),
            pytest.param("", data.password_random, data.first_name_random, id='without_login'),
            pytest.param(data.login_random, data.password_random, "", id='without_first_name'),
        ],
    )
    def test_without_field(self, login, password, first_name, delete_courier):
        with allure.step("Подготовка тестовых данных"):
            payload = {"login": login, "password": password, "firstName": first_name}
        with allure.step("Отправка запроса"):
            response = requests.post(const.BASE_URL + const.COURIER_HANDLE, data=payload)
        with allure.step("Проверка статус кода ответа"): 
            assert response.status_code == 400
        with allure.step("Удаление тестовых данных"):
            delete_courier(payload['login'], payload['password'])