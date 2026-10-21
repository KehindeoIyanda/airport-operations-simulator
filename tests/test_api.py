from app.api import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "Online"


def test_flights_endpoint():
    client = app.test_client()
    response = client.get('/flights')


    assert response.status_code == 200
    assert len(response.json) == 3
    assert response.json[0]["flight_number"] == "FL101"
