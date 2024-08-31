# Crear un diccionario con información de una persona
persona = {
    "nombre": "Santiago",
    "edad": 21,
    "ciudad": "Bogotá",
    "profesión": "Ingeniero",
    "telefono": (3103797832, 3028792802, 3217890828),
    "hobbies": ["motos", "futbol", "bicicleta"],
    "persona_contacto": {
                            "nombre": "Maria",
                            "telefono": (3012782982, 3110897832),
                            "afinidad": "Amiga",
                            "direccion": {
                                            "ciudad": "Cali",
                                            "barrio": "Miraflorez",
                                            "comuna": 19,
                                            "direccion": "Calle 5 # 10-25"
                                        }
                            }
}

# Acceder a un valor mediante su clave
print(persona["nombre"])  # Imprime: Juan
print(persona["telefono"])
print(persona["hobbies"])
print(f"El nombre del acudiente es: {persona['persona_contacto']['nombre']}")
print(f"La direccion del acudiente es: {persona['persona_contacto']['direccion']}")


for telefono in persona['telefono']:
    print(f" ---> {telefono}")
