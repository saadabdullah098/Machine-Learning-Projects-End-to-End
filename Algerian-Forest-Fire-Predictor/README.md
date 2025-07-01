
## Goal of Project

#### 1. Create the best linear regression model to predict Fire Weather Index (FWI) from selected features
#### 2. Create a logistic regression model that uses the selected features and the predicted FWI to predict the probability of a fire. 
#### 3. Export the models and scalers to create a user interface for future predictions and host it on AWS


Requires Python >3.9

To run the flask application, run these command in the terminal. 

```
pip install -r requirements.txt
python application.py
```


To access your flask application open new tab in and paste the url:
```

```


## Other Details:

- The notebooks folder contains the python notebooks that go into detail on exploratory data analysis and model training including model comparison and best model selection. 
- The models folder contains the exported pkl files of the scalers and models 
- The dataset folder contains the raw datasets along with the cleaned datasets
- The templates folder contains html files for the user interface webpages 
- The requirements.txt contains the required libraries to run the app 
- The application.py file is the code for the Flask application