import json

import requests

from variables import new_pet_for_single_post_test as new_pet


def test_post_create_new_correct_pet():
    response = requests.post("https://petstore.swagger.io/v2/pet", json=new_pet)
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(f"\nКод ответа: {response.status_code}")
    print(formatted_json)
