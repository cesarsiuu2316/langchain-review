- Agents are good for fast integration, tool calling and memory handling, etc
- To use tools in models created through init_chat_model or model_chat, need to create tool execution loops. 


## LLMs 

Start llm conversations:
- init_chat_model
- model_chat (specific to the model)
- create_agent (with memory and easier tool handling)


Inputs and outputs configs: 
- stream outputs (better than normal way for conversations)
- batches allow parallel processing of inputs


## Tools

Tool Execution Loop:
1. Binding tools to model and appending messages for every following step
2. Invoking model with tools to decide what tools to use
3. Invoking tool call from ai response for every tool
4. Invoking final model response without tools just from appended messages. 


## Messages

Prompts: 
- Text: Single, simple, no history scenarios
- Messages


Message Structures 
- System message: Tells the model how to behave and provide context for interactions
- Human Message: User input and interactions with model
- AIMessage: Model's responses including text content, tool calls and metadata
- Tool Message: Output of tool calls


Message parameters
- Role
- Content: the text
- Metadata: Define users, ids, etc


## Structured Outputs

It allows to define a schema so the llm always answer in a structured predefined way

Techniques
- Pydantic: Runtime validation (user inputs, api requests, llm outputs, configs)
- TypeDict: type check dicts, passing kwargs, annotation JSON that doesnt need validation, langchain state schemas, no distinct types
- DataClasses: Gives you methods, clean attribute access, no need of validation for trusted personal objects when coding


Pydantic: python library that enforces a scheme a data type structure at runtime (useful for data validation)
