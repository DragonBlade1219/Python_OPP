def log_employee_action(func):
    def wrapper(employee):
        with open('log.txt', 'a') as my_file:
            my_file.write(f"1.- {employee.name} - {employee.accion}")
            my_file.write("\n")
            print(f"1.- {employee.name} - {employee.accion}")
        return func(employee)
    return wrapper

class Employee:
    name: str
    accion: str

    def __init__(self, name: str, accion: str) -> str:
        self.name = name
        self.accion = accion

    @log_employee_action
    def acciones(self):
        print(f'2.- {self.name} realizó la acción {self.accion}')

emp1 = Employee('Andrés', 'ingresa')
emp2 = Employee('Daniel', 'sale')
emp1.acciones()
emp2.acciones()