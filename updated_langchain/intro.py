# Review langchain core concepts
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

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

def main():
    agent = make_agent("groq:llama-3.3-70b-versatile")
    continue_chat = True
    while continue_chat:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            continue_chat = False
        else:
            response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
            print(f"AI user response: {response['messages'][-1]}")

if __name__ == "__main__":
    main()