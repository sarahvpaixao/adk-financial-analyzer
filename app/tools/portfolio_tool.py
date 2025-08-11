import json

# Simula uma base de dados de clientes
MOCK_CLIENT_DATA = {
    "cliente_01": {
        "nome": "João Silva",
        "ativos": [
            {"nome": "Fundo de Renda Fixa Dinheiros S.A", "valor": 50000, "rentabilidade_anual": 0.12},
            {"nome": "Ações XPTO3", "valor": 25000, "rentabilidade_anual": 0.25},
            {"nome": "CDB Dinheiros S.A", "valor": 75000, "rentabilidade_anual": 0.10}
        ],
        "perfil": "moderado"
    },
    "cliente_02": {
        "nome": "Maria Santos",
        "ativos": [
            {"nome": "Fundo de Ações de Crescimento", "valor": 10000, "rentabilidade_anual": 0.35},
            {"nome": "Tesouro Direto", "valor": 90000, "rentabilidade_anual": 0.11}
        ],
        "perfil": "conservador"
    }
}

def get_portfolio_data(client_id: str) -> str:
    """
    Simula a busca por dados de um portfólio de investimento de um cliente.
    
    Args:
        client_id: O ID do cliente.
        
    Returns:
        Uma string JSON com os dados do portfólio ou um erro se o cliente não for encontrado.
    """
    print(f"Chamando ferramenta: get_portfolio_data para o cliente {client_id}")
    
    if client_id in MOCK_CLIENT_DATA:
        data = MOCK_CLIENT_DATA[client_id]
        return json.dumps(data, ensure_ascii=False)
    else:
        return json.dumps({"erro": "Cliente não encontrado."})

def calculate_portfolio_performance(client_id: str) -> str:
    """
    Calcula o desempenho total de um portfólio.
    
    Args:
        client_id: O ID do cliente.
        
    Returns:
        Uma string JSON com a rentabilidade total ou um erro.
    """
    print(f"Chamando ferramenta: calculate_portfolio_performance para o cliente {client_id}")

    if client_id in MOCK_CLIENT_DATA:
        data = MOCK_CLIENT_DATA[client_id]
        valor_total = sum(asset['valor'] for asset in data['ativos'])
        if valor_total > 0:
            rentabilidade_total = sum(asset['valor'] * asset['rentabilidade_anual'] for asset in data['ativos']) / valor_total
            return json.dumps({"rentabilidade_total": f"{rentabilidade_total:.2%}"})
        else:
            return json.dumps({"rentabilidade_total": "0.00%"})
    else:
        return json.dumps({"erro": "Cliente não encontrado."})
