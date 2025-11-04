import pandas as pd 
import numpy as np 
import os
from datetime import datetime 

base_directory = r'Y:\\REGULATORIO MERCADOS\\DODD FRANK\\BAU DFA\\ESTRATEGICO 2025\\06. JUNIO\\Ficheros'

def read_file_to_df(filepath):
    if filepath.endswith('xlsx'):
        # If such a sheet is found, read it; otherwise, read the second sheet (index 1)
        df = pd.read_excel(filepath, dtype=str)
        # Add the source filename to the DataFrame
        filename = os.path.basename(filepath)
        df['Source'] = filename
        return df

def process_files(directory, file_list):
    dataframes = []
    for filename in file_list:
        print(f"Processing file: {filename}")
        df = read_file_to_df(os.path.join(directory, filename))
        dataframes.append(df)
    aggregated_df = pd.concat(dataframes)
    return aggregated_df

# Procesar los archivos
aggregated_file = process_files(base_directory, os.listdir(base_directory))

# Verificar los conteos por archivo
print(aggregated_file['Source'].value_counts())

# NUEVA PARTE MEJORADA - GUARDADO CON MANEJO DE ERRORES
output_file_name = f'DFA_Junio_Acumulado.xlsx'
file_path = os.path.join(base_directory, output_file_name)

try:
    # Intentar con openpyxl primero
    aggregated_file.to_excel(file_path, index=False, engine='openpyxl')
    print("✅ Archivo guardado exitosamente con openpyxl")
    
except Exception as e:
    print(f"⚠️ Error con openpyxl: {e}")
    print("Intentando con xlsxwriter...")
    
    try:
        aggregated_file.to_excel(file_path, index=False, engine='xlsxwriter')
        print("✅ Archivo guardado exitosamente con xlsxwriter")
        
    except Exception as e2:
        print(f"❌ Error con xlsxwriter: {e2}")
        print("Intentando guardar como CSV como respaldo...")
        
        # Guardar como CSV como última opción
        csv_file = file_path.replace('.xlsx', '.csv')
        aggregated_file.to_csv(csv_file, index=False, encoding='utf-8-sig')
        print(f"✅ Datos guardados como CSV: {csv_file}")

print("Proceso completado.")
