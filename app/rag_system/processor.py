def consult_knowledge_base(query: str) -> str:
    """
    Simula a consulta à base de conhecimento do banco sobre produtos de investimento.
    
    Args:
        query: A pergunta do usuário sobre o produto.
        
    Returns:
        Uma string com a informação relevante.
    """
    print(f"Consultando base de conhecimento para a query: '{query}'")
    if "renda fixa" in query.lower() or "cdb" in query.lower():
        return "O CDB é um investimento de renda fixa emitido pelo banco. Ele é protegido pelo FGC até R$ 250.000."
    elif "lci" in query.lower() or "lca" in query.lower():
        return "LCI e LCA são títulos de renda fixa isentos de Imposto de Renda para pessoa física."
    else:
        return "Não encontrei informações detalhadas sobre esse produto na minha base. Por favor, especifique sua pergunta."
