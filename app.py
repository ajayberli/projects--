from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load trained model
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def predict_image(img_path):
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = "Dog" if prediction[0][0] > 0.5 else "Cat"
    confidence = prediction[0][0] if predicted_class == "Dog" else 1 - prediction[0][0]

    return predicted_class, float(confidence * 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            label, confidence = predict_image(filepath)
            return render_template('result.html',
                                   label=label,
                                   confidence=confidence,
                                   image_file=filepath)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
