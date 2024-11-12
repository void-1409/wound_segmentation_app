from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import os
import uuid
from ultralytics import YOLO

# Initialize Flask app
app = Flask(__name__)

# Load YOLOv8 model
model = YOLO("best.pt")

# Directory to save segmented images
default_img_path = "runs/segment/predict/image0.jpg"

@app.route('/segment', methods=['POST'])
def segment_image():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Read the image
    image = Image.open(BytesIO(file.read())).convert("RGB")

    # Run YOLOv8 segmentation with custom save directory
    model.predict(image, save=True, project="runs/segment", conf=0.65, exist_ok=True)

    # move image from default path to new path
    if os.path.exists(default_img_path):
        unique_filename = f"{uuid.uuid4().hex}_segmented.jpg"
        new_path = "segmented_images/" + unique_filename
        os.rename(default_img_path, new_path)
        print("image moved successfully!")

    return jsonify({"message": "Image processed successfully"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
