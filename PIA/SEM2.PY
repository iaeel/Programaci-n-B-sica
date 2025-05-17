import requests
import re
import json
import csv
from datetime import datetime

class AnimeDataProcessor:
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4"
        self.valid_genres = [
            "Action", "Adventure", "Comedy", "Drama", "Ecchi", "Fantasy",
            "Horror", "Mahou Shoujo", "Mecha", "Music", "Mystery",
            "Psychological", "Romance", "Sci-Fi", "Slice of Life",
            "Sports", "Supernatural", "Thriller"
        ]
    
    def validate_input(self, input_str, pattern):
        """Valida entrada con expresiones regulares"""
        if not re.match(pattern, input_str):
            raise ValueError(f"Formato de entrada inválido. Debe coincidir con: {pattern}")
        return input_str
    
    def fetch_anime_data(self, query, limit=5):
        """
        Realiza consultas a la API para obtener datos en formato JSON
        Args:
            query: Término de búsqueda
            limit: Número máximo de resultados
        Returns:
            Datos en crudo en formato JSON
        """
        # Validación de entradas
        self.validate_input(query, r'^[\w\s\-\'\.]+$')
        self.validate_input(str(limit), r'^\d+$')
        
        params = {'q': query, 'limit': limit}
        response = requests.get(f"{self.base_url}/anime", params=params)
        
        if response.status_code != 200:
            raise Exception(f"Error en la API: {response.status_code}")
        
        return response.json()
    
    def clean_anime_data(self, raw_data):
        """
        Limpieza y transformación de datos
        Args:
            raw_data: Datos en crudo de la API
        Returns:
            Lista de diccionarios con datos limpios
        """
        cleaned_data = []
        
        for anime in raw_data['data']:
            # Extraer información básica
            cleaned = {
                'mal_id': anime['mal_id'],
                'title': anime['title'],
                'title_english': anime.get('title_english', ''),
                'title_japanese': anime.get('title_japanese', ''),
                'type': anime['type'],
                'episodes': anime.get('episodes', 'N/A'),
                'status': anime.get('status', 'Unknown'),
                'score': anime.get('score', 'N/A'),
                'popularity': anime.get('popularity', 'N/A'),
                'members': anime.get('members', 'N/A')
            }
            
            # Limpiar y procesar géneros
            genres = [g['name'] for g in anime.get('genres', [])]
            cleaned['genres'] = ', '.join(genres) if genres else 'N/A'
            
            # Obtener detalles completos para sinopsis
            try:
                details = self.get_anime_details(anime['mal_id'])
                synopsis = self.clean_text(details.get('synopsis', '') or 
                            details.get('synopsis_es', '') or 
                            'Sin sinopsis disponible')
                cleaned['synopsis'] = synopsis
            except:
                cleaned['synopsis'] = 'Sin sinopsis disponible'
            
            # Fecha de emisión formateada
            if anime.get('aired', {}).get('from'):
                cleaned['start_date'] = anime['aired']['from'][:10]
            else:
                cleaned['start_date'] = 'N/A'
            
            cleaned_data.append(cleaned)
        
        return cleaned_data
    
    def get_anime_details(self, anime_id):
        """Obtiene detalles completos de un anime"""
        response = requests.get(f"{self.base_url}/anime/{anime_id}/full")
        if response.status_code == 200:
            return response.json()['data']
        raise Exception(f"Error al obtener detalles: {response.status_code}")
    
    def clean_text(self, text):
        """Limpia texto eliminando caracteres especiales y formateando"""
        if not text:
            return ''
        
        # Eliminar tags como [Escrito por MAL Rewrite]
        text = re.sub(r'\[.*?\]', '', text)
        # Eliminar caracteres especiales
        text = re.sub(r'[^\w\sáéíóúÁÉÍÓÚñÑ.,;:!?¿¡\'"-]', '', text)
        # Reemplazar múltiples espacios
        text = re.sub(r'\s+', ' ', text).strip()
        # Formatear saltos de línea
        text = text.replace('\\n', '\n')
        
        return text
    
    def create_structured_data(self, cleaned_data):
        """
        Crea una estructura de datos optimizada para análisis
        Args:
            cleaned_data: Datos limpios
        Returns:
            Estructura optimizada para análisis
        """
        structured = []
        
        for anime in cleaned_data:
            # Seleccionar solo los campos relevantes para el análisis
            item = {
                'id': anime['mal_id'],
                'titulo': anime['title'],
                'titulo_espanol': anime.get('title_english', ''),
                'generos': anime['genres'],
                'puntuacion': float(anime['score']) if anime['score'] != 'N/A' else None,
                'popularidad': int(anime['popularity']) if anime['popularity'] != 'N/A' else None,
                'miembros': int(anime['members']) if anime['members'] != 'N/A' else None,
                'fecha_inicio': anime['start_date'],
                'sinopsis': anime['synopsis'][:500]  # Limitar tamaño de sinopsis
            }
            
            # Resolver inconsistencias en tipos de anime
            if item['titulo_espanol'] == '':
                item['titulo_espanol'] = item['titulo']
            
            structured.append(item)
        
        return structured
    
    def save_to_file(self, data, filename_prefix='anime_data'):
        """
        Guarda datos en archivos CSV y JSON
        Args:
            data: Datos a guardar
            filename_prefix: Prefijo para los archivos
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Guardar como JSON
        json_filename = f"{filename_prefix}_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        # Guardar como CSV
        csv_filename = f"{filename_prefix}_{timestamp}.csv"
        if data:  # Solo si hay datos
            with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        
        return json_filename, csv_filename
    
    def document_process(self, query, raw_data, cleaned_data, structured_data, filenames):
        """
        Genera documentación del proceso
        Args:
            query: Término de búsqueda
            raw_data: Datos crudos
            cleaned_data: Datos limpios
            structured_data: Datos estructurados
            filenames: Nombres de archivos guardados
        Returns:
            Documentación en formato de texto
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        doc = f"""Documentación del Proceso de Extracción y Procesamiento de Datos de Anime

1. Información General
- Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- Término de búsqueda: "{query}"
- Resultados obtenidos: {len(structured_data)}

2. Extracción de Datos
[... resto del contenido de la documentación ...]
"""
        # Guardar documentación
        doc_filename = f"documentacion_proceso_{timestamp}.txt"
        with open(doc_filename, 'w', encoding='utf-8') as f:
            f.write(doc)
        
        return doc_filename

