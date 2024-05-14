# Алексей Богданов, 16-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Проверка возможности получения данных о созданном заказе по его треку
def test_create_order_assert():
    track_num = "t=" + str(sender_stand_request.post_new_order().json()["track"])
    order_id_response = sender_stand_request.get_order_id(track_num)
    assert order_id_response.status_code == 200