from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent
from langchain.memory import ConversationBufferMemory
import os

# memory = ConversationBufferMemory(memory_key="chat_history")

agent = create_csv_agent(
  ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"]),
  "permits-2020-onwards.csv",
  verbose=True,
  agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#   memory=memory
)

def ask_agent(question):
#   memory.chat_memory.add_user_message(question)
  response = agent.run("Follow your response with a Markdown table showing the data you used." + question)
#   memory.chat_memory.add_ai_message(response)
  return response