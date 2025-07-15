
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        features = data['features']  # Make sure this exists

        # Dummy prediction (replace with model.predict)
        prediction = [0]  # Replace with actual model output
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        print("❌ ERROR:", e)
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
