'''
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance 
methods. Incomes is a set of incomes and its description. The same goes for expenses.
'''


class PersonAccount:

    def __init__(self, first_name: str, last_name: str, balance: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.__balance = balance
        self.__incomes = list()
        self.__expenses = list()

        self.__incomes.append(balance)
        self.__expenses.append(0)

    def total_income(self) -> float:
        return sum(self.__incomes)

    def total_expense(self) -> float:
        return sum(self.__expenses)

    def account_info(self) -> str:
        return f'{self.first_name} {self.last_name} has {self.__balance} €'

    def add_income(self, income: float) -> None:
        self.__balance += income
        self.__incomes.append(income)

    def add_expense(self, expense: float) -> None:
        self.__balance -= expense
        self.__expenses.append(expense)

    def account_balance(self) -> str:
        return f'The balance is {self.total_income() - self.total_expense()}'


ruben = PersonAccount('Ruben', 'Blanco', 1000)
print(ruben.account_balance())
ruben.add_expense(50)
print(ruben.account_balance())
print(ruben.account_info())
