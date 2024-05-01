from src.utils import load_model, load_valid_data, split2x_y


def predict_by_model(x_cases, model):
    y_cases = model.predict(x_cases)
    return y_cases


if __name__ == "__main__":
    model = load_model()
    x_data, y_data = split2x_y(load_valid_data())
    y_results = predict_by_model(x_data, model)
    print("Right")
    print(y_data)
    print("Predicted")
    print(y_results)
