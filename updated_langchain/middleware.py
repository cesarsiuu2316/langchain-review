import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def main():
    agent = create_agent(
        model="groq:llama-3.3-70b-versatile",
        checkpointer=InMemorySaver(), # Saves history in memory RAM, not persistent but good for testing
        middleware = [
            SummarizationMiddleware(
                model="groq:llama-3.1-8b-instant", 
                trigger=("messages", 5), # Trigger summarization when there are 5 messages in the conversation history
                keep=("messages", 2), # Keep the last 2 messages in the conversation history to maintain context
            )
        ]
    )

    # Run with thread_id to maintain conversation history across multiple invokes
    config = {"thread_id": "test_thread"}
    questions = [
        "What is the capital of France?",
        "What is the largest mammal?",
        "What is 1+1?",
        "What is 2x2?",
        "What is the square root of 16?"
        "What is the cube root of 27?"
    ]

    for q in questions:
        response = agent.invoke({"messages": [HumanMessage(content=q)]}, config=config)
        print(f"Messages: {response}\n")
        print(f"Messages length: {len(response['messages'])}\n")

if __name__ == "__main__":
    main()