import json

import requests

from source.base import Api


class HHApi(Api):
    __url = 'https://api.hh.ru/vacancies'

    def __init__(self, keywords: str):

        self.keywords = keywords
        self.params = {
            'text': keywords,
            'per_page': 50,
            'page': 0,
            'items': [{}]
        }
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.list_of_vacancies = []

    @property
    def get_request(self):
        response = requests.get(self.__url, params=self.params, headers=self.__headers)
        return response.json()

    def get_vacancies(self):
        self.params['page'] = 0
        self.list_of_vacancies = []

        while True:
            vacancies = self.get_request

            if 'items' not in vacancies:
                break

            for vacancy in vacancies['items']:
                formatted_vacancy = self.__formatted_vacancy(vacancy)
                self.list_of_vacancies.append(formatted_vacancy)
                self.params['page'] += 1
            if not self.list_of_vacancies:
                return 'Нет совпадений по вакансиям'
        return self.list_of_vacancies

    @staticmethod
    def __formatted_vacancy(vacancy: dict) -> dict:
        new_vacancy = {
            'id': vacancy['id'],
            'url': vacancy['alternate_url'],
            'name': vacancy['name'],
            'salary': vacancy['salary'],
            'description': vacancy['snippet']['responsibility'],
            'requirements': vacancy['snippet']['requirement'],
            'area': vacancy['area']['name'],
            'platform': 'HHApi',
        }
        return new_vacancy


# hh = HHApi('python')

# print(hh.testing())
# print(hh.get_request)
# print(len(hh.get_request))
# print(type(hh.get_request))
# print(hh.get_vacancies())
# print(len(hh.list_of_vacancies))
# for i in hh.list_of_vacancies:
#     print(i.name)

