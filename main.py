import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


# Preparation and initialisation
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)





n = len(sys.argv)

if n < 2:
    print("no valid argument provided") # exit if no prompt is added to the program run call
    sys.exit(1)


# Prompt the LLM from sys.argv and get a response, print the response and token costs in the terminal. 
user_prompt = str(sys.argv[1]) #sys.argv[0] is the first argument which is the program called, sys.argv[1] is the first argument converted to a string. 
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

if "--verbose" in sys.argv: #if --verbose flag exists in the prompt, print a lot of info, otherwise just the response.
    
    print(f"User prompt: {user_prompt}\n")
    print(response.text) # print the .text part of the bot's response 

    # print the token counts for the prompt and the response
    print(f"Prompt tokens: {prompt_tokens}") 
    print(f"Response tokens: {response_tokens}")
else: 
    print(response.text) # print the .text part of the bot's response 


def main():
    print("Hello from aiagent!")




if __name__ == "__main__":
    main()


