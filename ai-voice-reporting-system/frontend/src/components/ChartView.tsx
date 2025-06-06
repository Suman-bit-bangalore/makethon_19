import React from 'react';
import { Bar } from 'react-chartjs-2';

interface ChartData {
    labels: string[];
    datasets: {
        label: string;
        data: number[];
        backgroundColor: string[];
    }[];
}

interface ChartViewProps {
    data: ChartData;
    charts: ChartData[]; // Add the 'charts' property
}

const ChartView: React.FC<ChartViewProps> = ({ data, charts }) => {
    return (
        <div>
            <h2>Report Data Visualization</h2>
            <Bar data={data} />
            {/* Example usage of charts prop */}
            {/* {charts.map((chart, idx) => (
                <Bar key={idx} data={chart} />
            ))} */}
        </div>
    );
};

export default ChartView;
