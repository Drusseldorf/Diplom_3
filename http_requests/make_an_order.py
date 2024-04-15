import requests as r
import allure

from data import URL
from http_requests.models.make_an_order_model import MakeOrder
from helpers.model_validate import Validate


class Order:
    MAKE_ORDER_URL = URL.MAIN_PAGE_URL + '/api/orders'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    @allure.step('Создание заказа')
    def create(cls, access_token) -> MakeOrder:

        headers = cls.HEADERS.copy()
        headers.update({'Authorization': access_token})

        ingredients = {
            "ingredients": [
                "61c0c5a71d1f82001bdaaa6f",
                "61c0c5a71d1f82001bdaaa70"
            ]
        }

        response = r.post(cls.MAKE_ORDER_URL, json=ingredients, headers=headers)

        return Validate.get_model_response(MakeOrder, response)
