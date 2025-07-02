
## Goal of Project

#### 1. Create the best linear regression model to predict Fire Weather Index (FWI) from selected features
#### 2. Create a logistic regression model that uses the selected features and the predicted FWI to predict the probability of a fire
#### 3. Export the models and scalers to create a user interface for future predictions and host it on AWS

## To Run the App Locally: 

1. Download the repository and navigate to the folder using the terminal
2. Create a python virtual environment with Python==3.9 (requires Python >3.9)
3. Run these command in the terminal. 
  ```
  pip install -r requirements.txt
  python application.py
  ```
3. To access your flask application open new tab in and paste the url:
  ```
  http://127.0.0.1:5002
  ```

## To Deploy the App on AWS (Unsecured):

1. Ensure that the .ebextensions and Procfile exists

2. Create an AWS Elastic Beanstalk environment with these configurations:

   Environment Tier: Web server environment
   Application Name: <any name>
   Platform: Python
   Plotform Branch: Python 3.9
   Application Code: Sample application
   Presets: Single Instance

   For Service role and EC2 instance profile, create a new role with default settings.
   Skip to Review and press Create

4. Create a AWS CodePipline with these configurations:

   Build custom pipeline
   Pipeline name: <any name>
   Service role: New service role
   Role name: <any name>

   Source provider: Github (connect to the repo containing the app)
   Skip Build and Test stage

   Deploy Provider: AWS Elastic Beanstalk

   Application Name: <AWS Beanstalk Env that was created previously>
   Environment Name: <AWS Beanstalk Env that was created previously>

   Create Pipeline
   
5. It will take some time to start up, but if everything works, there will be a URL in the Beanstalk environment for the app
   The app continuously updates as changes are made in GitHub

6. Remember to Terminate or Delete Environments and Pipelines if not for future use to prevent AWS fee charges

## File Descriptions 

- The notebooks folder contains the python notebooks that go into detail on exploratory data analysis and model training including model comparison and best model selection. 
- The models folder contains the exported pkl files of the scalers and models 
- The dataset folder contains the raw datasets along with the cleaned datasets
- The templates folder contains html files for the user interface webpages 
- The requirements.txt contains the required libraries to run the app 
- The application.py file is the code for the Flask application
- The .ebextensions and Procfile files contains AWS Beanstalk configurations to deploy this app as a webpage 
