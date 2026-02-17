from flask import Flask, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from base.constants import OPENAI_API_KEY
import os

app = Flask(__name__)

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Load and create index on startup
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/query', methods=['POST'])
def query():
    try:
        data = request.get_json()
        question = data.get('question')
        
        if not question:
            return jsonify({'error': 'Question is required'}), 400
        
        response = query_engine.query(question)
        return jsonify({'response': str(response)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port = 4000, debug = True)
