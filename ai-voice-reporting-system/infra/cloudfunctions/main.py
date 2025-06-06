from google.cloud import storage
from google.cloud import bigquery
from google.cloud import documentai_v1 as documentai
from google.cloud import firestore
import json
import os

def upload_to_cloud_storage(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the specified Google Cloud Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def summarize_document(project_id, input_uri):
    """Uses Document AI to extract text and summarize the document."""
    client = documentai.DocumentUnderstandingServiceClient()
    gcs_source = documentai.types.GcsSource(uri=input_uri)
    input_config = documentai.types.InputConfig(
        gcs_source=gcs_source,
        mime_type='application/pdf'  # Adjust based on the file type
    )

    request = documentai.types.ProcessRequest(
        name=f'projects/{project_id}/locations/us/processors/YOUR_PROCESSOR_ID',
        raw_document=documentai.types.RawDocument(content=input_config)
    )

    result = client.process_document(request=request)
    return result.document.text

def store_summary_in_bigquery(dataset_id, table_id, summary):
    """Stores the summary in BigQuery."""
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)

    rows_to_insert = [
        {u'summary': summary}
    ]

    errors = client.insert_rows_json(table_ref, rows_to_insert)
    if errors == []:
        print("New summary has been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def main(event, context):
    """Triggered by a change to a Cloud Storage bucket."""
    bucket_name = event['bucket']
    file_name = event['name']
    input_uri = f'gs://{bucket_name}/{file_name}'

    # Upload to Cloud Storage
    upload_to_cloud_storage(bucket_name, file_name, file_name)

    # Summarize the document
    summary = summarize_document(os.getenv('PROJECT_ID'), input_uri)

    # Store summary in BigQuery
    store_summary_in_bigquery(os.getenv('DATASET_ID'), os.getenv('TABLE_ID'), summary)