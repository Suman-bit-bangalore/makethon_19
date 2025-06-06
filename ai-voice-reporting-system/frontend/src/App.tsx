import React from 'react';
import AudioControls from './components/AudioControls';
import TranscriptDisplay from './components/TranscriptDisplay';
import SummaryView from './components/SummaryView';
import ChartView from './components/ChartView';
import useWebSocket from './hooks/useWebSocket';
import './styles/theme.css';

const App: React.FC = () => {
    const { socket, messages, error, sendMessage } = useWebSocket('ws://localhost:8080');

    // Example placeholders; replace with actual logic to extract these from messages or state
    const transcript = ""; // e.g., messages.transcript or useState
    const summary = "";    // e.g., messages.summary or useState
    const charts: any[] = [];     // e.g., messages.charts or useState
    const chartData = charts[0] || {}; // Provide a default ChartData object if charts is empty

    return (
        <div className="app">
            <h1>AI-Powered Voice Reporting System</h1>
            <AudioControls />
            <TranscriptDisplay transcript={transcript} />
            <SummaryView summary={summary} />
            <ChartView data={chartData} charts={charts} />
        </div>
    );
};

export default App;