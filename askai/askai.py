import sys
import os
import platform
from askai.ai import gpt

def getAPIKEY():
    keyfile = __file__ + '.key'
    if os.path.exists(keyfile):
        with open(keyfile, 'r') as file: 
            return file.read().strip()
    else:
        key = input("Write your API_KEY for OpenAI (will be saved on disk): ")
        with open(keyfile, 'w') as file:
            file.write(key)
            print(f"Your key is saved to the file {keyfile}")
        return key
    
# def feedback_function_example(number):
#     print(f"The example function got executed with nubmer {number}")

def askai(question):
    my_APIKEY = getAPIKEY()
    my_OS = platform.system()
    llm = gpt(f"you are a little IT-assistant answering my questions only in a few words. Mostly i ask something about computers. I use {my_OS}", my_APIKEY)
    # llm.add_tool("function_example", "a function example for demonstation", {"type": "object","properties": { "number": { "type": "number","description": "just a random number",}},"required": ["number"],}, feedback_function_example)
    rsp = llm.ask(question)
    print(rsp)    

def main():
    askai(' '.join(sys.argv[1:]))

if __name__ == '__main__':
    main()