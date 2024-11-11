def log_employee_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('acciones_empleados.txt', 'a') as archivo:
            archivo.write(f"Acción: {func.__name__}, Argumentos: {args}, {kwargs}\n")
        return result
    return wrapper

@log_employee_action
def realizar_accion_empleado(accion):
    print(f"Empleado realizó la acción: {accion}")
    
realizar_accion_empleado("Iniciar turno")
realizar_accion_empleado("Finalizar turno")