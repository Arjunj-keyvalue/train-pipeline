# Prefect Train Pipeline Demo
------------------------------------------------------------

# Prefect Commands
Install Prefect by
```shell
pip install -U prefect
```
Now to run prefect server run the command ```prefect server start```
 
In order to create a Prefect config, enter ```prefect init``` on terminal. It will create a ```prefect.yaml``` file.

In the ```deployment``` section of yaml add ```name```, ```entrypoint``` and ```work_pool``` ```name``` and 
```work_queue_name```


Go to the Prefect UI and go to Work Pools -> + -> Local Subprocess to create a new Worker Pool


Now use the command to start the pool.
```shell
prefect worker start --pool test-queue
```

To deploy a flow use ```prefect deploy --name iris-training-local``` command and the workflow will be available under deployments
