import requests
import json


#  Позитивные кейсы ================================================================


def test_post_create_new_correct_pet():
    new_pet = {
        "id": 2,
        "category": {
            "id": 2,
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
                "name": "Голодный"
            }
        ],
        "status": "available"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=new_pet)
    assert response.status_code == 200
    formatted_json = json.dumps(response.json(),indent=4, ensure_ascii=False)
    print(f'\nКод ответа: {response.status_code}')
    print(formatted_json)