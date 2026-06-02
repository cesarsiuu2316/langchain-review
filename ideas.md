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
- Pydantic: Library for runtime validation (user inputs, api requests, llm outputs, configs)
- TypeDict: type check dicts, passing kwargs, annotation JSON that doesnt need validation, langchain state schemas, no distinct types
- DataClasses: Gives you methods, clean attribute access, no need of validation for trusted personal objects when coding


## Middleware

Provides a way to control what happens inside an agent
- Tracking agents with logging, analytics, debugging
- transforming prompts and outputs formatting
- adding retries, fallbacks, early termination logic
- applying rate limits, guardrails, PII detection

Examples: Summarization of context is a Middleware in agents, Human In the Feedback, Model Call Limit, etc

Summarization Middleware is useful for: 
- Long running conversations that exceed token limits or context windows
- Multi-turn dialogues with extensive history
- Applications where preserverving full conversation context matters.

Human In The Loop: pauses execution for human approval
- High stakes operations, database writes, financial transactions, etc
- Compliance workflows where oversight is mandatory
- Long conversations where feedback guides an agent.
This provides a way to approve Commands, uses Command class to provide answers to the llm when asked.