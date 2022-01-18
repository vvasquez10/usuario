"""
Para esta tarea, agregaremos algunas funciones a la clase Usuario:
hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
Ej.: “Usuario: Guido van Rossum, Balance: $150
BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega
esa cantidad al balance de otro_usuario 
"""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.balance = 0
    
    def hacer_retiro(self, amount):
        if self.balance < amount:
            print("No cuenta con el saldo suficiente para realizar la operación.")
        else:
            self.balance -= amount 
            print("Retiro realizado correctamente.")
        return self

    def hacer_deposito(self, amount):
        self.balance += amount 
        print("Deposito realizado correctamente.")
        return self


    def mostrar_balance_usuario(self):
        print("Usuario:", self.nombre, self.apellido, "- Balance:", self.balance)
        return self


    def transfer_dinero(self, other_user, amount):
        if self.balance < amount:
            print("No cuenta con el saldo suficiente para realizar la operación.")
        else:
            other_user.balance += amount
            self.balance -=amount
        return self

