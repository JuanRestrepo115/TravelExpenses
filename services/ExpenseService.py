from interfaces import iExpenseRepository
from domain import user, expense

class ExpenseService:
    def __init__(self, expense_repository: iExpenseRepository):
        self.expense_repository = expense_repository

    def makeExpense(self, user: user, expense: expense):
        if expense.amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")
        
        self.expense_repository.create(expense)