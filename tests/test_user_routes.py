from tests.utilities import generate_headers, clear_db
from faker import Faker
import requests
import json

fake = Faker()


url = "http://localhost:5000/api/v1/user"


def test_post_user():
    email = fake.safe_email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = email
    payload = json.dumps({
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    })

    response = (requests.request(
        "POST", url, headers=generate_headers(), data=payload)).json()

    assert response["email"] == email
    assert response["first_name"] == first_name
    assert response["last_name"] == last_name

    clear_db(url=url, id=response["id"])


def test_post_user_fail():
    email = fake.safe_email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = email
    payload = json.dumps({
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    })

    new_user = requests.request(
        "POST", url, headers=generate_headers(), data=payload).json()

    # Attempting to create a new record using the same email used in new_user (must fail)
    response = (requests.request(
        "POST", url, headers=generate_headers(), data=payload)).text

    assert response == 'Create Error.'

    clear_db(url=url, id=new_user["id"])
