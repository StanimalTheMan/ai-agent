import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
sys_args = sys.argv
if len(sys_args) == 1:
    # prompt is not provided, so print err message and exit program with exit code 1
    print("ERROR: prompt is not provided")
    exit(1)
    
text_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys_args[1])

print(text_response)
print(f"Prompt tokens: {text_response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {text_response.usage_metadata.candidates_token_count}")