import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Load environment variables from .env file
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"

    # PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    # JINA_API_KEY = os.getenv("JINA_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION = "enterprise_rag"
    QDRANT_CLUSTER_ENDPOINT = os.getenv("QDRANT_CLUSTER_ENDPOINT")


settings = Settings()