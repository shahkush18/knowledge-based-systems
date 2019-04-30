# Linear Regression using BigQuery ML to Predict Taxi Fares 
### Kush Shah, Pallav Jhaveri, Darshan Shah, Anusha Balaji 


## Dataset 

We have used the **[Chicago Taxi Trips](https://console.cloud.google.com/bigquery?project=bq-tutorial-april-2019&folder&organizationId&p=bigquery-public-data&d=chicago_taxi_trips&t=taxi_trips&page=table)** dataset provided by the **[Google Cloud Platform](https://cloud.google.com/public-datasets/)** to carry out our analysis. 
The entire dataset can be accessed **[here](https://console.cloud.google.com/bigquery?project=bq-tutorial-april-2019&folder&organizationId&p=bigquery-public-data&d=chicago_taxi_trips&t=taxi_trips&page=table)**.


## Linear Regression Model  

A linear regression model was fit on the dataset using Google BigQuery ML toolkit. The following steps were performed in the process: 

1. To start with, we created a new project on the Google Cloud Platform. Using the new project, we created a new Cloud Datalab instance via the Cloud Shell. 
2. We launched a Jupyter Notebook on the allocated Datalab VM to perform our analysis. BigQuery Python client library was then imported to use BQ API. 

![load_bq](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/load_bq.PNG) 

3. We imported the taxi trips dataset using **[BQ Python client library](https://cloud.google.com/bigquery/docs/python-client-migration)**. 

![load_data](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/load_data.PNG) 

4. Using the BQ GUI, a SQL query was written to slightly preprocess and select the input features from the dataset. (See **[Data Preprocessing](#Data-Preprocessing)** section below for more details.) 

5. Linear Regression model was fit on the dataset while a test point was held out for validating the model later. 

![train_model](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/train_model.PNG)

6. Training statistics were calculated using Ml.TRAINING_INFO function of BQ. 

![train_result](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/train_result.PNG)

7. The model was evaluated using ML.EVALUATE. Various error measures such as mean_absolute_error, mean_squared_error, explained_variance, etc. were reported on the training set. 

![eval_result](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/eval_result.PNG)

8. Finally, the model was tested on the held out test point. 

![test_result](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/images/test_result.PNG)


Entire code of our model can be accessed in **[BigQuery ML Linear Regression Team4.ipynb](https://github.com/shahkush18/knowledge-based-systems/blob/master/LinReg/BigQuery%20ML%20Linear%20Regression%20Team4.ipynb)** notebook above. 

## Data Preprocessing  

For our model, we wought to predict **taxi fares** so users may get an estimate beforehand before boarding one. To keep our model simple for now, we used **distance of the trip** to estimate the fare as we tended to observe a positive correlation between distance of trips and their corresponding fares during the data exploration phase. We wanted to check how far that was true and how "strong" is the relationship. 

As distance of the trip was a continuous floating point variable, we feared the model might "memorize" the values than the general trends. To avoid this overfitting, we decided to **"bin"/group trips with similar distances** into their own category and average the fare for the trips in each bin. We had 20 bins in total for all the trips. 

## Results & Analysis 

As seen above, **training error** was pretty low by the end of the training phase. For every iteration during training (10 in total), there was a significant decrease in training error. The model's prediction on the test point was also very accurate. For taxi trips spanning 39-54 miles, the actual average fare was around $5386.99 and the model predicted $5387.362983 - which is very astonishing! 

As a group, we were very surprised to see very low error rate by our model. Usually, people hold the misconception that only complex models (like deep learning neural networks) can yield accurate and useful results. But this exercise proves that ***even a simple linear regression model trained on one to two features can be surprsingly accurate and successful in learning.*** 
