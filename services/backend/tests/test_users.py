def test_create_user(client):
    stub = {
        "username": "test@user.com",
        "full_name": "Test User",
        "password": "string",
        "superuser": False,
        "active": True,
    }
    response = client.post(url="/users/register", json=stub)
    assert response.status_code == 200

def test_deleter_user(client):
    username = "test@user.com"
    user = client.get(f"/users/{username}")
    id = user.json()["id"]
    response = client.delete(f"/users/{id}")
    assert response.status_code == 200