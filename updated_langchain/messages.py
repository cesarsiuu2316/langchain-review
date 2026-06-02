import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def create_llm_chat_model(model):
    chat_model = init_chat_model(model)
    return chat_model

def main():
    model = create_llm_chat_model(model="groq:llama-3.3-70b-versatile")

    model.invoke("What is langchain?")  # Text pront, no conversation historry, minimal code

    SeniorDeveloperSystemMessage = SystemMessage(
        """
        You are a helpful assistant that can answer complex coding questions. 
        You know a lot about ML, AI, and software development.
        Provide detailed explanations and code examples when relevant.    
        """
    )

    messages = [
        SeniorDeveloperSystemMessage,
        HumanMessage(content="What is langchain?")
    ]
    response = model.invoke(messages)  # Conversation history, more structured, more code
    print("Response:", response.content)


if __name__ == "__main__":
    main()