from extra import const
import pytest
import requests 

@pytest.fixture
def delete_courier():
    def delete(login, password):
        login_response = requests.post(
            const.BASE_URL+const.LOGIN_COURIER_HANDLE,
            json={"login": login, "password": password}
        )
        
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f"{const.BASE_URL}/api/v1/courier/{courier_id}")
    
    return delete