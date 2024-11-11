def check_access(func):
    def wrapper(employees):
        # Comprobando el rol 'admin'...
        if any(emp["role"] == "admin" for emp in employees.values()):
            return func(employees);
        else:
            print("Acceso Denegado!. Solo los administradores pueden eliminar...");
    return wrapper;
            
@check_access
def delete_employee(employees: dict) -> None:
    print(f"El empleado {employees[1]['name']} ha sido eliminado");
    
employees = {
                1:{"name": "Andrés",
                   "role": "admin"},
                2:{"name": "Reynaldo",
                   "role": "employee"},
                3:{"name": "Cristian",
                   "role": "employee"},
                4:{"name": "Saji",
                   "role": "employee"},
             };

delete_employee(employees);
