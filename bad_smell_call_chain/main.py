# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Address:
    room = 42
    street = ''
    city = ''
    country = ''
    city_population = 100500


class Person:
    def __init__(self, address: Address):
        self.address = address

    def get_person_room(self):
        return self.address.room

    def get_city_population(self):
        return self.address.city_population


