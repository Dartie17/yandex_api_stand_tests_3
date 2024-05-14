import configuration
import data
import requests

# Запрос на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)

# Запрос на получение ID заказа
def get_order_id(track_num):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers,
                         params=track_num)