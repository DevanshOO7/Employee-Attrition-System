from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app) # UI connect karne ke liye

# Model aur Features dono files 'model' folder ke andar hain
try:
    model = joblib.load('model/attrition_model.pkl')
    
    expected_features = joblib.load('model/features.pkl')
    
    print("ML Model successfully load ")
    print(f"Model ko ye inputs chahiye: {list(expected_features)}") # Terminal me dikhega
except Exception as e:
    print(f"Error loading files: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        features_list = []
        # Dynamic checking: features.pkl 
        for feature in expected_features:
            if feature not in data:
                return jsonify({
                    "status": "error",
                    "error": f"Missing value for: '{feature}'"
                }), 400
            
            features_list.append(data[feature])

        # Data ko Model ke format (2D Array) mein badalna
        final_features = np.array(features_list).reshape(1, -1)

        # Prediction lena
        prediction = model.predict(final_features)
        
        # Output Frontend ko bhejna (1 = Attrition Yes, 0 = Attrition No)
        result = int(prediction[0])
        
        return jsonify({
            "status": "success",
            "attrition_prediction": result,
            "message": "Employee might leave (Risk High)" if result == 1 else "Employee will stay (Risk Low)"
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)