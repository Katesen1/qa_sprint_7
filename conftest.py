import pytest

@pytest.fixture
def delete_courier():
    courier_data = []
    yield courier_data 
    import requests
    from extra import const
    for login, password in courier_data:
        try:
            login_response = requests.post(
                const.BASE_URL + const.LOGIN_COURIER_HANDLE,
                json={"login": login, "password": password}
            )
            
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                requests.delete(f"{const.BASE_URL}/api/v1/courier/{courier_id}")
        except Exception:
            pass