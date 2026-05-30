import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix



#-----------------------------------------------------------------------
# Functiona Name : PreserveMode
# Description :     It is used to preserve on secondary
# Parameters : model, filename
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def PreserveModel(model, fName):
    joblib.dump(model,fName)
    print("Model Preseved Successfully with name", fName)

#-----------------------------------------------------------------------
# Functiona Name : TrainTitanicModel
# Description :     It Does split X,Y, Training, Testing Data
# Parameters : df
# Return : None
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def TrainTitanicModel(df):
    #split features and lables
    X = df.drop("Survived", axis =1)
    Y = df["Survived"]
    print("\nfeatures")
    print(X.head)
    print("\n lables")
    print(Y.head)
    print("Shape of X",X.shape)
    print("Shape of Y",Y.shape)
    X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Shape of X_train",X_train.shape)
    print("Shape of Y_train",Y_train.shape)
    print("Shape of X_test",X_test.shape)
    print("Shape of Y_test",Y_test.shape)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,Y_train)
    print("Model train Successfully")
    print("Intercept of model", model.intercept_)
    print("\nCoefficient of modal")
    for feature, coefficient in zip(X.columns, model.coef_[0]):
        print(feature, ":", coefficient)
    
    PreserveModel(model, "Marvelloustitanic.pkl")




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
# Functiona Name : CleanTitanicData
# Description : It does Preprocessing, 
#               It removes unnecessary columns
#               It handles Missing Values
#               It converts text data to numeric format
#               It does encoding to categorical columns
# Parameters : df---> pandas dataframe
# Return : df -> cleaned pandas data frame 
# Date : 14/3/2026
# Author : Prajakta Khanvilkar
#-----------------------------------------------------------------------
def CleanTitanicData(df):
    DisplayInfo("Step 2: Original Data")
    print(df.head())

    #remove unnecessary columns
    drop_columns = ["Passengerid","zero","Name", "Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n columns to be dropped")
    print(existing_columns)

    #drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2: Data after column removal")
    print(df.head())

    #handel age column
    if "Age" in df.columns :
        print("Age column before filling missing vlaues")
        print(df["Age"].head(10))

        #coerce -> Invalid value gets converted to NAN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()
        print("median of age", age_median)
        #replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)
        print("\nAge column after preprocessing:")
        print(df["Age"].head(10))
    
    #handel Fare column
    if "Fare" in df.columns :
        print("\nFare column before preprocessing")
        print(df["Fare"].head(10))
        #coerce -> Invalid value gets converted to NAN
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

        fare_median = df["Fare"].median()
        print("median of Fare", fare_median)
        #replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)
        print("\n Fare column after preprocessing:")
        print(df["Fare"].head(10))
    # #handel Embarked column
    if "Embarked" in df.columns :
        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10))
        #convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip() 

        #Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan', 'None', ''], np.nan)
       
        embarked_mode = df["Embarked"].mode()[0]
        print("Mode of Embarked", embarked_mode)
        #replace missing values with median
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)
        print("\n Embarked column after preprocessing:")
        print(df["Embarked"].head(10))

    
    #handel Sex column
    if "Sex" in df.columns :
        print("\n Sex column before preprocessing")
        print(df["Sex"].head(10))
        #coerce -> Invalid value gets converted to NAN
        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")
        print("\n Sex column after preprocessing:")
        print(df["Sex"].head(10))

    DisplayInfo("Data after Preprocessing")
    print(df.head())

    print("missing values after preprocessing")
    print(df.isnull().sum())
    
    #encode embarked column
    df = pd.get_dummies(df,columns=["Embarked"], drop_first=True)
    print("\n Data After Encoding")
    #Convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print(df.head())
    print("Shape of dataser:", df.shape)

    return df
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
    df = CleanTitanicData(df)
    TrainTitanicModel(df)



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