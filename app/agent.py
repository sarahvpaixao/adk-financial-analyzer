import os
import google.auth
from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .instructions import FINANCIAL_ASSISTANT_INSTRUCTION
from .tools.portfolio_tool import get_portfolio_data, calculate_portfolio_performance
from .tools.market_data_tool import get_market_info
from .rag_system.processor import consult_knowledge_base


_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=FINANCIAL_ASSISTANT_INSTRUCTION,
    tools=[
        get_portfolio_data,
        calculate_portfolio_performance,
        get_market_info,
        consult_knowledge_base
    ]
)
