from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

# Initialize FastAPI
app = FastAPI()

# Cross-Origin Resource Sharing (CORS) setup
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading the pre-trained TensorFlow model
MODEL = tf.keras.models.load_model(r"C:\Users\viral\OneDrive\Desktop\Potato Leaf Disease\saved_models\1.keras")

# Defining class names for predictions
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Define a route for a simple ping test
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# Function to read uploaded file as an image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Define a route for image prediction
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    # Read the uploaded image
    image = read_file_as_image(await file.read())
    
    # Prepare the image for prediction
    img_batch = np.expand_dims(image, 0)
    
    # Make predictions using the loaded model
    predictions = MODEL.predict(img_batch)

    # Get the predicted class and confidence score
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    # Return the prediction result
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    # Running the FastAPI application using Uvicorn server
    uvicorn.run(app, host='localhost', port=8000)
