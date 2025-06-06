from google.cloud import storage

class CloudStorageClient:
    def __init__(self, bucket_name):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, file_path, destination_blob_name):
        """Uploads a file to the bucket."""
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(file_path)

    def download_file(self, source_blob_name, destination_file_path):
        """Downloads a blob from the bucket."""
        blob = self.bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_path)

    def list_blobs(self, prefix=None):
        """Lists all the blobs in the bucket."""
        blobs = self.bucket.list_blobs(prefix=prefix)
        return [blob.name for blob in blobs]