# AI Voice Reporting System Infrastructure

This directory contains the infrastructure-related files for the AI Voice Reporting System project. It includes configurations for deploying the backend services on Google Cloud using Cloud Run and Cloud Functions, as well as infrastructure management using Terraform.

## Directory Structure

- **cloudrun/**: Contains the Dockerfile for building the Cloud Run service.
- **cloudfunctions/**: Contains the main entry point for the Cloud Function that handles report ingestion and summarization.
- **terraform/**: Contains Terraform configurations for deploying the necessary infrastructure on Google Cloud.

## Setup Instructions

1. **Cloud Run**: 
   - Build the Docker image using the Dockerfile in the `cloudrun` directory.
   - Deploy the image to Google Cloud Run.

2. **Cloud Functions**: 
   - Deploy the function defined in `cloudfunctions/main.py` to handle report uploads and summarization.

3. **Terraform**: 
   - Use the configurations in `terraform/main.tf` to set up the required cloud resources.

## Additional Notes

- Ensure that you have the necessary permissions and API access enabled in your Google Cloud project.
- Refer to the individual README files in the `backend` and `frontend` directories for more details on their respective setups and usage.