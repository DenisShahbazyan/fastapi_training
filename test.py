from enum import StrEnum


class Fruit(StrEnum):
    APPLE = 'Яблоко'
    PEAR = 'Груша'
    PLUM = 'Слива'


for fr in Fruit:
    print(fr.upper())
    # Без наследования от str так не получится:
    # придётся писать fr.value.upper().
