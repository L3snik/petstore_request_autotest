import requests
import json
from colorama import Fore

username = 'Banderlog_Kiberdvach'
def test_get_user_and_assert_status_code_404():
    response = requests.get(url=f"https://petstore.swagger.io/v2/user/{username}")
    assert response.status_code == 404
    response_message = response.json()["message"]
    print(Fore.CYAN + f"\nПроверяем, что юзера с логином {username} не существует" +
          Fore.RESET + f"\nКод ответа: {response.status_code}"
          f"\nСообщение: {response_message}")


def test_post_add_new_user_with_correct_data():
    new_userdata = {
        'id': 121,
        'username': username,
        'firstName': 'Banderlog',
        "lastName": 'Kiberdvach',
        'email': 'BK1@test.ru',
        'password': '123321123321',
        'phone': '8999999999',
        'userStatus': 1
    }
    response = requests.post(url=f"https://petstore.swagger.io/v2/user", json=new_userdata)
    assert response.status_code == 200
    print(Fore.CYAN + f"\nДобавляем юзера с логином {username}" +
          Fore.RESET + f"\nКод ответа: {response.status_code}")


def test_get_added_user_and_assert_status_code_200():
    response = requests.get(url=f"https://petstore.swagger.io/v2/user/{username}")
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(Fore.CYAN + f"\nПроверяем, что юзер с логином {username} добавлен" +
          Fore.RESET + f"\nКод ответа: {response.status_code}"
          f"\nОтвет:\n{formatted_json}")


def test_put_update_existing_user():
    updated_userdata = {
        'id': 121,
        'username': username,
        'firstName': 'Banderlogus',
        'lastName': 'Kiberdvachevich',
        'email': 'BK11@test.ru',
        'password': '321123321123',
        'phone': '89998887766',
        'userStatus': 0
    }
    response = requests.put(url=f"https://petstore.swagger.io/v2/user/{username}", json=updated_userdata)
    assert response.status_code == 200
    print(Fore.CYAN + f"\nОбновляем данные юзера с логином {username}: " +
          Fore.RESET + f"\nКод ответа: {response.status_code}")


def test_get_updated_user_and_assert_status_code_200():
    response = requests.get(url=f"https://petstore.swagger.io/v2/user/{username}")
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(Fore.CYAN + f"\nПроверяем, что данные юзера с логином {username} обновлены:" +
          Fore.RESET + f"\nКод ответа: {response.status_code}"
          f"\nОтвет:\n{formatted_json}")


def test_delete_existing_user():
    response = requests.delete(url=f"https://petstore.swagger.io/v2/user/{username}")
    print(Fore.CYAN + f"\nУдаляем юзера с логином {username}" +
          Fore.RESET + f"\nКод ответа: {response.status_code}")


def test_get_deleted_user_and_assert_status_code_404():
    response = requests.get(url=f"https://petstore.swagger.io/v2/user/{username}")
    assert response.status_code == 404
    response_message = response.json()["message"]
    print(Fore.CYAN + f"\nПроверяем, что юзера с логином {username} больше не существует" +
          Fore.RESET + f"\nКод ответа: {response.status_code}"
          f"\nСообщение: {response_message}")
