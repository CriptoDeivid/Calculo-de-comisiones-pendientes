import pandas as pd
from itertools import combinations

def find_combinations(file_path, column_name, target_number):
    # Cargar el archivo Excel
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return
    
    # Verificar si la columna existe
    if column_name not in df.columns:
        print(f"La columna '{column_name}' no existe en el archivo.")
        return

    # Obtener los números de la columna
    numbers = df[column_name].dropna().tolist()

    # Validar que los datos sean numéricos
    if not all(isinstance(num, (int, float)) for num in numbers):
        print("La columna contiene valores no numéricos.")
        return

    # Generar todas las combinaciones y sus sumas
    closest_combination = None
    closest_difference = float('inf')
    exact_matches = []
    
    for r in range(1, len(numbers) + 1):  # Generar combinaciones de tamaño 1 hasta len(numbers)
        for combo in combinations(numbers, r):
            total = sum(combo)
            difference = abs(target_number - total)
            
            if total == target_number:
                exact_matches.append(combo)
            elif difference < closest_difference:
                closest_difference = difference
                closest_combination = combo

    # Resultados
    if exact_matches:
        print(f"Combinaciones exactas que suman {target_number}:")
        for match in exact_matches:
            print(match)
    else:
        print(f"No se encontraron combinaciones exactas. La combinación más cercana es {closest_combination} con suma {sum(closest_combination)}.")

# Parámetros específicos
file_path = '/mnt/c/Users/David/Desktop/arb/expedientes.xlsx'
column_name = 'comisiones'
target_number = 291

# Llamar a la función
find_combinations(file_path, column_name, target_number)
