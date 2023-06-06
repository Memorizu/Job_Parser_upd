import os
import requests
from dotenv import load_dotenv

from source.base import Api
load_dotenv()

class SuperJobAPI(Api):

    __url = 'https://api.superjob.ru/2.0/vacancies/'
    __key = os.getenv('SJ_KEY')


    def __init__(self, keywords: str):
        self.keywords = keywords
        self.headers = {
            "X-Api-App-Id": self.__key,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.params = {
            'keywords': keywords
        }
        self.list_of_vacancies = []

    def get_request(self):
        response = requests.get(self.__url, headers=self.headers, params=self.params)
        return response.json()

    def get_vacancies(self):
        load_dotenv()
        vacancies = self.get_request()
        for vacancy in vacancies['objects']:
            self.__formatted_vacancies(vacancy)
        return self.list_of_vacancies

    def __formatted_vacancies(self, vacancy: dict) -> dict:
        dict['']
        pass

s = SuperJobAPI('python')
print(s.get_vacancies())
