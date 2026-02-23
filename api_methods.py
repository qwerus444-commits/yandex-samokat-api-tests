import requests
from configuration import BASE_URL, ORDER_DATA

def create_order():
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=ORDER_DATA)
    response.raise_for_status()
    return response.json()["track"]

def get_order_by_track(track):
    return requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})