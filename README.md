# Diamond-Price-Prediction

### Overview
This project aims to build a machine learning model to predict diamond prices based on various features such as carat, cut, color and clarity.

To know more about these features: [experiments.ipynb](https://github.com/CodeWithCharan/Diamond-Price-Prediction/blob/main/research/experiments.ipynb)

### MLOps Pipeline
![MLOps_Pipeline](https://github.com/user-attachments/assets/487acb1b-b412-4108-84ff-3dc8cccda2f7)

### Demo Video
https://github.com/user-attachments/assets/fe2e389d-1b8b-4d41-8874-243039567831

### Workflow

1. **Update** `config.yaml`
   - **Purpose:** Centralizes configuration settings for the pipeline, including data paths, model parameters, and directory structures. This allows flexibility in adjusting the pipeline without hardcoding values.

2. **Update** `schema.yaml`
   - **Purpose:** Defines the structure and data types of the input dataset, ensuring that the data meets the required format for processing (e.g., column names, data types).

3. **Update** `params.yaml`
   - **Purpose:** Stores hyperparameters (e.g., `n_estimators`, `random_state`) and model-specific configurations. This makes the model easily tunable without changing the code.

4. **Update the** `entity`
   - **Purpose:** Defines data classes to manage the configuration for various pipeline stages (e.g., data ingestion, validation). This provides a clean and organized way to handle configurations across the pipeline.

5. **Update the** `configuration manager`
   - **Purpose:** Loads and manages the configurations from `config.yaml`, `schema.yaml`, and `params.yaml` and makes them available to the various components of the pipeline.

6. **Update the** `components`
   - **Purpose:** Implements individual components (e.g., data ingestion, data validation, feature transformation) for the machine learning pipeline. Each component is responsible for a specific task.

7. **Update the main** `pipeline`
   - **Purpose:** Manages the flow of the pipeline, determining the sequence of operations (data ingestion → validation → transformation → training → evaluation). It ensures that each component is executed in the right order.

8. **Update** `main.py`
   - **Purpose:** Acts as the entry point for executing the entire pipeline. It triggers each stage sequentially, enabling the end-to-end execution of the project.

## DAGsHub Model Registry

[DAGsHub Documentation](https://dagshub.com/)

- **MLFlow Experiment Tracking:** https://dagshub.com/CodeWithCharan/Diamond-Price-Prediction.mlflow

- **Model Versioning:** https://dagshub.com/CodeWithCharan/Diamond-Price-Prediction.mlflow/#/models

### MLFlow Tracking URI:

```bash
MLFLOW_TRACKING_URI = https://dagshub.com/CodeWithCharan/Diamond-Price-Prediction.mlflow
```
```bash
MLFLOW_TRACKING_USERNAME = CodeWithCharan
```
```bash
MLFLOW_TRACKING_PASSWORD = YourAccessToken
```

### Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/CodeWithCharan/Diamond-Price-Prediction.mlflow
```
```bash
export MLFLOW_TRACKING_USERNAME=CodeWithCharan
``` 
```bash
export MLFLOW_TRACKING_PASSWORD=YourAccessToken
```

## Flask App

### Run the flask app:
```bash
python app.py
```

### After running the app, it will be available at:
- `http://127.0.0.1:8080/`
- `http://localhost:8080/`

## AWS CI/CD Deployment with Github Actions

Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2
## Steps:

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI =

    ECR_REPOSITORY_NAME = mlproj

## Model Performance Comparison

| Metric                | Linear Regression | KNN Regression | Decision Tree Regression | Random Forest Regression |
|-----------------------|-------------------|----------------|--------------------------|--------------------------|
| **Mean Absolute Error (MAE)**  | 801.79            | 380.42         | 358.59                   | 265.44                   |
| **Mean Squared Error (MSE)**   | 1,503,159.39      | 495,653.67     | 532,793.32               | 278,395.54               |
| **Root Mean Squared Error (RMSE)** | 1,226.03          | 704.03         | 729.93                   | 527.63                   |
| **R2 Score**          | 0.91              | 0.97           | 0.97                      | 0.98                     |
