# AI-Powered Voice Reporting System

This project implements an AI-powered voice reporting system that allows users to upload reports and interact with them through voice commands. The system leverages Google Cloud services and various AI models to provide real-time transcription, summarization, and voice responses.

## Project Structure

The project is organized into several key components:

- **backend**: Contains the server-side application responsible for handling report ingestion, summarization, and voice interactions.
  - **src**: The source code for the backend application.
    - **ingestion**: Modules for document processing and summarization.
    - **voice**: Modules for handling speech-to-text and text-to-speech functionalities.
    - **llm**: Logic for interacting with language models and managing conversation state.
    - **storage**: Interfaces for interacting with cloud storage solutions.
    - **utils**: Utility functions and configuration management.
  - **requirements.txt**: Lists the Python dependencies required for the backend application.
  - **README.md**: Documentation specific to the backend.

- **frontend**: Contains the client-side application built with React.
  - **public**: Static files, including the main HTML file.
  - **src**: The source code for the frontend application, including components, hooks, and styles.
  - **package.json**: Configuration file for npm, listing dependencies and scripts.
  - **tsconfig.json**: TypeScript configuration file.
  - **README.md**: Documentation specific to the frontend.

- **infra**: Infrastructure as code for deploying the application on Google Cloud.
  - **cloudrun**: Dockerfile for building the Cloud Run service.
  - **cloudfunctions**: Entry point for the Cloud Function handling report ingestion.
  - **terraform**: Terraform configurations for deploying infrastructure.
  - **README.md**: Documentation for the infrastructure setup.

- **tests**: Contains unit tests for both backend and frontend components.
  - **backend**: Tests for the backend ingestion module.
  - **frontend**: Tests for accessibility features in the frontend application.
  - **README.md**: Documentation for the testing strategy and setup.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- Google Cloud account with access to relevant services

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-voice-reporting-system
   ```

2. Set up the backend:
   - Navigate to the `backend` directory and install dependencies:
     ```
     cd backend
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory and install dependencies:
     ```
     cd frontend
     npm install
     ```

### Running the Application

- Start the backend server:
  ```
  cd backend
  python src/app.py
  ```

- Start the frontend application:
  ```
  cd frontend
  npm start
  ```

### Usage

- Upload reports (PDFs, spreadsheets) through the frontend interface.
- Use voice commands to interact with the reports and receive summaries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.