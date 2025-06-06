import { render, screen } from '@testing-library/react';
import { AccessibilityProvider } from '../src/accessibility/AccessibilityContext';
import AudioControls from '../src/components/AudioControls';
import TranscriptDisplay from '../src/components/TranscriptDisplay';
import SummaryView from '../src/components/SummaryView';
import ChartView from '../src/components/ChartView';

describe('Accessibility Tests', () => {
    test('AudioControls component should be accessible', () => {
        render(
            <AccessibilityProvider>
                <AudioControls />
            </AccessibilityProvider>
        );
        const button = screen.getByRole('button', { name: /start listening/i });
        expect(button).toBeInTheDocument();
        expect(button).toHaveAttribute('aria-label', 'Start listening');
    });

    test('TranscriptDisplay component should be accessible', () => {
        render(
            <AccessibilityProvider>
                <TranscriptDisplay />
            </AccessibilityProvider>
        );
        const transcript = screen.getByRole('textbox');
        expect(transcript).toBeInTheDocument();
        expect(transcript).toHaveAttribute('aria-label', 'Real-time transcript display');
    });

    test('SummaryView component should be accessible', () => {
        render(
            <AccessibilityProvider>
                <SummaryView />
            </AccessibilityProvider>
        );
        const summary = screen.getByRole('region', { name: /summary/i });
        expect(summary).toBeInTheDocument();
        expect(summary).toHaveAttribute('aria-labelledby', 'summary-title');
    });

    test('ChartView component should be accessible', () => {
        render(
            <AccessibilityProvider>
                <ChartView />
            </AccessibilityProvider>
        );
        const chart = screen.getByRole('img', { name: /chart/i });
        expect(chart).toBeInTheDocument();
        expect(chart).toHaveAttribute('alt', 'Chart visualization');
    });
});