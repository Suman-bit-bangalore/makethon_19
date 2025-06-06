# AI Voice Reporting System - Backend

This document provides an overview of the backend components of the AI Voice Reporting System. It outlines the structure, setup instructions, and usage of the backend services.

## Project Structure

The backend is organized into several modules, each responsible for different functionalities:

- **src/app.py**: Main entry point for the backend application. Initializes the web server and sets up routes for handling requests related to report ingestion and voice interactions.

- **src/ingestion**: Contains modules for processing uploaded reports.
  - **document_ai.py**: Functions for interacting with Google Document AI to extract text from uploaded documents.
  - **ocr_utils.py**: Utility functions for performing OCR on images and PDFs.
  - **summarizer.py**: Functions that utilize LLMs to summarize extracted text from documents.

- **src/voice**: Manages voice interaction functionalities.
  - **stt_stream.py**: Implements streaming functionality for Google Speech-to-Text, handling real-time audio transcription.
  - **tts_stream.py**: Manages the streaming of text-to-speech responses back to the client.
  - **websocket_server.py**: Sets up a WebSocket server for real-time communication between the frontend and backend.

- **src/llm**: Contains logic for interacting with LLM APIs.
  - **agent.py**: Defines the logic for interacting with the LLM API, managing conversation state and context.
  - **rag.py**: Implements retrieval-augmented generation logic for pulling relevant summaries.

- **src/storage**: Handles data storage interactions.
  - **bigquery_client.py**: Functions for interacting with Google BigQuery.
  - **firestore_client.py**: Functions for interacting with Firestore.
  - **cloud_storage.py**: Functions for uploading and retrieving files from Google Cloud Storage.

- **src/utils**: Contains utility functions and configuration management.
  - **config.py**: Manages configuration settings for the application.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd ai-voice-reporting-system/backend
   ```

2. **Install Dependencies**:
   Use pip to install the required Python packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Set up the necessary environment variables for API keys and service URLs as specified in `src/utils/config.py`.

4. **Run the Application**:
   Start the backend server:
   ```
   python src/app.py
   ```

## Usage

- The backend provides endpoints for uploading reports, processing them, and handling voice interactions.
- Ensure that the necessary cloud services (e.g., Google Cloud Storage, BigQuery) are properly configured and accessible.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.