from abc import ABC, abstractmethod


class Api(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class FileManager(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_all_vacancies(self):
        pass
