class iExpenseRepository:

    def create(self, expense):
        raise NotImplementedError

    def getby_id(self, expense_id: int):
        raise NotImplementedError

    def update(self, expense):
        raise NotImplementedError