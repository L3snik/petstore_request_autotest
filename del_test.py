import json

import requests


def test_delete_remove_existing_pet():
    response = requests.delete("https://petstore.swagger.io/v2/pet/2")
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(f"\n{formatted_json}")
