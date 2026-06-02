import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain.agents import create_agent


load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def create_llm_chat_model(model):
    chat_model = init_chat_model(model)
    return chat_model


def make_agent(model, response_format):
    agent = create_agent(
        model=model,
        system_prompt="You are a helpful assistant that can answer questions about movies. Provide detailed information about movies when asked.",
        response_format=response_format
    )
    return agent



class Actor(BaseModel):
    """A structured output class representing an actor."""
    name: str = Field(..., description="The name of the actor")
    role: str = Field(..., description="The role of the actor")
    awards: list[str] = Field(default="None", description="A list of awards the actor has won")


class Movie(BaseModel):
    # default value can be added or ... to indicate it is required
    """A structured output class representing a movie."""
    title: str = Field(..., description="The title of the movie")
    year: int = Field(default=0000 ,description="The year the movie was released")
    director: str = Field(..., description="The director of the movie")
    rating: float = Field(..., description="The rating of the movie out of 10")
    cast: list[Actor] = Field(..., description="The main cast of the movie", min_length=5)
    budget: float | None = Field(default=None, description="The budget of the movie in millions of dollars")


def main():
    model = create_llm_chat_model(model="groq:llama-3.3-70b-versatile")

    # Create a version of the model that returns structured output in the form of a Movie object.
    model_with_structure = model.with_structured_output(Movie, include_raw=False)

    agent_with_structure = make_agent(model="groq:llama-3.3-70b-versatile", response_format=Movie)

    #result = model_with_structure.invoke("Provide a lot of info about shrek2 moviee")  # This will return a Movie object with the relevant information filled in.
    #print("Structured output:\n", result)

    result_agent = agent_with_structure.invoke({"messages": [{"role": "user", "content": "Provide a lot of info about shrek2 moviee"}]})
    print("Structured output from agent:\n", result_agent["structured_response"])
    

if __name__ == "__main__":
    main()