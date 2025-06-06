from google.cloud import aiplatform

def summarize_text(text: str) -> str:
    """
    Summarizes the given text using a large language model (LLM).
    
    Args:
        text (str): The text to summarize.
        
    Returns:
        str: The summarized text.
    """
    # Initialize the AI Platform
    aiplatform.init(project='your-gcp-project-id', location='us-central1')

    # Define the model to use for summarization
    model = aiplatform.Model('your-model-id')

    # Call the model to generate a summary
    response = model.predict(instances=[text])

    # Extract the summary from the response
    summary = response.predictions[0]

    return summary

def summarize_document(document_text: str) -> dict:
    """
    Summarizes the content of a document and returns both the original text and the summary.
    
    Args:
        document_text (str): The text content of the document.
        
    Returns:
        dict: A dictionary containing the original text and the summary.
    """
    summary = summarize_text(document_text)
    return {
        'original_text': document_text,
        'summary': summary
    }