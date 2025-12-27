import requests


def test_get_user_and_assert_status_code_404():
    response = requests.get("https://petstore.swagger.io/v2/user/Banderlog_Kiberdvach")
    print(response.status_code, response.json())
    assert response.status_code == 404


def test_post_add_new_user_with_correct_data():
    new_userdata = {
        'id': 121,
        'username': 'Banderlog_Kiberdvach',
        'firstName': 'Banderlog',
        "lastName": 'Kiberdvach',
        'email': 'BK1@test.ru',
        'password': '123321123321',
        'phone': '8999999999',
        'userStatus': 1
    }
    response = requests.post(url="https://petstore.swagger.io/v2/user", json=new_userdata)
    print(response.text)
    assert response.status_code == 200
    response_body = response.json()
    print(response_body["message"])


def test_get_added_user_and_assert_status_code_200():
    response = requests.get("https://petstore.swagger.io/v2/user/Banderlog_Kiberdvach")
    print(response.status_code, response.json())
    assert response.status_code == 200


def test_put_update_existing_user():
    updated_userdata = {
        'id': 121,
        'username': 'Banderlog_Kiberdvach',
        'firstName': 'Banderlogus',
        'lastName': 'Kiberdvachevich',
        'email': 'BK11@test.ru',
        'password': '321123321123',
        'phone': '89998887766',
        'userStatus': 0
    }
    response = requests.put(url="https://petstore.swagger.io/v2/user/Banderlog_Kiberdvach", json=updated_userdata)
    assert response.status_code == 200
    print(response.status_code, response.json())


def test_delete_existing_user():
    response = requests.delete(url="https://petstore.swagger.io/v2/user/Banderlog_Kiberdvach")
    print(response.status_code, response.json())

def test_get_deleted_user_and_assert_status_code_404():
    response = requests.get("https://petstore.swagger.io/v2/user/Banderlog_Kiberdvach")
    print(response.status_code, response.json())
    assert response.status_code == 404