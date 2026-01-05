class Item:
    _id: int
    _name: str
    _weight: str
    _qty: int
    _price: int

    def __init__(self, id: int, name: str, weight: str, qty: int, price: int) -> None:
        self._id = id
        self._name = name
        self._weight = weight
        self._qty = qty
        self._price = price

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def weight(self) -> str:
        return self._weight

    @weight.setter
    def weight(self, value: str) -> None:
        self._weight = value

    @property
    def qty(self) -> int:
        return self._qty

    @qty.setter
    def qty(self, value: int) -> None:
        self._qty = value

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        self._price = value
