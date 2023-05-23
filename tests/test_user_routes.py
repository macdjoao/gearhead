from tests.utilities import generate_headers, clear_bd
from faker import Faker
import requests
import json

fake = Faker()

email = fake.safe_email()
first_name = fake.first_name()
last_name = fake.last_name()
password = email
url = "http://localhost:5000/api/v1/user"
payload = json.dumps({
    "email": email,
    "first_name": first_name,
    "last_name": last_name,
    "password": password
})


def test_post_user():
    response = (requests.request(
        "POST", url, headers=generate_headers(), data=payload)).json()

    assert response["email"] == email
    assert response["first_name"] == first_name
    assert response["last_name"] == last_name

    clear_bd(url=url, id=response["id"])


# def test_post_user_fail():
#     response = (requests.request(
#         "POST", url, headers=generate_headers(), data=payload)).text

#     # Deve falhar pois o email (criado em test_post_user) já existe
#     assert response == 'Create Error.'
