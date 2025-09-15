import requests
import time
from typing import List, Dict, Any
import os

from dotenv import load_dotenv
import pytz

load_dotenv()

QLIK_HOST = os.getenv("HOST")
QLIK_API_KEY = os.getenv("API_KEY")

class QlikFilterDeleter:
    def __init__(self, tenant_url: str, access_token: str):
        self.base_url = f"https://{tenant_url}/api/v1/apps"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    
    def delete_single_filter(self, app_id: str, filter_id: str) -> Dict[str, Any]:
        """Deleta um único filtro"""
        try:
            url = f"{self.base_url}/{app_id}/report-filters/{filter_id}"
            response = requests.delete(url, headers=self.headers, timeout=30)
            
            return {
                'success': response.status_code == 204,
                'status_code': response.status_code,
                'response_text': response.text,
                'filter_id': filter_id
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'filter_id': filter_id
            }
    
    def delete_multiple_filters(self, app_id: str, filter_ids: List[str], 
                               delay: float = 0.1) -> Dict[str, Any]:
        """Deleta múltiplos filtros com delay entre requisições"""
        results = {
            'successful': [],
            'failed': [],
            'total': len(filter_ids)
        }
        
        for i, filter_id in enumerate(filter_ids):
            print(f"Processando filtro {i+1}/{len(filter_ids)}: {filter_id}")
            
            result = self.delete_single_filter(app_id, filter_id)
            
            if result['success']:
                results['successful'].append(filter_id)
                print(f"✅ Deletado: {filter_id}")
            else:
                results['failed'].append({
                    'id': filter_id,
                    'error': result.get('error', result.get('response_text', 'Erro desconhecido'))
                })
                print(f"❌ Falha: {filter_id} - {result.get('error', 'Erro desconhecido')}")
            
            # Pequeno delay para não sobrecarregar a API
            if i < len(filter_ids) - 1:
                time.sleep(delay)
        
        return results

# Exemplo de uso
if __name__ == "__main__":
    # Configuração
    TENANT_URL = QLIK_HOST  # Sem o https://
    ACCESS_TOKEN = QLIK_API_KEY
    APP_ID = "app_id_exemplo_123456"  # Substitua pelo ID real do app
    
    # Lista de filtros para deletar
    filters_to_delete = [
        "id_filtro_exemplo_1",
        "Id_filtro_exemplo_2",
        "Id_filtro_exemplo_3",
        "Id_filtro_exemplo_4",
    ]
    
    # Inicializar e executar
    deleter = QlikFilterDeleter(TENANT_URL, ACCESS_TOKEN)
    results = deleter.delete_multiple_filters(APP_ID, filters_to_delete)
    
    # Exibir resultados
    print(f"\n🎯 Resultado final:")
    print(f"Total processado: {results['total']}")
    print(f"Sucessos: {len(results['successful'])}")
    print(f"Falhas: {len(results['failed'])}")
    
    if results['failed']:
        print("\n📋 Detalhes das falhas:")
        for failure in results['failed']:
            print(f"ID: {failure['id']} - Erro: {failure['error']}")