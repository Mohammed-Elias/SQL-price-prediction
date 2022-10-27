import json
import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ModelInput(BaseModel):
    square_meter: int


def load_model_and_scalars():
    model_file = open("reg_model.pkl", "rb")
    scaler_x_file = open("scaler_x.pkl", "rb")
    scaler_y_file = open("scaler_y.pkl", "rb")

    loaded_model = pickle.load(model_file)
    loaded_scaler_x = pickle.load(scaler_x_file)
    loaded_scaler_y = pickle.load(scaler_y_file)

    return loaded_model, loaded_scaler_x, loaded_scaler_y


@app.post("/price_prediction/")
def price_pred(input_params: ModelInput):

    input_data = input_params.json()
    input_dict = json.loads(input_data)
    square_meter = input_dict["square_meter"]
    loaded_model, loaded_scaler_x, loaded_scaler_y = load_model_and_scalars()

    pred_y = loaded_model.predict(
        loaded_scaler_x.transform(np.array([square_meter]).reshape(1, -1))
    )
    pred_y_rescaled = loaded_scaler_y.inverse_transform(pred_y)
    price = np.around(pred_y_rescaled[0][0])

    return {"Price": price}
