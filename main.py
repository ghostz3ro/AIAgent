import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)
n = len(sys.argv)
#print(n)
if n < 2:
    print("no valid argument provided")
    sys.exit(1)
#print(str(sys.argv[1]))

input_prompt = sys.argv[1]
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=input_prompt)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# def main():
#     print("Hello from aiagent!")




# if __name__ == "__main__":
#     main()


