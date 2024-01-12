import pandas as pd
from pandas import DataFrame
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn import metrics


def load_dataset() -> DataFrame:
    iris = pd.read_csv("Iris.csv")
    return iris


def train(data, experiment_name, tracking_uri):
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
    train, test = train_test_split(data, test_size=0.3)

    # taking the training data features
    train_X = train[['SepalLengthCm', 'SepalWidthCm',
                     'PetalLengthCm', 'PetalWidthCm']]
    train_y = train.Species 

    test_X = test[['SepalLengthCm', 'SepalWidthCm',
                   'PetalLengthCm', 'PetalWidthCm']] 
    test_y = test.Species 

    with mlflow.start_run():
        run = mlflow.active_run()
        print("Active run_id: {}".format(run.info.run_id))
        model = svm.SVC()  
        model.fit(train_X, train_y)
        prediction = model.predict(test_X)
        
        test_acc = metrics.accuracy_score(prediction, test_y)
        print("Training Complete with accuracy: ", test_acc)

        prediction = model.predict(train_X)
        
        train_acc = metrics.accuracy_score(prediction, train_y)
        mlflow.log_metric("training data accuracy", train_acc)
        mlflow.sklearn.log_model(model, artifact_path="intent-model")
        # mlflow.log_artifact(data_csv, artifact_path="features")
    return train_acc, test_acc


if __name__ == "__main__":
    data = load_dataset()
    train(data, "", "")
