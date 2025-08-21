

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env kalau di local
load_dotenv()

def ask_llm(prompt: str) -> str:
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("Google API Key not found. Pastikan diset di .env atau environment variables.")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=google_api_key
    )
    return llm.invoke(prompt)


