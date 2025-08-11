import json

# Simula uma API de dados de mercado
MOCK_MARKET_DATA = {
    "XPTO3": {"preco": 35.50, "ultima_atualizacao": "2025-08-09T18:00:00Z", "noticia": "XPTO3 anuncia novo projeto de expansão."},
    "ABCA4": {"preco": 112.75, "ultima_atualizacao": "2025-08-09T18:00:00Z", "noticia": "ABCA4 reporta lucro recorde no trimestre."}
}

def get_market_info(ticker: str) -> str:
    """
    Simula a busca por informações de mercado de um ativo.
    
    Args:
        ticker: O código do ativo (ex: XPTO3).
        
    Returns:
        Uma string JSON com o preço e notícia do ativo, ou um erro.
    """
    print(f"Chamando ferramenta: get_market_info para o ticker {ticker}")

    ticker_upper = ticker.upper()
    if ticker_upper in MOCK_MARKET_DATA:
        return json.dumps(MOCK_MARKET_DATA[ticker_upper], ensure_ascii=False)
    else:
        return json.dumps({"erro": "Ativo não encontrado."})