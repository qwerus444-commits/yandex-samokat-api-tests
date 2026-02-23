# test_order.py
from api_methods import create_order, get_order_by_track

def test_get_order_by_track_returns_200():
    track = create_order()
    response = get_order_by_track(track)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"