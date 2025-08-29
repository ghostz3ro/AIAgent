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
input_prompt = str(sys.argv[1]) #sys.argv[0] is the first argument which is the program called, sys.argv[1] is the first argument converted to a string. 
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=input_prompt)

print(response.text) # print the .text part of the bot's response 

# print the token counts for the prompt and the response
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") 
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



# def main():
#     print("Hello from aiagent!")




# if __name__ == "__main__":
#     main()


