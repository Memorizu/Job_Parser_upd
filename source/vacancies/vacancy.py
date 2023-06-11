class Vacancy:
    __list_of_vacancies = []

    def __init__(self,
                 id: str,
                 url: str,
                 name: str,
                 salary: dict,
                 description: str,
                 requirements: str,
                 area: str,
                 platform: str,
                 ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.salary = salary
        self.description = description
        self.requirements = requirements
        self.area = area
        self.platform = platform
        self.__list_of_vacancies = []

    def __str__(self):
        return f"{self.name} \n" \
               f"от {self.salary['from']}\n" \
               f"{self.url}\n" \
               f"Описание вакансии: {self.description}\n" \
               f"Требования: {self.requirements}\n" \
               f"{self.area}\n" \
               f"{self.platform}\n" \
               f"=========================================="

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary['from'] > other.salary['from']
        return NotImplemented


    #
