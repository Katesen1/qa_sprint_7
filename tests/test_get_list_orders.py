from extra import const
import requests
import allure

class TestGetListOrders:
    @allure.title('Проверка списка заказов')
    def test_get_list_orders(self):
        response = requests.get(const.BASE_URL+const.ORDERS_HANDLE)
        assert response.status_code == 200 