from abc import ABC, abstractmethod


class Api(ABC):

    def connect(self):
        pass

    def get_vacancies(self):
        pass


class FileManager(ABC):

    def save(self):
        pass

    def delete(self):
        pass
