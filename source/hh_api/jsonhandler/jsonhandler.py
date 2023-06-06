import json

from source.base import FileManager


class JSONHandler(FileManager):

    def __init__(self, platforms: list):
        self.platforms = platforms

    def save(self):
        for vacancy in self.platforms.get_vacancies():
            with open('./vacancies', 'w', encoding='utf-8') as f:
                json.dump(vacancy, f, indent=4, ensure_ascii=False)


    def delete(self):
        pass

