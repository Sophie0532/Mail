# [Tus imports y funciones anteriores se mantienen igual...]

# Esta parte se mantiene igual
aggregated_file = process_files(base_directory,os.listdir(base_directory))

# Verificar los datos (esto se mantiene)
aggregated_file['Source'].value_counts()

# 👇 AQUÍ REEMPLAZAS LAS LÍNEAS PROBLEMÁTICAS 👇
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
