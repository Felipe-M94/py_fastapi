from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "Felipe",
            "email": "felipe@teste.com",
            "password": "password",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "Felipe",
        "email": "felipe@teste.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "Felipe",
                "email": "felipe@teste.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "Felipe Teste",
            "email": "felipe@teste.com",
            "password": "",
            "id": 1,
        },
    )
    assert response.json() == {
        "username": "Felipe Teste",
        "email": "felipe@teste.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted!"}


def test_delete_non_existent_user(client):
    response = client.delete("/users/999")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "USER NOT FOUND"}


def test_update_non_existent_user(client):
    data = {"username": "Felipe Teste", "email": "felipe@teste.com", "password": ""}
    response = client.put("/users/999", json=data)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "USER NOT FOUND"}
