# Luis Adrián Hinojos Chávez
# Práctica 6 - Fundamentos de Machine Learning
# p6-fundamentos-1344.py

print("======================================")
print("PRACTICA 6 - FUNDAMENTOS DE ML")
print("======================================")

# ======================================
# 1. VARIABLES
# ======================================

print("\n--- 1. VARIABLES ---")

print("\nEjemplo 1:")
nombre = "Adrian"
print("Nombre:", nombre)

print("\nEjemplo 2:")
edad = 18
print("Edad:", edad)

print("\nEjemplo 3:")
estatura = 1.75
print("Estatura:", estatura)


# ======================================
# 2. VARIABLES MÚLTIPLES
# ======================================

print("\n--- 2. VARIABLES MULTIPLES ---")

print("\nEjemplo 1:")
x, y, z = 10, 20, 30
print("x =", x)
print("y =", y)
print("z =", z)

print("\nEjemplo 2:")
nombre, edad, ciudad = "Adrian", 18, "Juarez"
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

print("\nEjemplo 3:")
a = b = c = 100
print("a =", a)
print("b =", b)
print("c =", c)


# ======================================
# 3. TIPOS DE DATOS
# ======================================

print("\n--- 3. TIPOS DE DATOS ---")

print("\nEjemplo 1:")
nombre = "Adrian"
print("Dato:", nombre)
print("Tipo:", type(nombre))

print("\nEjemplo 2:")
edad = 18
print("Dato:", edad)
print("Tipo:", type(edad))

print("\nEjemplo 3:")
precio = 25.50
print("Dato:", precio)
print("Tipo:", type(precio))


# ======================================
# 4. OPERADORES ARITMÉTICOS
# ======================================

print("\n--- 4. OPERADORES ARITMETICOS ---")

a = 10
b = 5

print("\nEjemplo 1 - Suma:")
print(a, "+", b, "=", a + b)

print("\nEjemplo 2 - Resta:")
print(a, "-", b, "=", a - b)

print("\nEjemplo 3 - Multiplicación:")
print(a, "*", b, "=", a * b)


# ======================================
# 5. OPERADORES DE COMPARACIÓN
# ======================================

print("\n--- 5. OPERADORES DE COMPARACION ---")

a = 10
b = 5

print("\nEjemplo 1 - Igualdad:")
print(a, "==", b, ":", a == b)

print("\nEjemplo 2 - Mayor que:")
print(a, ">", b, ":", a > b)

print("\nEjemplo 3 - Menor que:")
print(a, "<", b, ":", a < b)


# ======================================
# 6. OPERADORES LÓGICOS
# ======================================

print("\n--- 6. OPERADORES LOGICOS ---")

edad = 18
tiene_identificacion = True

print("\nEjemplo 1 - AND:")
print(edad >= 18 and tiene_identificacion)

print("\nEjemplo 2 - OR:")
es_estudiante = True
tiene_beca = False
print(es_estudiante or tiene_beca)

print("\nEjemplo 3 - NOT:")
activo = True
print(not activo)


print("\n======================================")
print("FIN DE LA PRACTICA")
print("======================================")
print("programa realizado por Adrian Hinojos1344")
