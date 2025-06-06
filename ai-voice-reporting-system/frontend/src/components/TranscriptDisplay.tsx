import React from 'react';

interface TranscriptDisplayProps {
    transcript: string;
}

const TranscriptDisplay: React.FC<TranscriptDisplayProps> = ({ transcript }) => {
    return (
        <div className="transcript-display">
            <h2>Real-time Transcript</h2>
            <p>{transcript}</p>
        </div>
    );
};

export default TranscriptDisplay;