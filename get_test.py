import requests
import json

correct_id = 2
inexisting_id = 8765456
incorrect_id = 'гпллрцилал'


# Позитивные кейсы========================================================================

def test_get_pet_by_correct_id():
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{correct_id}")
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(f'\nКод ответа: {response.status_code}')
    print(formatted_json)


# Негативные кейсы=======================================================================


def test_get_pet_by_correct_inexisting_id():  # Пока не созданы записи, успешно отрабатывает только этот
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{inexisting_id}")
    assert response.status_code == 404
    formatted_json = json.dumps(response.json(), indent=4)
    print(f'\nКод ответа: {response.status_code}')
    print(formatted_json)


def test_get_pet_by_incorrect_id_type():  # Выдает 405 вместо ожидаемого 400
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{incorrect_id}")
    assert response.status_code == 400
    formatted_json = json.dumps(response.json(), indent=4)
    print(f'\nКод ответа: {response.status_code}')
    print(formatted_json)
