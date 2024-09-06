from finance import create_account, add_transaction, get_account_balance, get_total_balance
# Creamos el menu
def main():
    
    #Creamos un diccionario para almacenar las cuentas
    accounts = []


    while True:
        print("Bienvenido a la calculadora")
        print("1. Crear cuenta")
        print("2. Agregar Transacion")
        print("3. Consultar saldo cuenta")
        print("4. Consultar el saldo total")
        print("5. Salir")

    #capturar la oipcion de entrada
        option = int(input("Ingrese la opcion deseada: "))

        #Creamos una cuenta
        if option == 1:
            name = input("Ingrese el nombre de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta: ")
            account_id = create_account(accounts,name, account_type)
            print(f"Cuenta '{name}' creada con el id {account_id}")

        #Agregar transaccion
        elif option == 2:
            account_id = int(input("Ingrese el id de la cuenta: "))
            description = input("Ingrese la descripcion de la transaccion: ")
            amount = float(input("Ingrese el monto de la transaccion: "))
            add_transaction(accounts,description, account_id, amount)
            print(f"Transaccion de {amount} realizada en la cuenta {account_id}")

        #Consultar saldo de la cuenta
        elif option == 3:
            account_id = int(input("Ingrese el id de la cuenta: "))
            balance = get_account_balance(accounts, account_id)
            print(f"El saldo de la cuenta {account_id} es {balance}")
        
        

        #Consultar saldo total
        elif option == 4:
            total_balance = get_total_balance(accounts)
            print(f"El saldo total de las cuentas es {total_balance}")
        
        elif option ==  5:
            print("Gracias por usar la calculadora")
            #salimos del ciclo
            break
        
        #Opcion invalida
        else:
            print("opcion invalida, por favor intenta de nuevo")


if __name__ == "__main__":
    main()