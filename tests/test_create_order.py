from extra import const
from extra import data 
import pytest
import requests
import allure


class TestOrder:
    @allure.title('Проверка создания заказа с разным выбором цвета')
    @pytest.mark.parametrize('color_variant', data.COLOR)
    def test_create_order(self, color_variant):
        with allure.step("Подготовка данных"):
            payload = data.COMMON_ORDER_DATA
            payload["color"] = color_variant
        with allure.step("Отправка запроса"):
            response = requests.post(const.BASE_URL + const.ORDERS_HANDLE, json=payload)
        with allure.step("Проверка статуса кода и наличие track в содержании ответа"):
            assert response.status_code == 201 and "track" in response.text
