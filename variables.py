username_for_array: str = "Banderlog_Kiberdvach"

userdata_for_post_test_in_array = {
    "id": 121,
    "username": username_for_array,
    "firstName": "Banderlog",
    "lastName": "Kiberdvach",
    "email": "BK1@test.ru",
    "password": "123321123321",
    "phone": "8999999999",
    "userStatus": 1,
}

userdata_for_put_test_in_array = {
    "id": 121,
    "username": username_for_array,
    "firstName": "Banderlogus",
    "lastName": "Kiberdvachevich",
    "email": "BK11@test.ru",
    "password": "321123321123",
    "phone": "89998887766",
    "userStatus": 0,
}

correct_id_for_single_get_test = 2

inexisting_id_for_single_get_test = 8765456

incorrect_id_for_single_get_test = "гпллрцилал"

new_pet_for_single_post_test = {
    "id": 2,
    "category": {"id": 2, "name": "Кот"},
    "name": "Васян",
    "photoUrls": ["https://photo.com/1"],
    "tags": [{"id": 1, "name": "Дворовый"}, {"id": 2, "name": "Голодный"}],
    "status": "available",
}

pet_for_single_put_test = {
    "id": 2,
    "category": {"id": 1, "name": "Кот"},
    "name": "Васян",
    "photoUrls": ["https://photo.com/1"],
    "tags": [
        {"id": 1, "name": "Дворовый"},
        {"id": 2, "name": "Отъевшийся"},
        {"id": 3, "name": "Довольный"},
    ],
    "status": "available",
}
