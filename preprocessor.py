import pandas as pd
import numpy as np

def preprocess(df, df_train, df_test):
    # load both datasets
    df_train = pd.read_csv('train.csv')
    df_test = pd.read_csv('test.csv')
    
    # combining both datasets
    df = df_train.append(df_test)
    
    # Let's replace the empty strings with NaN values
    df = df.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    df = df.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    df = df.replace('.', np.nan)
    
    # delete these columns
    df.drop(columns=['User_ID','Product_ID'], inplace=True)
    
    # check for duplicate rows in the dataset -> 
    df.duplicated().sum()
    
    # if there are duplicated rows and columns, drop/delete them -> 
    df.drop_duplicates(inplace=True)
    
    # check missing values -> 
    df.isnull().sum()
    
    # If the numerical column is skewed, we use median.
    # Product_Category_2
    df['Product_Category_2'].fillna((df['Product_Category_2'].median()), inplace=True)
    
    # for Product_Category_3
    df['Product_Category_3'].fillna((df['Product_Category_3'].median()), inplace=True)
    
    # If the numerical column is not skewed, we use mean.
    df['Purchase'].fillna((df['Purchase'].mean()), inplace=True)
    
    return df