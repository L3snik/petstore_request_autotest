import json

import requests

from variables import correct_id_for_single_get_test as correct_id
from variables import incorrect_id_for_single_get_test as incorrect_id
from variables import inexisting_id_for_single_get_test as inexisting_id


def test_get_pet_by_correct_id():
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{correct_id}")
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(f"\nКод ответа: {response.status_code}")
    print(formatted_json)


def test_get_pet_by_correct_inexisting_id():  # Пока не созданы записи, успешно отрабатывает только этот
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{inexisting_id}")
    assert response.status_code == 404
    formatted_json = json.dumps(response.json(), indent=4)
    print(f"\nКод ответа: {response.status_code}")
    print(formatted_json)


def test_get_pet_by_incorrect_id_type():  # Выдает 405 вместо ожидаемого 400
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{incorrect_id}")
    assert response.status_code == 400
    formatted_json = json.dumps(response.json(), indent=4)
    print(f"\nКод ответа: {response.status_code}")
    print(formatted_json)
