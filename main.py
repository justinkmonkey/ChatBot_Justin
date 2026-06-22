from flask import Flask, request, jsonify
from flask_cors import CORS
import fun
from dotenv import load_dotenv
from ollama import chat as ollama_chat

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for Gemini chatbot"""
    try:
        data = request.json
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get response from Gemini API
        response = fun.gemini_chatbot_response(message)
        
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat2', methods=['POST'])
def chat2():
    """API endpoint for Ollama chatbot (local model)"""
    try:
        data = request.json
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get response from Ollama local model
        response = ollama_chat(
            model='nemotron-3-ultra:cloud',
            messages=[{'role': 'user', 'content': message}],
        )
        
        return jsonify({'response': response.message.content}), 200
    except Exception as e:
        return jsonify({'error': f'Ollama error: {str(e)}. Make sure Ollama is running.'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

@app.route('/api/chatbots', methods=['GET'])
def list_chatbots():
    """List available chatbots"""
    return jsonify({
        'chatbots': [
            {'id': 1, 'name': 'Gemini AI', 'description': 'Google Gemini AI (requires API key)', 'endpoint': '/api/chat'},
            {'id': 2, 'name': 'Ollama Local', 'description': 'Local Ollama Model (requires Ollama running)', 'endpoint': '/api/chat2'}
        ]
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)