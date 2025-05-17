import json
import csv
from datetime import datetime

class AnimeDataProcessor:
    def __init__(self):
        self.field_mapping = {
            'Título': 'titulo',
            'Puntuación': 'puntuacion',
            'Géneros': 'generos',
            'Año': 'fecha_inicio'
        }
    
    def read_data_file(self, filename):
        """Lee archivos CSV con manejo robusto de errores"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            raise Exception(f"Error leyendo archivo: {str(e)}")
    
    def process_data(self, raw_data):
        """Convierte los datos a la estructura esperada"""
        processed = []
        for record in raw_data:
            try:
                new_record = {}
                for csv_field, expected_field in self.field_mapping.items():
                    new_record[expected_field] = record.get(csv_field, 'N/A')
                processed.append(new_record)
            except Exception as e:
                print(f"Error procesando registro: {str(e)}")
                continue
        return processed
    
    def save_to_json(self, data, filename='anime_processed.json'):
        """Guarda los datos procesados en JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\nDatos guardados en: {filename}")
            return filename
        except Exception as e:
            print(f"\nError guardando archivo JSON: {str(e)}")
            return None

def main():
    processor = AnimeDataProcessor()
    
    print("=== Analizador de Datos de Anime ===")
    print("Este script procesa los archivos CSV y prepara los datos para análisis")
    
    try:
        filename = input("\nIngrese el nombre del archivo CSV a analizar: ").strip()
        
        print("\n[1/4] Leyendo archivo de datos...")
        raw_data = processor.read_data_file(filename)
        
        print("[2/4] Procesando datos...")
        processed_data = processor.process_data(raw_data)
        
        if not processed_data:
            print("\nNo hay datos válidos para procesar")
            return
        
        print("[3/4] Mostrando primer registro...")
        print("\nDatos del primer registro (estructura procesada):")
        for key, value in processed_data[0].items():
            print(f"- {key}: {value}")
        
        print("[4/4] Guardando datos procesados...")
        json_file = processor.save_to_json(processed_data)
        
        if json_file:
            print("\n¡Proceso completado exitosamente!")
            print("\nEjecuta ahora SEM4.py para generar el análisis y visualizaciones")
        
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()