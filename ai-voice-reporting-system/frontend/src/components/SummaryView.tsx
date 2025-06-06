import React from 'react';

interface SummaryViewProps {
    summary: string;
}

const SummaryView: React.FC<SummaryViewProps> = ({ summary }) => {
    return (
        <div className="summary-view">
            <h2>Summary</h2>
            <p>{summary}</p>
        </div>
    );
};

export default SummaryView;