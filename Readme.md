# Potato Leaf Disease Classification

## Python Setup:

1. Install Python on your computer.

2. Install all required Python packages by running:

```
pip install -r training/requirements.txt
pip install -r api/requirements.txt
```

## React JS Setup

1. Install Nodejs (https://nodejs.org/en/download/package-manager/)
2. Get npm package (https://www.npmjs.com/get-npm).
3. Install all dependencies

```bash
cd frontend
npm install --from-lock-json
npm audit fix
    or
npm audit fix --force
```

4. Duplicate `.env.example` as `.env`.

5. Update the API URL in `.env`.

## Model Training

1. Download the data from kaggle (https://www.kaggle.com/arjuntejaswi/plant-village).
2. Retain only the folders related to potatoes.
3. Launch Jupyter Notebook in your browser:

```bash
jupyter notebook
```

4. Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
5. Adjust the dataset path in cell #2.
6. Execute all code cells sequentially.
7. Save the generated model in the models folder with the corresponding version number.

## API Running

### How to use FastAPI

1. Navigate to the `api` folder

```bash
cd api
```

2. Run the FastAPI server using uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now accessible at `0.0.0.0:8000`

## Running the Frontend

1. Move to the `api` folder

```bash
cd frontend
```

2. Duplicate the `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.
3. Launch the frontend:

```bash
npm run start
```

## Deploying the TF Model (.h5) on GCP

1. Create a GCP account (https://console.cloud.google.com/freetrial/signup/tos?_ga=2.25841725.1677013893.1627213171-706917375.1627193643&_gac=1.124122488.1627227734.Cj0KCQjwl_SHBhCQARIsAFIFRVVUZFV7wUg-DVxSlsnlIwSGWxib-owC-s9k6rjWVaF4y7kp1aUv5eQaAj2kEALw_wcB).
2. Create a Project on GCP (https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project) (Keep note of the project id).
3. Create a GCP bucket (https://console.cloud.google.com/storage/browser/).
4. Upload the TensorFlow .h5 model to the bucket in the path `models/potato-model.h5`.
5. Set up the Google Cloud SDK by following the instructions  (https://cloud.google.com/sdk/docs/quickstarts).
6. Authenticate with Google Cloud SDK.

```bash
gcloud auth login
```

7. Run the deployment script.

```bash
cd gcp
gcloud functions deploy predict --runtime python38 --trigger-http --memory 512 --project project_id
```

8. Your model is now deployed.
9. Test the Google Cloud Function using Postman with the [Trigger URL](https://cloud.google.com/functions/docs/calling/http).

Inspiration: https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions

