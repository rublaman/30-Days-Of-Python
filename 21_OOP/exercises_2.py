'''
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance 
methods. Incomes is a set of incomes and its description. The same goes for expenses.
'''


class PersonAccount:

    def __init__(self, first_name, last_name, incomes, expenses_properties) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses_properties = expenses_properties

        def total_income() -> float:
            pass

        def total_expense() -> float:
            pass

        def account_info() -> str:
            pass

        def add_income(income: float):
            pass

        def add_expense(expense: float):
            pass

        def account_balance() -> str:
            pass
