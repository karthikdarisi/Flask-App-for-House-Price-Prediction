import os
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "house_price_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model_loaded = pickle.load(f)
def prediction(df):
    y_predicted = model_loaded.predict(df)
    return y_predicted

