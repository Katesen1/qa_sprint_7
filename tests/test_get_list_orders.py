from extra import const
import requests
import allure

class TestGetListOrders:
    @allure.title('Проверка возвращения списка заказов')
    def test_get_list_orders(self):
        with allure.step("Отправка запроса получения списка заказов"):
            response = requests.get(const.BASE_URL+const.ORDERS_HANDLE)
        with allure.step("Получение кода ответа"):
            assert response.status_code == 200
        with allure.step("Преобразуем в json"):
            data = response.json()
        with allure.step("Проверка, что получили именно словарь и в нем есть слово orders"):
            assert isinstance(data, dict) and 'orders' in data

    