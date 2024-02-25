# Configurations for API tests

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

# Create customer payload
customer_payload = {
    "customer": {
        "email": "jdoe69@example.com",
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
    "username": "jdoe@example999.com",
    "password": "Password1"
}
