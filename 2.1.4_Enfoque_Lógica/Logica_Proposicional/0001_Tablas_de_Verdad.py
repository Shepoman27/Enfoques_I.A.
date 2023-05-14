# Función para generar la tabla de verdad
def truth_table(n, func):
    table = []
    for i in range(2**n):
        row = []
        for j in range(n):
            row.append((i // (2 ** j)) % 2)
        row.append(func(*row))
        table.append(row)
    return table

# Operaciones lógicas
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

# Ejemplos de uso
table_and = truth_table(2, AND)
table_or = truth_table(2, OR)
table_not = truth_table(1, NOT)
table_xor = truth_table(2, XOR)

# Impresión de las tablas de verdad
print("Tabla de verdad para la operación AND:")
for row in table_and:
    print(row)
    
print("\nTabla de verdad para la operación OR:")
for row in table_or:
    print(row)
    
print("\nTabla de verdad para la operación NOT:")
for row in table_not:
    print(row)
    
print("\nTabla de verdad para la operación XOR:")
for row in table_xor:
    print(row)
