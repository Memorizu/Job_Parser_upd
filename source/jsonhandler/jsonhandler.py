import json
from source.base import FileManager
from source.vacancies.vacancy import Vacancy


class JSONHandler(FileManager):

    def __init__(self, vacancies: list):
        self.vacancies = vacancies

    def save(self):
        vacancies = []
        for vacancy in self.vacancies:
            vacancies.extend(vacancy)
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def load_file(self):
        with open('vacancies.json', encoding='utf-8') as f:
            return json.load(f)

    def get_all_vacancies(self):
        vacancies = self.load_file()
        list_of_vacancies = [Vacancy(
            id=vacancy['id'],
            url=vacancy['url'],
            name=vacancy['name'],
            salary=vacancy['salary'],
            description=vacancy['description'],
            requirements=vacancy['requirements'],
            area=vacancy['area'],
            platform=vacancy['platform'],
        ) for vacancy in vacancies]
        return list_of_vacancies

