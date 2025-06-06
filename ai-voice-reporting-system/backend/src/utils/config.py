import os

class Config:
    """Configuration settings for the application."""
    
    # API keys and service URLs
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "path/to/credentials.json")
    DOCUMENT_AI_ENDPOINT = os.getenv("DOCUMENT_AI_ENDPOINT", "https://your-document-ai-endpoint")
    SPEECH_TO_TEXT_ENDPOINT = os.getenv("SPEECH_TO_TEXT_ENDPOINT", "https://speech.googleapis.com/v1/speech:recognize")
    TEXT_TO_SPEECH_ENDPOINT = os.getenv("TEXT_TO_SPEECH_ENDPOINT", "https://texttospeech.googleapis.com/v1/text:synthesize")
    
    # Database settings
    BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET", "your_dataset_name")
    FIRESTORE_PROJECT_ID = os.getenv("FIRESTORE_PROJECT_ID", "your-firestore-project-id")
    
    # Other settings
    MAX_SUMMARY_LENGTH = int(os.getenv("MAX_SUMMARY_LENGTH", 500))
    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en-US")