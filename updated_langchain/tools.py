import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.chat_models import init_chat_model
import json

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location} is sunny."

@tool
def get_time(timezone: str) -> str:
    """Get the current time in a given timezone."""
    return f"The current time in {timezone} is 3:00 PM."

TOOLS = [get_weather, get_time]
TOOL_REGISTRY = {t.name: t for t in TOOLS}

def create_llm_chat_model(model):
    chat_model = init_chat_model(model)
    return chat_model

def testing(user_message): 
    model = create_llm_chat_model(model="groq:llama-3.3-70b-versatile")
    model_with_tools = model.bind_tools(TOOLS)

    messages = [
        {"role": "system", "content": "You have access to real-time tools. When a tool result is provided, use it to answer directly and confidently."},
        {"role": "user", "content": user_message}
    ]

    # TOOL EXECUTION LOOP

    print("\n========== INVOKE 1 — what the LLM receives ==========")
    for m in messages:
        print(m)
    
    # 1. Invoke the model with the initial messages to get the AI response, which may include tool calls 
    #   (if the model decides to use tools).
    ai_response = model_with_tools.invoke(messages)
    messages.append(ai_response)

    print("\n========== INVOKE 1 — what the LLM returned ==========")
    print(ai_response)

    if ai_response.tool_calls:
        # 2. If there are tool calls, execute each tool and append the results to the messages.
        for tool_call in ai_response.tool_calls:
            tool_fn = TOOL_REGISTRY[tool_call["name"]]
            # Appending the tool call to the messages so the model can see the original tool call in the context of the conversation with the tool result.
            messages.append(tool_fn.invoke(tool_call))
            # this receives a tool message

        print("\n========== INVOKE 2 — what the LLM receives ==========")
        for m in messages:
            print(m)

        # 3. Invoke the model again with the updated messages to get the final response.
        final_response = model.invoke(messages)

        print("\n========== INVOKE 2 — what the LLM returned ==========")
        print(final_response)

        print("\n>>> FINAL ANSWER WITH TOOLS:", final_response.content)
    else:
        print("\n>>> FINAL ANSWER:", ai_response.content)
    print("\n=========================================================\n")

def main():
    testing("What's the weather like in New York?")
    testing("What time is it in Tokyo?")
    testing("What's the weather like in Paris and what time is it in London?")

if __name__ == "__main__":
    main()