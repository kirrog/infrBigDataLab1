import json
import pickle
from pathlib import Path

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from src.utils import load_train_data, load_test_data, split2x_y


def train_model():
    clf = make_pipeline(StandardScaler(), LinearSVC(dual="auto", random_state=0, tol=1e-5))

    x_train, y_train = split2x_y(load_train_data())
    x_test, y_test = split2x_y(load_test_data())

    clf.fit(x_train, y_train)
    scores = dict()

    score = clf.score(x_train, y_train)
    print(f"Result score of trained model on train data: {score}")
    scores["train_acc"] = score

    score = clf.score(x_test, y_test)
    print(f"Result score of trained model on test data: {score}")
    scores["test_acc"] = score

    p = Path("../experiments/svc")

    p.mkdir(exist_ok=True, parents=True)

    with open(str(p / "model.pkl"), "wb") as f:
        pickle.dump(clf, f)

    with open(str(p / "metrics.json"), "w", encoding="UTF-8") as f:
        json.dump(scores, f)


if __name__ == "__main__":
    train_model()
