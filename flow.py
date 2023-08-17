from prefect import (
    task,
    flow,
    variables
)
from pandas import DataFrame

from train import (
    train,
    load_dataset
)


@task(name="Load Data")
def load_data() -> DataFrame:
    return load_dataset()


@task(name="Train Model")
def train_model(data, experiment_name):
    train(data, experiment_name, variables.get("mlflow_server"))


@flow(name="Train IRIS Model")
def perform_training(experiment_name):
    data = load_data()
    train_model(data, experiment_name)


if __name__ == "__main__":
    perform_training(
        experiment_name="IRIS Demo Experiment"
    )
