

from dotenv import load_dotenv
load_dotenv()
import os
print(1)


API_KEY = os.getenv("openai_api_key")
print(API_KEY)
if not API_KEY:
    raise ValueError("Missing openai_api_key in environment variables or .env file")

os.environ["OPENAI_API_KEY"] = API_KEY

client = OpenAI()


