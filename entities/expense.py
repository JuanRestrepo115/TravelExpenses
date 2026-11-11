import datetime


class expense:

    def __init__(self, expense_id: int, trip_id: int, amount: float, description: str, dateE: datetime.date):
        self._expense_id = expense_id
        self._trip_id = trip_id
        self._amount = amount
        self._description = description
        self._dateE = datetime.now().date()


    # Getters and Setters
    @property
    def expense_id(self) -> int:
        return self._expense_id

    @property
    def trip_id(self) -> int:
        return self._trip_id

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def description(self) -> str:
        return self._description

    @property
    def dateE(self) -> datetime.date:
        return self._dateE

    # Setters
    @trip_id.setter
    def trip_id(self, value: int):
        self._trip_id = value

    @amount.setter
    def amount(self, value: float):
        self._amount = value

    @description.setter
    def description(self, value: str):
        self._description = value

    @dateE.setter
    def dateE(self, value: datetime.date):
        self._dateE = value

    def __repr__(self):
        return f"Expense(expense_id={self._expense_id}, trip_id={self._trip_id}, amount={self._amount}, description='{self._description}')"