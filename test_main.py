import unittest
from fastapi.testclient import TestClient
from pydantic import BaseModel
from mock import Mock, patch, MagicMock

from main import app
import main as main_file

client = TestClient(app)


class ModelInput(BaseModel):
    square_meter: int


class TestMain(unittest.TestCase):

    # Test for main.price_pred
    def test_price_pred_functional_successful(self):
        response = client.post(
            "/price_prediction/",
            headers={"Content-Type": "application/json"},
            json={"square_meter": 2350},
        )
        assert response.status_code == 200
        assert response.json() == {"Price": 351.0}

    # Test for main.price_pred
    def test_price_pred_wrong_status_code_and_price_functional_successful(self):
        response = client.post(
            "/price_prediction/",
            headers={"Content-Type": "application/json"},
            json={"square_meter": 2350},
        )
        assert response.status_code != 400
        assert response.json() != {"Price": 000.0}

    # Test for main.price_pred
    @patch("main.load_model_and_scalars")
    @patch("main.np")
    @patch("main.json")
    def test_price_pred_mock(self, json_mock, np_mock, load_model_and_scalars_mock):
        input_params = Mock(spec=ModelInput)

        loaded_model = MagicMock()
        loaded_scaler_x = MagicMock()
        loaded_scaler_y = MagicMock()

        np_mock_result = MagicMock()
        np_mock.array().reshape(1, -1).return_value = np_mock_result

        load_model_and_scalars_mock.return_value = [
            loaded_model,
            loaded_scaler_x,
            loaded_scaler_y,
        ]
        result = main_file.price_pred(input_params)
        load_model_and_scalars_mock.assert_called_once()
        loaded_model.predict.assert_called_once()
        loaded_scaler_y.inverse_transform.assert_called_once_with(
            loaded_model.predict.return_value
        )
        np_mock.around.assert_called_once_with(
            loaded_scaler_y.inverse_transform().__getitem__().__getitem__()
        )

        self.assertEqual(result, {"Price": np_mock.around.return_value})

    # Test for main.load_model_and_scalars
    @patch("main.open")
    @patch("main.pickle.load")
    def test_load_model_and_scalars_mock(self, pickle_load_mock, open_mock):
        main_file.load_model_and_scalars()

        pickle_load_mock.assert_called_with(open_mock("scaler_y.pkl", "rb"))

        pickle_load_mock.assert_called_with(open_mock("scaler_x.pkl", "rb"))

        pickle_load_mock.assert_called_with(open_mock("reg_model.pkl", "rb"))
