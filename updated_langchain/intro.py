# Review langchain core concepts
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

@tool
def get_time():
    """Get the current time in ISO format."""
    from datetime import datetime
    return f"The time right now is {datetime.now().isoformat()}."

def make_agent(model):
    agent = create_agent(
        model=model,
        tools=[get_time],
        system_prompt="You are a helpful assistant that can answer questions about the world.",
    )
    return agent

def create_llm_chat_model(model):
    chat_model = init_chat_model(model)
    return chat_model

def create_groq_chat_model(model):
    chat_model = ChatGroq(model=model)
    return chat_model

def main():
    agent = make_agent("groq:llama-3.3-70b-versatile")
    chat_model = create_llm_chat_model("groq:llama-3.3-70b-versatile")
    groq_chat_model = create_groq_chat_model("llama-3.3-70b-versatile")

    continue_chat = True
    while continue_chat:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            continue_chat = False
        else:
            response1 = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
            print(f"AI user response: {response1['messages'][-1]}\n")
            response2 = chat_model.invoke(user_input)
            print(f"LLM chat model response: {response2.content}\n")
            response3 = groq_chat_model.invoke(user_input)
            print(f"Groq chat model response: {response3.content}\n")

if __name__ == "__main__":
    main()