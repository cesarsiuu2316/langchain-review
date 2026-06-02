- Agents are good for fast integration, tool calling and memory handling, etc
- To use tools in models created through init_chat_model or model_chat, need to create tool execution loops. 

Tool Execution Loop
1. Binding tools to model and appending messages for every following step
2. Invoking model with tools to decide what tools to use
3. Invoking tool call from ai response for every tool
4. Invoking final model response without tools just from appended messages. 
