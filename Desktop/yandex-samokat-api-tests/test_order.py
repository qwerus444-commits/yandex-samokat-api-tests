# Капранова Надежда, 40-я когорта — Дипломный проект. 

import requests

BASE_URL = "https://9ad177a6-e29f-4392-b81d-8025f5b088f3.serverhub.praktikum-services.ru"

def create_order():
    response = requests.post(f"{BASE_URL}/api/v1/orders", json={
        "firstName": "Naruto",
        "lastName": "Uzumaki",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    })
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"
    return response.json()["track"]

def get_order(track):
    response = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
    assert response.status_code == 200, f"Ошибка получения заказа: {response.status_code}"
    return response.json()

def test_order_flow():
    track = create_order()
    print(f"Заказ создан, трек: {track}")
    order = get_order(track)
    print("Статус ответа: 200, данные заказа получены")
    print("Тест пройден!")

if __name__ == "__main__":
    test_order_flow()