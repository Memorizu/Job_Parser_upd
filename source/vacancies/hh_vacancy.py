from source.base import Vacancy


class HHVacancy(Vacancy):

    def __init__(self,
                 id: str,
                 name: str,
                 salary: int,
                 description: str,
                 requirements: str
                 ) -> None:
        self.id = id
        self.name = name
        self.salary = salary
        self.description = description
        self.requirements = requirements

