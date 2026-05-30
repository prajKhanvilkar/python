import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#-----------------------------------------------------------------------
# Functiona Name : DisplayInfo
# Description :     it displays the formatted title
# Parameters :title (str)
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def DisplayInfo(title):
    print("\n"+ "="*70)
    print(title)
    print("="*70)

#-----------------------------------------------------------------------
# Functiona Name : ShowData
# Description : It Shows basic information bout dataset
# Parameters :  df 
#               df-> Pandas dataframe object
#               message
#               message-> Heading Text to display
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def ShowData(df, message):
    DisplayInfo(message)
    print("First five rows of Dataset")
    print(df.head)
    print("\nnShape of Datase")
    print(df.shape)
    print("\n Column names")
    print(df.columns.tolist()) 
    print("\n Missing value in Each Column")
    print(df.isnull().sum())
#-----------------------------------------------------------------------
# Functiona Name : MarvellousTitanicLogistic
# Description : This is main Pipeline controller
#               It Loads the dataset, shows raw data
#               It preprocess the dataset and train the model
# Parameters : Data Path of Dataset file
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1: Loading the Dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial Dataset")


#-----------------------------------------------------------------------
# Functiona Name : main
# Description : Starting point of the application
# Parameters : None
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()