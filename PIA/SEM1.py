import requests
import re

class AnimeSearcher:
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4"
    
    def validate_input(self, input_str, pattern):
        """Valida entrada con expresiones regulares"""
        if not re.match(pattern, input_str):
            raise ValueError("Formato de entrada inválido")
        return input_str
    
    def search_anime(self, query, limit=5):
        """
        Busca cualquier anime por nombre
        Args:
            query: Nombre del anime a buscar
            limit: Número máximo de resultados (default 5)
        Returns:
            Lista de animes que coinciden con la búsqueda
        """
        # Validar inputs
        self.validate_input(query, r'^[\w\s\-]+$')
        self.validate_input(str(limit), r'^\d+$')
        
        params = {
            'q': query,
            'limit': limit
        }
        
        url = f"{self.base_url}/anime"
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json()['data']
        else:
            raise Exception(f"Error al conectar con la API: {response.status_code}")
    
    def get_anime_details(self, anime_id):
        """Obtiene detalles completos incluyendo sinopsis en español"""
        self.validate_input(str(anime_id), r'^\d+$')
        
        url = f"{self.base_url}/anime/{anime_id}/full"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()['data']
        else:
            raise Exception(f"Error al conectar con la API: {response.status_code}")

def display_anime_results(anime_list, query):
    """Muestra los resultados con sinopsis en español cuando está disponible"""
    print(f"\n=== Resultados para '{query}' ===")
    for idx, anime in enumerate(anime_list, 1):
        print(f"\n{idx}. {anime['title']} ({anime.get('title_japanese', '')})")
        print(f"   Tipo: {anime['type']} | Episodios: {anime.get('episodes', 'N/A')}")
        print(f"   Score: {anime.get('score', 'N/A')}")
        print(f"   Géneros: {', '.join(g['name'] for g in anime.get('genres', []))}")
        
        # Obtener detalles completos para la sinopsis en español
        try:
            details = AnimeSearcher().get_anime_details(anime['mal_id'])
            synopsis = details.get('synopsis', '') or details.get('synopsis_es', '') or 'Sin sinopsis disponible'
            
            # Limpiar sinopsis de caracteres especiales
            synopsis = re.sub(r'\[.*?\]', '', synopsis)  # Remover tags como [Escrito por MAL Rewrite]
            synopsis = synopsis.replace('\\n', '\n   ')  # Formatear saltos de línea
            
            print(f"   Sinopsis (español): {synopsis[:300]}..." if len(synopsis) > 300 else f"   Sinopsis (español): {synopsis}")
        except Exception as e:
            print(f"   Sinopsis: No disponible (error al obtener detalles)")

if __name__ == "__main__":
    searcher = AnimeSearcher()
    
    print("=== Buscador de Anime con Sinopsis en Español ===")
    print("(Puedes buscar cualquier anime por su nombre)")
    print("Ejemplos: 'Naruto', 'Attack on Titan', 'One Piece', 'Demon Slayer'")
    
    while True:
        try:
            query = input("\nIngrese el nombre del anime a buscar (o 'salir' para terminar): ")
            
            if query.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            if not query.strip():
                print("Por favor ingrese un nombre válido")
                continue
                
            results = searcher.search_anime(query)
            
            if not results:
                print(f"No se encontraron resultados para '{query}'")
            else:
                display_anime_results(results, query)
                
        except Exception as e:
            print(f"\nError: {e}\nPor favor intente nuevamente.")