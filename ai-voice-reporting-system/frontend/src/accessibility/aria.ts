export const ariaLabels: Record<string, Record<string, string>> = {
    playButton: {
        'aria-label': 'Play audio',
        'aria-pressed': 'false',
    },
    pauseButton: {
        'aria-label': 'Pause audio',
        'aria-pressed': 'false',
    },
    stopButton: {
        'aria-label': 'Stop audio',
        'aria-pressed': 'false',
    },
    transcriptDisplay: {
        'aria-live': 'polite',
        'aria-atomic': 'true',
    },
    summaryView: {
        'aria-labelledby': 'summary-title',
        'role': 'region',
    },
    chartView: {
        'aria-labelledby': 'chart-title',
        'role': 'img',
    },
};