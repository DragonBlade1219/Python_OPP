
# Función para imprimir la jerarquía de Exepciones en Pythonen Español:
exception_descriptions = {
    'Exception': 'Clase base para todas las excepciones.',
    'ArithmeticError': 'Errores numéricos.',
    'FloatingPointError': 'Error en operaciones de punto flotante.',
    'OverflowError': 'Resultado de una operación numérica demasiado grande para ser representado.',
    'ZeroDivisionError': 'División por cero.',
    'AssertionError': 'Error en una declaración assert.',
    'AttributeError': 'Fallo al intentar acceder a un atributo de un objeto.',
    'BufferError': 'Errores relacionados con el buffer.',
    'EOFError': 'Fin de archivo alcanzado sin datos adicionales.',
    'ImportError': 'Fallo al importar un módulo.',
    'IndexError': 'Índice fuera del rango en una secuencia.',
    'KeyError': 'Clave no encontrada en un diccionario.',
    'KeyboardInterrupt': 'Interrupción del programa por el usuario.',
    'MemoryError': 'Fallo al intentar asignar memoria.',
    'NameError': 'Nombre no encontrado en el ámbito local o global.',
    'OSError': 'Errores del sistema operativo.',
    'RuntimeError': 'Error que no pertenece a ninguna otra categoría.',
    'StopIteration': 'Señala el final de una iteración.',
    'SyntaxError': 'Error en la sintaxis del código.',
    'IndentationError': 'Error en la indentación del código.',
    'TabError': 'Error en la mezcla de tabulaciones y espacios en la indentación.',
    'SystemError': 'Error interno del intérprete de Python.',
    'TypeError': 'Operación o función aplicada a un objeto de tipo inapropiado.',
    'ValueError': 'Valor inapropiado.',
    'UnicodeError': 'Errores relacionados con la codificación y decodificación de Unicode.',
    'Warning': 'Clase base para advertencias.',
}

# Función para imprimir la jerarquía de Exepciones en Python en Inglés:
def print_exception_hierarchy_EN(exception_class, indent=0):
    description = exception_class.__doc__.strip() if exception_class.__doc__ else 'No description available.'
    print(' ' * indent + f"└─ {exception_class.__name__}: {description}")
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy_EN(subclass, indent + 4)
        
def print_exception_hierarchy_ES(exception_class, indent=0):
    description = exception_descriptions.get(exception_class.__name__, 'Descripción no disponible.')
    print(' ' * indent + f"└─ {exception_class.__name__}: {description}")
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy_ES(subclass, indent + 4)


# Imprimir la jerarquía comenzando desde la clase base Exception en Español.
print_exception_hierarchy_ES(Exception)


# Imprimir la jerarquía comenzando desde la clase base Exception en Inglés.
print_exception_hierarchy_EN(Exception)
