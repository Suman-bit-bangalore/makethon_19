provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_storage_bucket" "report_bucket" {
  name     = "your-report-bucket-name"
  location = "US"
}

resource "google_bigquery_dataset" "summaries_dataset" {
  dataset_id = "summaries_dataset"
  location   = "US"
}

resource "google_cloud_run_service" "voice_reporting_service" {
  name     = "voice-reporting-service"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/your-gcp-project-id/your-backend-image"
        ports {
          container_port = 8080
        }
      }
    }
  }
}

resource "google_cloud_run_service_iam_member" "invoker" {
  service = google_cloud_run_service.voice_reporting_service.name
  location = google_cloud_run_service.voice_reporting_service.location
  role    = "roles/run.invoker"
  member  = "allUsers"
}

output "report_bucket_name" {
  value = google_storage_bucket.report_bucket.name
}

output "bigquery_dataset_id" {
  value = google_bigquery_dataset.summaries_dataset.dataset_id
}

output "cloud_run_service_url" {
  value = google_cloud_run_service.voice_reporting_service.status[0].url
}