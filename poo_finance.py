class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description
    

class Account:
    def __init__(self, name, account_type):
        self.name = name.lower()
        self.account_type = account_type
        self.transactions = []

    def add_transaction(self, description, amount):
        self.transactions.append(Transaction(description, amount))

    def calculate_transactions_total(self, transaction_type):
        if transaction_type not in ['ingreso','egreso']:
            return None
        
        total = 0
        for transaction in self.transactions:
            if (transaction_type == 'ingreso' and transaction.amount > 0) or (transaction_type == 'egreso' and transaction.amount < 0):
                total += transaction.amount
        return total

    def get_balance(self):
        ingresos = self.calculate_transactions_total('ingreso')
        egresos = self.calculate_transactions_total('egreso')   
        balance = (ingresos if ingresos else 0) + (egresos if egresos else 0)
        return balance
    
class Bank:
    def __init__(self):
        self.accounts = []
    
    def create_account(self, name, account_type):
        for account in self.accounts:
            if account.name == name.lower():
                return None
        new_account = Account(name, account_type)
        self.accounts.append(new_account)
        return new_account
    
    def find_account_name(self, name):
        for account in self.accounts:
            if account.name == name.lower():
                return account
            
    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)

    