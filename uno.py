from collections import Counter #Uso de biblioteca que cuenta elementos

# Función para llenar un vector de hasta 5 elementos
def llenar_vector(nombre_vector):
    vector = []
    print(f"\nIngresa hasta 5 números para el {nombre_vector}, sino ponga 'fin':")
    while len(vector) < 5:
        dato = input(f"Número {len(vector) + 1}: ")
        if dato.lower()=='fin':
            break
        try:
            vector.append(int(dato))
        except ValueError:
            print("Por favor ingresa un número válido.")
    return vector

# Función para encontrar elementos repetidos en un vector
def numero_mas_frecuente(vector):
    contador = Counter(vector)
    return [num for num, cantidad in contador.items() if cantidad > 1]

# Determinar vectores
vector1 = llenar_vector("vector 1")
vector2 = llenar_vector("vector 2")

# Numero que se repite en cada vector
repetidos_v1 = numero_mas_frecuente(vector1)
repetidos_v2 = numero_mas_frecuente(vector2)


#Resultados
print("\n--- RESULTADOS ---")
print(f"Vector 1: {vector1}")
print(f"Repetidos en vector 1: {repetidos_v1 if repetidos_v1 else 'Ninguno'}")

print(f"\nVector 2: {vector2}")
print(f"Repetidos en vector 2: {repetidos_v2 if repetidos_v2 else 'Ninguno'}")


