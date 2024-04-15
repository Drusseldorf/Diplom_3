import allure
import requests as r

from data import URL
from helpers.model_validate import Validate
from http_requests.models.user_model import RegisterUser


class User:

    REGISTER_URL = URL.MAIN_PAGE_URL + '/api/auth/register'
    DELETE_URL = URL.MAIN_PAGE_URL + '/api/auth/user'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    @allure.step('Регистрация пользователя')
    def register(cls, **kwargs):

        response = r.post(cls.REGISTER_URL, json=kwargs, headers=cls.HEADERS)

        return Validate.get_model_response(RegisterUser, response)

    @classmethod
    @allure.step('Удаление пользователя')
    def delete(cls, access_token):

        headers = {'Authorization': access_token}

        response = r.delete(cls.DELETE_URL, headers=headers)

        return response
