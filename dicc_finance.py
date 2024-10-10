
global_accounts_id = 0

def create_account(accounts, name, account_type):
    
    global global_accounts_id
    account = {
        "id": global_accounts_id,
        "name": name,
        "type": account_type,
        "transactions": []
    }
    # Agregamos la cuenta al diccionario de cuentas
    accounts.append(account)
    global_accounts_id += 1
    # Retornamos el id de la cuenta
    return accounts ['id']

def find_account_by_name(accounts, account_name):
    for account in accounts:
        if account['name'] == account_name:
            return account
    return None


def add_transaction(accounts, description, account_name, amount):
    account = find_account_by_name(accounts, account_name)
    if account:
        account['transactions'].append({"description": description,"amount": amount})
    else:
        print(f"La cuenta {account_name} no existe")


#funcion para clacular las transacciones de una cuenta

def calculate_transactions(account):
    return sum(transaction['amount'] for transaction in account['transactions'])



def get_account_balance(accounts, account_name):
    account = find_account_by_name(accounts, account_name)
    if account:
        balance  = calculate_transactions(account)
        return balance
    else:
        print(f"La cuenta {account_name} no existe")
        return None
    
