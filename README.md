# Objective:
Heart Failure is biggest problem in the word into healtcare industry. So we predict possibility of heart failure on the basis of given features using machine learning

# Website Link:
https://heart-failure-prediction12.herokuapp.com/

# How to run this app:
Code is written in Python 3.9. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

# Technical aspect:
1.  Python 3.9
2.  Front-end: HTML
3.  Back-end: Flask
4.  IDE: Jupyter Notebook, VS Code
5.  Deployment: Heroku

# Technology Used:
1.  Pandas
2.  Numpy
3.  Matplotlib
4.  Seaborn
5.  Sci-kit learn
6.  Flask
7.  Gunicorn
8.  Heroku

# Workflow:
   # Data Collection:
Apple iPhone SE data set from Kaggle

# Data Pre-Processing:
1.  Missing values handling by Simple imputation (median strategy)
2.  Categorical features handling by ordinal encoding and label encoding
3.  Feature scaling done by Standard Scalar method
4.  Imbalanced dataset handled by SMOTE
5.  Feature selection done by forward feature selection

# Model Implementation and Evaluation:
1.  Various classification algorithms like Logistic Regression, Random Forest, Decision Tree, Naïve Bayes, KNN tested.
2.  Random Forest was given better results. Random Forest was chosen for the final model training and testing.
3.  Model performance evaluated based on accuracy, confusion matrix.

# Model Deployment
The final model is deployed on Heroku using Flask framework
