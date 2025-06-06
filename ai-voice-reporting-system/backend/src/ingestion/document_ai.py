from google.cloud import documentai_v1 as documentai
from google.oauth2 import service_account

def initialize_document_ai_client(credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = documentai.DocumentUnderstandingServiceClient(credentials=credentials)
    return client

def process_document(project_id, input_uri, credentials_path):
    client = initialize_document_ai_client(credentials_path)

    gcs_input_uri = f"gs://{input_uri}"
    document = documentai.types.Document(
        input_gcs_source=gcs_input_uri,
        mime_type="application/pdf"  # Change mime_type based on the document type
    )

    request = documentai.types.ProcessRequest(
        name=f"projects/{project_id}/locations/us-central1/documents:process",
        raw_document=document
    )

    result = client.process_document(request=request)
    return result.document.text  # Return the extracted text from the document