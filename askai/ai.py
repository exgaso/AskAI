import openai
import json

class gpt:
    
    def __init__(self, instructions, api_key) -> None:
        self.gpt = openai.OpenAI(api_key=api_key)
        self.tools = []
        self.callbacks = {}
        self.messages=[{"role": "system", "content": instructions}]
        self.model = "gpt-3.5-turbo"

    def add_tool(self, toolname, desc, params, callback):
        if params is None:
            self.tools.append({"type": "function", "function": {"name": toolname, "description": desc}})
        else:
            self.tools.append({"type": "function", "function": {"name": toolname, "description": desc, "parameters": params}})
        self.callbacks[toolname] = callback

    def add_message(self, role, msg):
        self.messages.append({"role": role, "content" : msg})

    def reset_message(self):
        self.messages = self.messages[:1]
        print("Reset GPT message history")

    def ask(self, text: str):
        self.add_message("user", text)
        params = {'model': self.model, 'messages': self.messages}
        if self.tools:
            params["tools"] = self.tools
        response = self.gpt.chat.completions.create(**params)
        # print("GPT tokens used: " + str(response.usage.total_tokens))
        # print("Finish reason: " + response.choices[0].finish_reason)
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        if response_message.content is not None:
            self.add_message(response_message.role, response_message.content)
            # print("Answer: " + response.choices[0].message.content)
        if tool_calls:
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                print("Call function: " + function_name)
                print("Call parameters: " + json.dumps(function_args, indent=2))
                self.callbacks.get(function_name)(function_args)
        return(response.choices[0].message.content)
