import json
from typing import Any

import requests

from source.base import Api
from source.vacancies.hh_vacancy import HHVacancy


class HHApi(Api):
    __url = 'https://api.hh.ru/vacancies'

    def __init__(self, keywords: Any):

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
        return json.dumps(response.json(), indent=3, ensure_ascii=False)

    # def get_vacancies(self):
    #     self.params['page'] = 0
    #     self.list_of_vacancies = []
    #     while True:
    #         vacancies = self.get_request
    #
    #         if 'items' not in vacancies:
    #             break
    #
    #         for vacancy in vacancies['items']:
    #
    #             if vacancy['name'] and vacancy['snippet']['responsibility']:
    #                 if self.keywords.lower() in vacancy['name'].lower() or self.keywords.lower() in vacancy['snippet']['responsibility'].lower():
    #                     self.list_of_vacancies.append(
    #                         HHVacancy(
    #                             id=vacancy['id'],
    #                             name=vacancy['name'],
    #                             salary=vacancy['salary'],
    #                             description=vacancy['snippet']['responsibility'],
    #                             requirements=vacancy['snippet']['requirement']
    #                         )
    #                     )
    #             print(f'прочитана {self.params["page"]} страница')
    #             self.params['page'] += 1
    #
    #         if not self.list_of_vacancies:
    #             return 'Нет совпадений по вакансиям.'
    #     return self.list_of_vacancies


hh = HHApi('продавец')

# print(hh.testing())
print(hh.get_request)
# print(hh.get_vacancies())
# for i in hh.list_of_vacancies:
#     print(i.name)

