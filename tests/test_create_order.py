from extra import const
import pytest
import requests
import json
import allure

class TestOrder:
    @allure.title('Проверка создания заказа с разным выбором цвета')
    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color",
        [
            pytest.param(
                "Kotopes",
                "kotopesov",
                "saratov",
                4,
                "+78564321965",
                3,
                "25-12-2025",
                "dont be late",
                ["BLACK"],
                id="black",
            ),
            pytest.param(
                "Kotopes",
                "kotopesov",
                "saratov",
                4,
                "+78564321965",
                3,
                "25.12.2025",
                "dont be late",
                ["GREY"],
                id="grey",
            ),
            pytest.param(
                "Kotopes",
                "kotopesov",
                "saratov",
                4,
                "+78564321965",
                3,
                "25.12.2025",
                "dont be late",
                ["BLACK", "GREY"],
                id="both",
            ),
            pytest.param(
                "Kotopes",
                "kotopesov",
                "saratov",
                4,
                "+78564321965",
                3,
                "25.12.2025",
                "dont be late",
                "",
                id="empty",
            ),
        ],
    )
    def test_create_order(
        self,
        firstName,
        lastName,
        address,
        metroStation,
        phone,
        rentTime,
        deliveryDate,
        comment,
        color,
    ):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color,
        }

        response = requests.post(const.BASE_URL + const.ORDERS_HANDLE, data=json.dumps(payload))
        assert response.status_code == 201 and "track" in response.text
