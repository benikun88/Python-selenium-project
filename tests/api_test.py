import allure
import requests
import pytest
import uuid

from answers.api_calls import ApiRequests


@allure.feature("API Tests")
@allure.story("Customer Management")
@pytest.mark.api
class TestApi:
    # Credentials
    consumer_key = "u5gkmvsnxvc5w6qxoy2iwx98mkc1j30d"
    consumer_secret = "brpz2fvopf9fcdlkqh6dlbh8ui5lqow6"
    access_token = "55yrut70u8qgvkvaw7xc9yvokhs09ztw"
    access_token_secret = "64ueg9agxzzy4pgsxd73qqnj7f36lkom"

    # Base URL
    base_url = "https://magento.softwaretestingboard.com/rest/default/V1"

    # Common headers
    common_headers = {
        "Content-Type": "application/json",
        "Host": "magento.softwaretestingboard.com",
        # "Content-Length": "69",
        "Cookie": "PHPSESSID=827611b7d87be75f321673ab0c102a07",
        "User-Agent": "Chrome/111.0.5575.46"
    }

    # Generate random email
    random_email = f"jdoe{uuid.uuid4().hex[:6]}@example.com"

    # Create customer payload
    customer_payload = {
        "customer": {
            "email": random_email,
            "firstname": "Jane",
            "lastname": "Doe",
            "addresses": [{
                "defaultShipping": True,
                "defaultBilling": True,
                "firstname": "Jane",
                "lastname": "Doe",
                "region": {
                    "regionCode": "NY",
                    "region": "New York",
                    "regionId": 43
                },
                "postcode": "10755",
                "street": ["123 Oak Ave"],
                "city": "Purchase",
                "telephone": "512-555-1111",
                "countryId": "US"
            }]
        },
        "password": "Password1"
    }

    # Customer token payload
    token_payload = {
        "username": random_email,
        "password": "Password1"
    }

    @pytest.fixture
    def customer_token(self):
        url = f"{self.base_url}/integration/customer/token/"
        response = ApiRequests.post(url, json=self.token_payload, headers=self.common_headers)
        assert response.status_code == 200, f"Failed to create customer token: {response.text}"
        return response.json()

    @allure.description("Test creating a customer via API.")
    def test_create_customer(self):
        url = f"{self.base_url}/customers"
        response = ApiRequests.post(url, json=self.customer_payload, headers=self.common_headers)
        assert response.status_code == 200, f"Failed to create customer: {response.text}"
        customer_id = response.json()["id"]
        assert customer_id is not None, "Customer ID not received"

    @allure.description("Test get customer info")
    def test_get_customer_info(self, customer_token):
        url = f"{self.base_url}/customers/me"
        headers = {
            **self.common_headers,
            "Authorization": f"Bearer {customer_token}",
        }
        response = ApiRequests.get(url, headers=headers)
        assert response.status_code == 200, f"Failed to get customer info: {response.text}"
        customer_info = response.json()
        assert customer_info["email"] == self.random_email, "Incorrect customer email"

    def test_create_customer_invalid_email(self):
        invalid_email_payload = self.customer_payload.copy()
        invalid_email_payload["customer"]["email"] = "invalid_email"
        url = f"{self.base_url}/customers"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}",
            "Host": "magento.softwaretestingboard.com",
            "Content-Length": "69",
            "Cookie": "PHPSESSID=827611b7d87be75f321673ab0c102a07",
            "User-Agent": "Chrome/111.0.5575.46"
        }
        response = ApiRequests.post(url, json=invalid_email_payload, headers=headers)
        assert response.status_code == 400, ("Expected 400 Bad Request for invalid email but received different status "
                                             "code")
