import pytest
from jose import jwt
from app import schemas

from app.config import settings


@pytest.mark.parametrize('lat, lng',[
    ("42.495137", "-83.237855"),
    ("42.481933", "-83.106192"),
    ("42.819823", "-83.269120")])

def test_create_gps(client, lat, lng):
    print("test_create_gps: " , lat, lng)
    res = client.post("/gps/", json={"lat": lat, "lng": lng})

    new_gps = schemas.GpsOut(**res.json())
    assert res.status_code == 201