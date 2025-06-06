# Frontend AI Voice Reporting System

This directory contains the frontend application for the AI-powered voice reporting system. The frontend is built using React and TypeScript, providing a user-friendly interface for interacting with the backend services.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ai-voice-reporting-system/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then, run the following command to install the necessary dependencies:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server with:
   ```bash
   npm start
   ```
   The application will be available at `http://localhost:3000`.

## Features

- **Audio Controls**: Users can start and stop audio input for voice interactions.
- **Real-time Transcription**: Displays live transcription of spoken queries.
- **Summary View**: Shows summarized content extracted from uploaded reports.
- **Chart Visualization**: Visualizes data from reports using interactive charts.

## Accessibility

The frontend is designed with accessibility in mind, featuring:

- Screen reader compatibility
- Voice navigation support
- High-contrast themes and scalable text options

## Folder Structure

- `public/`: Contains static files, including the main HTML file.
- `src/`: Contains the main application code.
  - `components/`: Reusable components for the application.
  - `hooks/`: Custom hooks for managing state and side effects.
  - `styles/`: Styling themes for the application.
  - `accessibility/`: Accessibility features and ARIA roles.

## Testing

To run tests for the frontend application, use:
```bash
npm test
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.