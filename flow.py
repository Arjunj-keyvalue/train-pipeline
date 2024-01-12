from prefect import (
    task,
    flow,
    variables
)
from prefect.artifacts import create_table_artifact
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
    return train(data, experiment_name, variables.get("mlflow_server"))


@task
def record_acc(train_acc, test_acc):
    highest_churn_possibility = [
       {'data':'Train', 'accuracy': train_acc }, 
       {'data':'Test', 'accuracy': test_acc } 
    ]

    create_table_artifact(
        key="train-metrics",
        table=highest_churn_possibility,
        description= "# Metrics"
    )


@flow(name="Train IRIS Model")
def perform_training(experiment_name):
    data = load_data()
    train_acc, test_acc = train_model(data, experiment_name)
    record_acc(train_acc, test_acc)


if __name__ == "__main__":
    perform_training(
        experiment_name="IRIS Demo Experiment"
    )