def main():
    processor = AnimeDataProcessor()
    
    print("=== Sistema de Extracción y Procesamiento de Datos de Anime ===")
    print("Este sistema realiza búsquedas, limpia y estructura datos de anime para análisis.")
    
    while True:
        try:
            query = input("\nIngrese el nombre del anime a buscar (o 'salir' para terminar): ")
            
            if query.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            if not query.strip():
                print("Por favor ingrese un nombre válido")
                continue
                
            # 1. Extracción de datos
            print("\n[1/4] Extrayendo datos de la API...")
            raw_data = processor.fetch_anime_data(query)
            
            if not raw_data['data']:
                print(f"No se encontraron resultados para '{query}'")
                continue
                
            # 2. Limpieza de datos
            print("[2/4] Limpiando y transformando datos...")
            cleaned_data = processor.clean_anime_data(raw_data)
            
            # 3. Estructuración de datos
            print("[3/4] Creando estructura optimizada para análisis...")
            structured_data = processor.create_structured_data(cleaned_data)
            
            # 4. Almacenamiento y documentación
            print("[4/4] Guardando resultados y generando documentación...")
            json_file, csv_file = processor.save_to_file(structured_data)
            doc_file = processor.document_process(
                query, raw_data, cleaned_data, structured_data, (json_file, csv_file)
            )
            
            print("\nProceso completado exitosamente!")
            print(f"- Datos JSON guardados en: {json_file}")
            print(f"- Datos CSV guardados en: {csv_file}")
            print(f"- Documentación del proceso en: {doc_file}")
            
            # Mostrar resumen de resultados
            print(f"\nResumen de datos para '{query}':")
            for i, anime in enumerate(structured_data[:3], 1):  # Mostrar primeros 3
                print(f"\n{i}. {anime['titulo']} ({anime['titulo_espanol']})")
                print(f"   Géneros: {anime['generos']}")
                print(f"   Puntuación: {anime['puntuacion'] or 'N/A'}")
                print(f"   Sinopsis: {anime['sinopsis'][:100]}...")
                
        except Exception as e:
            print(f"\nError: {str(e)}\nPor favor intente nuevamente.")

if __name__ == "__main__":
    main()