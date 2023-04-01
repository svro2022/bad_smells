# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

from enum import Enum


class Direction:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class State(Enum):
    FLY = 1.2
    CRAWL = 0.5


class Unit:

    # ...
    def __init__(self, field):
        self.x = 0
        self.y = 0
        self.field = field
        self.state: State = State.FLY
        self.speed = 0

    def change_state(self, new_state):
        self.state = new_state
        self._get_speed()

    def move(self, direction: Direction):

        if direction == Direction.UP:
            self.field.set_unit(y=self.y + self.speed, x=self.x, unit=self)
        elif direction == Direction.DOWN:
            self.field.set_unit(y=self.y - self.speed, x=self.x, unit=self)
        elif direction == Direction.LEFT:
            self.field.set_unit(y=self.y, x=self.x - self.speed, unit=self)
        elif direction == Direction.RIGHT:
            self.field.set_unit(y=self.y, x=self.x + self.speed, unit=self)

    def _get_speed(self):
        if self.state == State.FLY:
            self.speed *= self.state.value
        elif self.state == State.CRAWL:
            self.speed *= self.state.value
        else:
            raise ValueError('Эк тебя раскорячило')

