import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    }
}
    "978-84-204-1625-4": {
    "título": "Orgullo y prejuicio",
    "autor" : ["Jane Austen"]
    "generos": ["Novela Romantica"]
    }
     "978-84-376-0494-6": {
        "título": "El principito",
        "autor": ["Antonie de saint"],
        "géneros": ["Novela corta", "fabula"]
    } 
    "978-84-376-0494-7": {
        "título": "Frankenstein",
        "autor": ["Mary Shelley"],
        "géneros": ["Novela gotica", "terror"]
    }
     "978-84-376-0494-8": {
        "título": "El despertar",
        "autor": ["Kate chopion"],
        "géneros": ["Novela feminista"]
    }
     "978-84-376-0494-10": {
        "título": "El club de la buena estrella",
        "autor": ["Amy Tan"],
        "géneros": ["Novela literaria"]
    },
#
isbn = "978-84-376-0494-"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)
#
import os

carpeta = "C:/Users/juan/Documentos/ejemplo"
for i, archivo in enumerate(os.listdir(carpeta), start=1):
    ruta_antigua = os.path.join(carpeta, archivo)
    ruta_nueva = os.path.join(carpeta, f"archivo_{i}.txt")
    os.rename(ruta_antigua, ruta_nueva)

print("Archivos renombrados con éxito.")
#
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)  # [4, 16, 36]
#
def contador(limite):
    n = 1
    while n <= limite:
        yield n
        n += 1
#
for numero in contador(5):
    print(numero)
colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores, start=1):
    print(f"{indice}: {color}")
