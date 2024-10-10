from dicc_finance import *

# Creamos el menu
def main():
    
    #Creamos un diccionario para almacenar las cuentas
    accounts = []


    while True:
        print("Bienvenido a la calculadora")
        print("1. Crear cuenta")
        print("2. Buscar cuenta por nombre")
        print("3. Agregar Transacion")
        print("3. Consultar saldo cuenta")
        print("4. Consultar el saldo total")
        print("3. Mostrar todas la cuentas")
        print("5. Salir")

    #capturar la oipcion de entrada
        try: 
            option = int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("Por favor ingrese la opcion correcta")
            continue
    
        if option == 1:
            name = input("Ingrese el nombre de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta: ")
            create_account(accounts,name, account_type)
            print(f"Cuenta '{name}' creada con el id")
        #buscar cuenta por nombre
        elif option == 2:
            name = input("Ingrese el nombre de la cuenta: ")
            account = find_account_by_name(accounts, name)
            if account:
                print(f"La cuenta {name} existe")
            else:
                print(f"La cuenta {name} no existe")
        #Agregar transaccion
        elif option == 3:
            name = input("Ingrese el nombre de la transaction: ")
            description = input("Ingrese la descripcion de la transaccion: ")
            try:
                amount = float(input("Ingrese el monto de la transaccion: "))
                add_transaction(accounts, description, name, amount)

            except ValueError:  
                print("Por favor ingrese un monto valido")
                continue

        
            
        