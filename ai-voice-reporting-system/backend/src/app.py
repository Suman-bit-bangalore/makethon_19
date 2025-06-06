from flask import Flask, request, jsonify
from ingestion.document_ai import extract_text
from ingestion.summarizer import summarize_text
from voice.websocket_server import start_websocket_server

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_report():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    # Extract text from the uploaded document
    extracted_text = extract_text(file)
    
    # Summarize the extracted text
    summary = summarize_text(extracted_text)
    
    return jsonify({'summary': summary}), 200

if __name__ == '__main__':
    # Start the WebSocket server in a separate thread
    start_websocket_server()
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)