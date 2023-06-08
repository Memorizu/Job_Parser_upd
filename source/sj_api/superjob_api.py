import json
import os
import requests
from dotenv import load_dotenv

from source.base import Api
load_dotenv()


class SJApi(Api):

    __url = 'https://api.superjob.ru/2.0/vacancies/'
    __key = os.getenv('SJ_KEY')

    def __init__(self, keywords: str):
        self.keywords = keywords
        self.headers = {
            "X-Api-App-Id": self.__key,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.params = {
            'page': 0,
            'count': 100,
            'keywords': keywords
        }
        self.list_of_vacancies = []

    def get_request(self):
        response = requests.get(self.__url, headers=self.headers, params=self.params)
        return response.json()

    def get_vacancies(self):
        self.params['page'] = 0

        while True:
            vacancies = self.get_request()
            if 'objects' not in vacancies:
                break

            for vacancy in vacancies['objects']:
                formatted_vacancies = self.__formatted_vacancies(vacancy)
                self.list_of_vacancies.append(formatted_vacancies)
            self.params['page'] += 1

            if not self.list_of_vacancies:
                return 'Нет совпадений по вакансиям'

            return self.list_of_vacancies

    @staticmethod
    def __formatted_vacancies(vacancy: dict) -> dict:
        new_vacancy = {
            'id': vacancy['id'],
            'url': vacancy['link'],
            'name': vacancy['profession'],
            'salary': {'from': vacancy['payment_from'], 'to': vacancy['payment_to']},
            'description': vacancy['candidat'],
            'requirements': None,
            'area': vacancy['place_of_work']['title'],
            'platform': 'SJApi',
        }
        return new_vacancy



