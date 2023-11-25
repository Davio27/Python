import pandas as pd
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(titanic_url)
print(titanic_data.head())
print(titanic_data.info())
print(titanic_data.describe())  
