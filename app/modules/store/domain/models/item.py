class Item:
    _id: int
    _name: str
    _weight: str
    _qty: int

    def __init__(self, id: int, name: str, weight: str, qty: int) -> None:
        self._id = id
        self._name = name
        self._weight = weight
        self._qty = qty

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
