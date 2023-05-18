# End_to_End_ML
Train a regression model, pickle it, load it and serve the model using Flask, Github, CICD, Heroku and Docker

### Software and Tools Required

1. [Github_Account](https://github.com/)
2. [VS_Code_Editor](https://code.visualstudio.com/download) or any other editor of your choice
3. [Google_Cloud](https://cloud.google.com/)
4. [Git_Cli](https://git-scm.com/download/)

Create a new environment
```
conda create -p myenv python=3.8 -y
```

In this project we will build a machine learning model that can predict a housing price based on the features given. We're just trying to build a basic machine learning model and understand how we can deploy machine learning models in cloud. Building machine learning models using Jupyter notebooks is very common these days. But deploying the model where we can predict in real time Has not been cared much. So we will show how we can deploy in model that we've built after all the analysis that we have done in different cloud platforms like Heroku, GCP and AWS.

Building a machine learning model usually follows the below steps:
1)	Define the objective/business goal.
2)	Data ingestion process where we collect the data from different sources.
3)	Data transformation phase where we will transform the data we have, so that the data can be used for further analysis and machine learning model.
4)	Perform exploratory data analysis or statistical analysis for insights.
5)	Build the machine learning model and fine tune the hyper parameters of machine learning model.
6)	Validate the machine learning model for better generalization and avoid overfitting/underfitting.
7)	Create an API for machine learning model that we built using flask or any other framework you prefer and deploy the app in a docker container.
8)	Deploy the docker containers into any cloud platform and expose the model using an end point.

Here in this culture we built a linear regression model, utilized flask to create an API and deployed the flask application into the docker. Then we deployed the docker into Heroku and GCP.

To deploy the model into GCP we made use of GCP cloud run and utilized cloud build to build the docker application directly from the GitHub to GCP.

To deploy the model into Heroku, we utilized GitHub workflows to automatically deploy the code as soon as it is updated in GitHub.

Switch to heroku branch to see the deployment in Heroku

To run app using python on local environment
```
python app.py
```
access the application using 
```
http://localhost:5000
```
To build docker image
```
docker build -t myapp .
```
To run docker container
```
docker run -p 5000:5000 -d myapp
```
Once you successfully run the container, you can continue your deployment in GCP cloud run.