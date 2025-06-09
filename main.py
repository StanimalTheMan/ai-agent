import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    args = user_args = sys.argv[1:]
    if args[-1] == '--verbose':
        user_args = user_args[:-1]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python man.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(user_args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    text_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    if args[-1] == '--verbose':
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {text_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {text_response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(text_response.text)

if __name__ == "__main__":
    main()