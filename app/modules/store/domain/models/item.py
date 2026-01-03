class Item:
    __id: int
    __name: str
    __weight: str
    __qty: int

    def __init__(self, id: int, name: str, weight: str, qty: int) -> None:
        self.__id = id
        self.__name = name
        self.__weight = weight
        self.__qty = qty

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, value: str) -> None:
        self.__weight = value

    @property
    def qty(self) -> int:
        return self.__qty

    @qty.setter
    def qty(self, value: int) -> None:
        self.__qty = value
