from google.cloud import bigquery

class BigQueryClient:
    def __init__(self, project_id):
        self.client = bigquery.Client(project=project_id)

    def insert_summary(self, dataset_id, table_id, summary_data):
        table_ref = self.client.dataset(dataset_id).table(table_id)
        errors = self.client.insert_rows_json(table_ref, summary_data)
        if errors:
            raise Exception(f"Failed to insert rows: {errors}")

    def query_summaries(self, query):
        query_job = self.client.query(query)
        return query_job.result()  # Returns an iterator of rows

    def get_summary_by_id(self, dataset_id, table_id, summary_id):
        query = f"""
        SELECT * FROM `{dataset_id}.{table_id}`
        WHERE id = @summary_id
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("summary_id", "STRING", summary_id)
            ]
        )
        query_job = self.client.query(query, job_config=job_config)
        return query_job.result()  # Returns an iterator of rows