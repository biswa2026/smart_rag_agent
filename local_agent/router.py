from openai import OpenAI
from local_agent.qa_agent import qa_agent
from config.settings import EMAIL_REGEX
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
API_KEY = os.getenv("openai_api_key")
if not API_KEY:
    raise ValueError("Missing openai_api_key in environment variables or .env file")
os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize OpenAI client (if needed)
client = OpenAI()

# -------------------------------------------------------------------
# 🧠 SUPERVISOR
# -------------------------------------------------------------------

def supervisor() -> "Agent":
    """
    Returns a ready-to-use QA Agent.
    The user prompt is passed separately to Runner.run_sync.
    """
    return qa_agent()  # returns Agent object, not called here

# -------------------------------------------------------------------
# 📧 EMAIL DETECTION
# -------------------------------------------------------------------

def contains_email(text: str) -> bool:
    """
    Returns True if text contains an email, False otherwise.
    """
    return bool(EMAIL_REGEX.search(text))
