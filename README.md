# Financial Assistant Agent - Banco Dinheiros S.A

Este projeto implementa um assistente financeiro inteligente para o Banco Dinheiros S.A usando o Google Agent Development Kit (ADK). O assistente ajuda clientes a consultar informações sobre seus portfólios de investimento, dados de mercado e produtos bancários através de uma interface conversacional.

## Visão Geral da Arquitetura

O sistema é baseado em um `root_agent` que utiliza o modelo Gemini 2.5 Flash e coordena as seguintes ferramentas especializadas:

* **get_portfolio_data**: Busca dados do portfólio de investimento de um cliente específico
* **calculate_portfolio_performance**: Calcula a rentabilidade total de um portfólio
* **get_market_info**: Obtém informações de mercado sobre ativos específicos (preços e notícias)
* **consult_knowledge_base**: Consulta a base de conhecimento sobre produtos de investimento do banco

## Funcionalidades Principais

- 📊 **Consulta de Portfólio**: Visualize composição e valores dos investimentos
- 📈 **Análise de Performance**: Calcule a rentabilidade total do portfólio
- 💹 **Dados de Mercado**: Obtenha preços e notícias atualizadas de ativos
- 📚 **Informações de Produtos**: Consulte detalhes sobre CDB, LCI, LCA e fundos de investimento
- 🔒 **Segurança**: O assistente não fornece conselhos de investimento diretos, apenas informações

-----

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

* **Python 3.11** ou superior
* **uv**: Gerenciador de pacotes Python - [Instalar](https://docs.astral.sh/uv/getting-started/installation/)
* **Google Cloud SDK**: Para serviços GCP - [Instalar](https://cloud.google.com/sdk/docs/install)
* **Terraform**: Para deployment de infraestrutura - [Instalar](https://developer.hashicorp.com/terraform/downloads)
* **Make**: Ferramenta de automação de build

-----

## Configuração do Ambiente

### 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd data-analyzer-agent
```

### 2. Instalar as Dependências

```bash
make install
```

### 3. Configurar as Variáveis de Ambiente

Configure suas credenciais do Google Cloud:

```bash
gcloud auth application-default login
gcloud config set project <seu-projeto-gcp>
```

Crie um arquivo `.env` na raiz do projeto (se necessário):

```ini
# Google Cloud
GOOGLE_CLOUD_PROJECT="seu-projeto-gcp"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_USE_VERTEXAI="True"

# Models Configuration
ROOT_MODEL="gemini-2.5-flash"
```

-----

## Executando o Assistente

### Execução Local (Playground)

Para iniciar o ambiente de desenvolvimento local com interface Streamlit:

```bash
make playground
```

Isso abrirá uma interface web onde você pode interagir com o assistente financeiro.

### Deploy para Produção

Para fazer deploy do agente no Vertex AI Agent Engine:

```bash
make backend
```

-----

## Exemplos de Prompts para Teste

Ao executar o playground, você pode testar as capacidades do assistente com os seguintes exemplos:

### Consultar Portfólio de Investimentos

> "Gostaria de ver meu portfólio de investimentos. Meu ID de cliente é cliente_01"

**Resposta esperada**: O assistente retornará detalhes sobre os ativos, valores e perfil de investidor.

### Calcular Performance do Portfólio

> "Qual é a rentabilidade total do meu portfólio? Meu ID é cliente_01"

**Resposta esperada**: Cálculo da rentabilidade ponderada de todos os ativos.

### Consultar Dados de Mercado

> "Quais são as últimas informações sobre a ação XPTO3?"

**Resposta esperada**: Preço atual e últimas notícias sobre o ativo.

### Informações sobre Produtos Bancários

> "O que é um CDB e como funciona?"

**Resposta esperada**: Explicação detalhada sobre o Certificado de Depósito Bancário, incluindo proteção do FGC.

### Consulta sobre LCI e LCA

> "Quais são as vantagens de investir em LCI ou LCA?"

**Resposta esperada**: Informações sobre isenção de IR e características desses investimentos.

### Fluxo Completo de Atendimento

> "Olá, sou cliente do banco e gostaria de entender melhor meus investimentos. Meu ID é cliente_02. Pode me mostrar meu portfólio e calcular a rentabilidade? Também gostaria de saber mais sobre o Fundo de Renda Fixa do banco."

**Resposta esperada**: O assistente fornecerá uma análise completa do portfólio, calculará a performance e explicará sobre o produto mencionado.

-----

## Estrutura do Projeto

```
data-analyzer-agent/
├── app/                      # Código principal da aplicação
│   ├── agent.py             # Configuração do agente principal
│   ├── agent_engine_app.py # Lógica para Vertex AI Agent Engine
│   ├── instructions.py      # Instruções do assistente
│   ├── tools/              # Ferramentas do agente
│   │   ├── portfolio_tool.py    # Gestão de portfólios
│   │   └── market_data_tool.py  # Dados de mercado
│   ├── rag_system/         # Sistema RAG
│   │   └── processor.py    # Processamento de conhecimento
│   └── utils/              # Utilitários
│       ├── gcs.py          # Integração com Google Cloud Storage
│       ├── tracing.py      # Observabilidade e traces
│       └── typing.py       # Definições de tipos
├── deployment/             # Scripts de deployment
├── notebooks/              # Notebooks para prototipação
├── tests/                  # Testes unitários e integração
├── Makefile               # Comandos de automação
└── pyproject.toml         # Configuração do projeto

```

-----

## Comandos Disponíveis

| Comando              | Descrição                                                                    |
| -------------------- | ---------------------------------------------------------------------------- |
| `make install`       | Instala todas as dependências necessárias                                   |
| `make playground`    | Inicia interface Streamlit para testes locais                              |
| `make backend`       | Deploy do agente para o Agent Engine                                        |
| `make test`          | Executa testes unitários e de integração                                    |
| `make lint`          | Verifica qualidade do código (codespell, ruff, mypy)                       |
| `make setup-dev-env` | Configura recursos do ambiente de desenvolvimento com Terraform             |

-----

## Monitoramento e Observabilidade

O aplicativo utiliza OpenTelemetry para observabilidade abrangente, com todos os eventos sendo enviados para:
- **Google Cloud Trace**: Para rastreamento de requisições
- **Google Cloud Logging**: Para monitoramento em tempo real
- **BigQuery**: Para armazenamento de longo prazo e análise

Você pode usar o [dashboard do Looker Studio](https://lookerstudio.google.com/reporting/46b35167-b38b-4e44-bd37-701ef4307418/page/tEnnC) para visualizar os eventos registrados.

-----

## Regras de Negócio Importantes

O assistente segue regras rígidas para garantir conformidade e segurança:

1. **Sem Conselhos de Investimento**: O assistente NUNCA fornece recomendações diretas de compra ou venda
2. **Validação de Identidade**: Sempre solicita ID do cliente antes de fornecer informações do portfólio
3. **Informações Educativas**: Foca em fornecer informações sobre produtos e mercado
4. **Encaminhamento Humano**: Sugere consultor humano quando não pode ajudar

-----

**Desenvolvido com Google Agent Development Kit (ADK)**
