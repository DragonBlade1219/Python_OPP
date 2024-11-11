# Decorador que comprueba si un empleado tiene un rol específico.
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            # Si el rol del empleado coincide con el rol requerido:
            if employee.get('role') == required_role:
                return func(employee);
            else:
                print(f"ACCESO DENEGADO. Solo usuarios tipo {required_role} pueden realizar esta acción.");
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Registrando acción para el empleado {employee['name']}.")
        return func(employee)
    return wrapper

@check_access("admin")
@log_action
def delete_employee(employee):
    print(f"el empleado {employee} ha sido eliminado");
    
admin = {"name": "Andrés", "role": "admin"};
employee = {"name": "Reynaldo", "role": "employee"};

delete_employee(admin);
    