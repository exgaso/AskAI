import sys
import os
import platform
from rich.markdown import Markdown
from rich.console import Console
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

def main():
    my_MODEL = "gpt-3.5-turbo"
    my_APIKEY = getAPIKEY()
    my_OS = platform.system()
    my_INSTRUCTION = f"you are an IT-assistant answering my questions only in short sentence. Mostly i ask something about {my_OS} computers."   
    args = sys.argv[1:]
    if len(args) >= 1:
        for arg in args[:]:
            if arg[0] == "-":
                if arg == "-4": # use version 4
                    my_MODEL = "gpt-4o"
                if arg == "-b": # dont use short response
                    my_INSTRUCTION = f"you are an IT-assistant. Mostly i ask something about {my_OS} computers."  
                if arg == "-h" or arg == "--help":
                    print("askai [-4] [-b] your question")
                    quit()
                args.remove(arg)
            else:
                break
    if len(args) == 0:
        question = input("Your question: ")
    else:
        question = (' '.join(args))
    llm = gpt(my_MODEL, my_INSTRUCTION, my_APIKEY)
    # llm.add_tool("function_example", "a function example for demonstation", {"type": "object","properties": { "number": { "type": "number","description": "just a random number",}},"required": ["number"],}, feedback_function_example)
    rsp = llm.ask(question)
    concole = Console()
    rspmd = Markdown(rsp)
    concole.print(rspmd)   


if __name__ == '__main__':
    main()