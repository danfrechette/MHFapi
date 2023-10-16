import pytest
from jose import jwt
from app import schemas

from app.config import settings


def test_create_clubs(client,test_create_multiple_users):
    print("test_create_multiple_users: ")

    assert True