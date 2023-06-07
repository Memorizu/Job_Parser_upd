import json

from source.base import FileManager
from source.hh_api.headhunter_api import HHApi
from source.sj_api.superjob_api import SJApi


class JSONHandler(FileManager):

    def __init__(self, platforms: list):
        self.platforms = platforms

    def save(self):
        vacancies = []
        for api in self.platforms:
            vacancies.extend(api.get_vacancies())
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_all_vacancies(self):
        with open('vacancies.json', 'r', encoding='utf-8') as f:
            return json.load(f)

