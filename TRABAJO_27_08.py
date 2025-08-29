#Ejercicio 1 — Sistema de becas estudiantiles
#Enunciado
#La universidad desea automatizar la postulación a becas. El programa debe pedir al usuario:
#1.	Nombre y apellido.
#2.	Edad (validada).
#3.	Promedio general (0–10, validado).
#4.	Ingresos familiares mensuales (validado).
#Condiciones:
#•	Si el promedio es menor a 6 → automáticamente rechazado.
#•	Si el promedio es 6 o más:
#o	Si los ingresos familiares < $300.000 → beca completa.
#o	Si los ingresos entre $300.000 y $600.000 → media beca.
#o	Si los ingresos > $600.000 → rechazado.
#Ejemplo de salida
#✔ Juan Pérez, 20 años
#Promedio: 8.2
#Ingresos: $250000
#Resultado: Beca completa
print("--- Sistema de becas estudiantiles ---")
nombre = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio general (0-10): "))
ingresos = float(input("Ingrese sus ingresos familiares mensuales: "))
if promedio < 0 or promedio > 10:
    print("Promedio inválido. Debe estar entre 0 y 10.")
elif edad < 0:
    print("Edad inválida. Debe ser un número positivo.")
else:
    if ingresos < 0:
        print("Ingresos inválidos. Deben ser un número positivo.")
    else:
        if promedio < 6:
            print("Resultado: Rechazado")
        elif ingresos < 300000:
            print("Resultado: Beca completa")
        elif ingresos < 600000:
            print("Resultado: Media beca")
        else:
            print("Resultado: Rechazado")

# Ejercicio 2 — Gestión de turnos hospitalarios
#Enunciado
#Un hospital quiere organizar turnos según el tipo de paciente. El sistema debe pedir:
#1.	Nombre completo.
#2.	DNI (validado).
#3.	Edad.
#4.	Obra social (sí/no).
#5.	Prioridad médica: (1 = emergencia, 2 = urgente, 3 = control).
#Reglas:
# •	Si prioridad = 1 → asignar inmediatamente a guardia (fin del programa).
# •	Si prioridad = 2 →
# o	Si tiene obra social → turno en menos de 24 hs.
# o	Si no tiene obra social → turno en 48 hs.
# •	Si prioridad = 3 →
# o	Si edad > 65 → turno preferencial en 72 hs.
#o	Caso contrario → turno normal en 7 días.
#Ejemplo de salida
#✔ Paciente: María Gómez
#DNI: 30123456
#Edad: 70
#Prioridad: 3
#Turno asignado: Preferencial en 72 hs
print("\n--- Gestión de turnos hospitalarios ---")
bienvenida = "Bienvenido al sistema de gestión de turnos hospitalarios"
print(bienvenida)
paciente = {}
paciente["nombre"] = input("Ingrese su nombre completo: ")
paciente["dni"] = input("Ingrese su DNI (sin puntos): ")
paciente["edad"] = int(input("Ingrese su edad: "))
paciente["obra_social"] = input("¿Tiene obra social? (sí/no): ")
paciente["prioridad"] = int(input("Ingrese su prioridad médica (1=emergencia, 2=urgente, 3=control): "))
if paciente["prioridad"] == 1:
    print(f'✔ Paciente: {paciente["nombre"]}')
    print(f'DNI: {paciente["dni"]}')
    print(f'Edad: {paciente["edad"]}')
    print("Prioridad: 1")
    print("Turno asignado: Guardia inmediata")
elif paciente["prioridad"] == 2:
    if paciente["obra_social"] == "sí":
        print("Turno asignado: Menos de 24 hs")
    else:
        print("Turno asignado: 48 hs")
elif paciente["prioridad"] == 3:
    if paciente["edad"] > 65:
        print("Turno asignado: Preferencial en 72 hs")
    else:
        print("Turno asignado: Normal en 7 días")
else:
    print("Prioridad inválida.")

# Ejercicio 3 — Evaluación de crédito bancario
# Enunciado
# Un banco necesita evaluar créditos personales. El sistema pedirá:
# 1.	Nombre y apellido.
# 2.	CUIT (validado).
# 3.	Ingresos mensuales.
# 4.	Antigüedad laboral (en años).
# 5.	Historial crediticio: bueno / regular / malo.
# Condiciones:
# •	Si historial = malo → rechazo inmediato.
# •	Si ingresos < $200.000 → rechazo.
# •	Si ingresos ≥ $200.000 y antigüedad < 2 años → solo puede pedir hasta $500.000.
# •	Si ingresos ≥ $200.000 y antigüedad ≥ 2 años:
# o	Historial regular → hasta $1.000.000.
# o	Historial bueno → hasta $3.000.000.
# Ejemplo de salida
# ✔ Cliente: Pedro Sánchez
# CUIT: 20-30233444-9
# Ingresos: $280000
# Antigüedad: 3 años
# Historial: bueno
# Monto aprobado: $3,000,000
print("\n--- Evaluación de crédito bancario ---")
bienvenida = "Bienvenido al sistema de evaluación de crédito bancario"
cliente = {}
cliente["nombre"] = input("Ingrese su nombre y apellido: ")
cliente["cuit"] = input("Ingrese su CUIT (sin guiones): ")
cliente["ingresos"] = float(input("Ingrese sus ingresos mensuales: "))
cliente["antiguedad"] = int(input("Ingrese su antigüedad laboral (en años): "))
cliente["historial"] = input("Ingrese su historial crediticio (bueno/regular/malo): ")
if cliente["historial"] == "malo":
    print("Resultado: Rechazado")
elif cliente["ingresos"] < 200000:
    print("Resultado: Rechazado")
elif cliente["ingresos"] >= 200000 and cliente["antiguedad"] < 2:
    print("Monto aprobado: $500,000")
elif cliente["ingresos"] >= 200000 and cliente["antiguedad"] >= 2:
    if cliente["historial"] == "regular":
        print("Monto aprobado: $1,000,000")
    elif cliente["historial"] == "bueno":
        print("Monto aprobado: $3,000,000")
    else:
        print("Historial crediticio inválido.")