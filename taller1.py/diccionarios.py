#1
#tienda de ropa
'''tienda_ropa = {
    "camisas": ["talla S", "talla M", "talla L"],
    "pantalones": ["talla 32", "talla 34", "talla 36"],
    "accesorios": {
        "gorros": ["negro", "blanco", "gris"],
        "bufandas": ("rojo", "azul", "verde"),
    },
    "stock_total": 100
}

print("Lista de tallas de camisas:", tienda_ropa["camisas"])
print("Colores de bufandas disponibles:", tienda_ropa["accesorios"]["bufandas"])
print("Stock total:", tienda_ropa["stock_total"])'''


#2
#biblioteca
'''biblioteca = {
    "secciones": ["Ficción", "Ciencia", "Historia"],
    "libros": {
        "Ficción": ["Cien años de soledad", "El Quijote"],
        "Ciencia": ["Breve historia del tiempo", "El gen egoísta"],
        "Historia": ["Sapiens", "El arte de la guerra"]
    },
    "prestamos": {
        "2024-01-01": ("Juan", "Cien años de soledad"),
        "2024-02-15": ("María", "Sapiens")
    },
    "capacidad_maxima": 500
}

print("Secciones de la biblioteca:", biblioteca["secciones"])
print("Libros de la sección de Ciencia:", biblioteca["libros"]["Ciencia"])
print("Préstamos del 2024-02-15:", biblioteca["prestamos"]["2024-02-15"])'''


#3
#estudiante

estudiante = {
    "nombre": "Maria",
    "edad": 21,
    "cursos": ["Matemáticas", "Programación", "Historia"],
    "notas": {
        "Matemáticas": (4.5, 4.8, 5.0),
        "Programación": (4.7, 4.9, 5.0),
        "Historia": (4.3, 4.6, 4.7)
    },
    "detalles_contacto": {
        "email": "maria@example.com",
        "telefono": "3017837822"
    }
}

print("Nombre del estudiante:", estudiante["nombre"])
print("Notas en Programación:", estudiante["notas"]["Programación"])
print("Email de contacto:", estudiante["detalles_contacto"]["email"])
