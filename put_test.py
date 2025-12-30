import json

import requests

from variables import pet_for_single_put_test as pet


def test_put_edit_existing_pet():
    response = requests.put("https://petstore.swagger.io/v2/pet", json=pet)
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(f"\nКод ответа: {response.status_code}")
    print(formatted_json)
