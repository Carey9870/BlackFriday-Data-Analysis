def GenderDistributions(df):
    gender = df.Gender.value_counts().reset_index()
    gender.rename(columns={'index': 'Gender', 'Gender':'Count Per Gender'}, inplace=True)
    return gender

def AgeDistributions(df):
    age = df.Age.value_counts().reset_index()
    age.rename(columns={'index':'Age Groups', 'Age':'Total Amount of People Per Age Group'}, inplace=True)
    return age

def Occupation(df):
    occupation = df.Occupation.value_counts().reset_index()
    occupation.rename(columns={'index':'Type of Occupation', 'Occupation': 'Count of People per Occupation'}, inplace=True)
    return occupation

def CityCategory(df):
    city_category = df.City_Category.value_counts().reset_index()
    city_category.rename(columns={'index':'City Category Type', 'City_Category':'Number of People Per City'}, inplace=True)
    return city_category

def StayInCurrentYears(df):
    ss = df.Stay_In_Current_City_Years.value_counts().reset_index()
    ss.rename(columns={'index':'Stay in Current City Year', 'Stay_In_Current_City_Years':'Number of People Per Year'}, inplace=True)
    return ss

def MaritalStatus(df):
    ms = df.Marital_Status.value_counts().reset_index()
    ms.rename(columns={'index':'Marital Status', 'Marital_Status':'Count of People who are Married or Not Married'}, inplace=True)
    return ms

def Product_Category_1(df):
    pc1 = df.Product_Category_1.value_counts().reset_index()
    pc1.rename(columns={'index': 'Product_Category_1', 'Product_Category_1':'Count of Products Per Category'}, inplace=True)
    return pc1

def Product_Category_2(df):
    pc2 = df.Product_Category_2.value_counts().reset_index()
    pc2.rename(columns={'index':'Product_Category_2',  'Product_Category_2': 'Count of People who Purchased Products in category 2'}, inplace=True)
    return pc2

def Product_Category_3(df):
    pc3 = df.Product_Category_3.value_counts().reset_index()
    pc3.rename(columns={'index':'Product_Category_3', 'Product_Category_3':'Count of People who bought Products in Category 3'}, inplace=True)
    return pc3