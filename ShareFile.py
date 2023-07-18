from Accounting import Accounting
from Programmer import Programmer
from Sale import Sale

account = Accounting("Non", 35000, 30)
account._showData()
print(account.__str__())
print(f"Salary/Year With Bonus {account._getIncome(50_000)}")

programmer = Programmer("Nini", 50000, 2, "Dev Game")
programmer._showData()
print(programmer.__str__())
print(f"Salary/Year With Bonus {programmer._getIncome(80_000,8_000)}")

sale = Sale("NorNor", 12000, "CNX")
sale._showData()
print(sale.__str__())