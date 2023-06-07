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
               f"от {self.salary['from']}"

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary['from'] > other.salary['from']
        return NotImplemented



    def append_to_list(self, vacancies: list):
        for vacancy in vacancies:
            self.__list_of_vacancies.append(Vacancy(
                id=vacancy['id'],
                url=vacancy['url'],
                name=vacancy['name'],
                salary=vacancy['salary'],
                description=vacancy['description'],
                requirements=vacancy['requirements'],
                area=vacancy['area'],
                platform=vacancy['platform'],
            ))


    def sort_by_salary(self):
        return self.__list_of_vacancies.sort(key=lambda vacancy: vacancy.salary['from'] if vacancy.salary and 'from' in vacancy.salary and
                                                                         vacancy.salary['from'] is not None else float(
            '-inf'), reverse=True)
