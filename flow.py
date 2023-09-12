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
    train(data, experiment_name, variables.get("mlflow_server"))


@task
def my_fn():
    highest_churn_possibility = [
       {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
       {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
    ]

    create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )


@flow(name="Train IRIS Model")
def perform_training(experiment_name):
    data = load_data()
    train_model(data, experiment_name)
    my_fn()


if __name__ == "__main__":
    perform_training(
        experiment_name="IRIS Demo Experiment"
    )
