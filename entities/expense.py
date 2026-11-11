class expense:

    def __init__(self, expense_id: int, trip_id: int, amount: float, description: str):
        self._expense_id = expense_id
        self._trip_id = trip_id
        self._amount = amount
        self._description = description


    # Getters and Setters
    def get_expense_id(self):
        return self._expense_id

    def get_trip_id(self):
        return self._trip_id

    def get_amount(self):
        return self._amount

    def get_description(self):
        return self._description

    def set_expense_id(self, expense_id: int):
        self._expense_id = expense_id

    def set_trip_id(self, trip_id: int):
        self._trip_id = trip_id

    def set_amount(self, amount: float):
        self._amount = amount

    def set_description(self, description: str):
        self._description = description 

    def __repr__(self):
        return f"Expense(expense_id={self._expense_id}, trip_id={self._trip_id}, amount={self._amount}, description='{self._description}')"