from flask import Flask, request, jsonify

from postal.parser import parse_address
from postal.expand import expand_address

app = Flask(__name__)


@app.route('/')
def index():
    """
    API Documentation Landing Page
    """
    return """
    <html>
        <head>
            <title>Address API Documentation</title>
        </head>
        <body>
            <h1>📚 Address API Documentation</h1>
            <p>Welcome to the Address API! Below are the available endpoints:</p>
            <ul>
                <li><strong>Parse Address:</strong> <code>POST /parse</code>
                    <p>Parse an address into its components.</p>
                    <p><strong>Example:</strong> <code>{"address": "1600 Amphitheatre Parkway, Mountain View, CA"}</code></p>
                </li>
                <li><strong>Expand Address:</strong> <code>POST /expand</code>
                    <p>Expand an address into multiple variations.</p>
                    <p><strong>Example:</strong> <code>{"address": "123 Main St"}</code></p>
                </li>
                <li><strong>Tokenize Address:</strong> <code>POST /tokenize</code>
                    <p>Tokenize an address into individual words.</p>
                    <p><strong>Example:</strong> <code>{"address": "123 Main St, Anytown"}</code></p>
                </li>
                <li><strong>Health Check:</strong> <code>GET /health</code>
                    <p>Check if the service is running properly.</p>
                </li>
            </ul>
            <h3>📌 Usage Example</h3>
            <p>Use tools like <strong>curl</strong> or <strong>Postman</strong> to interact with these endpoints.</p>
            <pre>
                curl -X POST -H "Content-Type: application/json" -d '{"address": "123 Main St"}' http://localhost:5000/parse
            </pre>
        </body>
    </html>
    """


@app.route('/parse', methods=['POST'])
def parse():
    """
    Parse an address into components.
    """
    address = request.json.get('address')
    if not address:
        return jsonify({"error": "No address provided"}), 400
    
    parsed = parse_address(address)
    return jsonify(dict(parsed))


@app.route('/expand', methods=['POST'])
def expand():
    """
    Expand an address into multiple variations.
    """
    address = request.json.get('address')
    if not address:
        return jsonify({"error": "No address provided"}), 400
    
    expanded = expand_address(address)
    return jsonify(expanded)


@app.route('/tokenize', methods=['POST'])
def tokenize():
    """
    Tokenize an address into words.
    """
    address = request.json.get('address')
    if not address:
        return jsonify({"error": "No address provided"}), 400
    
    tokens = address.split()
    return jsonify(tokens)


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    """
    return jsonify({"status": "ok"})
