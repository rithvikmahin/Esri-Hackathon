from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods = ['GET'])
def get_query_from_react():
    print("Reached")
    data = request.get_json()
    print(data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)