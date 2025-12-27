import requests
import json


#  Позитивные кейсы ================================================================


def test_put_edit_existing_pet():
    pet = {
        "id": 2,
        "category": {
            "id": 1,
            "name": "Кот"
        },
        "name": "Васян",
        "photoUrls": [
            "https://photo.com/1"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Дворовый"
            },
            {
                "id": 2,
                "name": "Отъевшийся"
            },
            {
                "id": 3,
                "name": "Довольный"
            }
        ],
        "status": "available"
    }
    response = requests.put("https://petstore.swagger.io/v2/pet", json=pet)
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(),indent=4, ensure_ascii=False)
    print(f'\nКод ответа: {response.status_code}')
    print(formatted_json)