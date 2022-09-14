import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper
import plotly.express as px

# load and read both datasets
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# combining both datasets
df = df_train.append(df_test)

# load preprocessor.py
df = preprocessor.preprocess(df, df_train, df_test)

# sidebar ui
st.sidebar.title('Black Friday Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Gender Distribution', 'Age Distribution', 'Occupation of People', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1 Products',
        'Product_Category_2 Products', 'Product_Category_3 Products'
))

if user_menu == 'Gender Distribution':
    st.subheader('Gender Distribution Among the Buyers')
    gender = helper.GenderDistributions(df)
    st.table(gender)
    
    # A Bar Graph showing Gender Distributions
    st.subheader('A Bar Graph Displaying Gender Distribution Among the Buyers')
    fig = px.bar(df.Gender.value_counts(), color=['indigo','yellow'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Gender Distributions
    st.subheader('A Pie Chart Displaying Gender Distribution Among the Buyers')
    fig = px.pie(values= df.Gender.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Age Distribution':
    st.title('Age Group Distribution')
    age = helper.AgeDistributions(df)
    st.table(age)
    
    # A Bar Graph showing Gender Distributions
    st.subheader('A Bar Graph Displaying Age Group Distribution Among the Buyers')
    fig = px.bar(df.Age.value_counts(), color=['indigo','yellow','blue','green','red','black','violet'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Gender Distributions
    st.subheader('A Pie Chart Displaying Gender Distribution Among the Buyers')
    fig = px.pie(values= df.Age.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Occupation of People':
    st.title('Types of Occupation Among the People')
    occupaton = helper.Occupation(df)
    st.table(occupaton)
    
    # A Bar Graph showing Types of Occupation Among the People
    st.subheader('A Bar Graph Displaying Types of Occupation Among the People')
    fig = px.bar(df.Occupation.value_counts(), color=['indigo','yellow','blue','green','red','black','violet','indigo', 'yellow', 'blue', 'green', 'red', 'black',
                                                'yellow', 'yellow', 'green', 'black', 'red', 'violet', 'blue', 'darkgreen'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Types of Occupation Among the People
    st.subheader('A Pie Chart Displaying Types of Occupation Among the People')
    fig = px.pie(values= df.Occupation.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'City_Category':
    st.title('Types of City Category')
    city_category = helper.CityCategory(df)
    st.table(city_category)
    
    # A Bar Graph showing Types of City Category in which People reside in
    st.subheader('A Bar Graph Displaying Types of City Category in which People reside in')
    fig = px.bar(df.City_Category.value_counts(), color=['indigo','yellow','blue'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Types of City Category in which People reside in
    st.subheader('APie chart Displaying Types of City Category in which People reside in')
    fig = px.pie(values= df.City_Category.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Stay_In_Current_City_Years':
    st.title('How Many Years have People stayed in that City')
    ss = helper.StayInCurrentYears(df)
    st.table(ss)
    
    # A Bar Graph showing how Many Years have People stayed in that City
    st.subheader('A Bar Graph Displaying How Many Years have People stayed in that City')
    fig = px.bar(df.Stay_In_Current_City_Years.value_counts(), color=['indigo','yellow','blue','red','green'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Types of City Category in which People reside in
    st.subheader('A Pie Chart Displaying How Many Years have People stayed in that City')
    fig = px.pie(values= df.Stay_In_Current_City_Years.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Marital_Status':
    st.title('Marital Status Among the Population')
    ms = helper.MaritalStatus(df)
    st.table(ms)
    
    # A Bar Graph showing Marital Status Among the Population
    st.subheader('A Bar Graph showing Marital Status Among the Population')
    fig = px.bar(df.Marital_Status.value_counts(), color=['indigo','yellow'])
    st.plotly_chart(fig)
    
    # A Pie chart showing Marital Status Among the Population
    st.subheader('A Pie Chart showing Marital Status Among the Population')
    fig = px.pie(values= df.Marital_Status.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Product_Category_1 Products':
    st.title('Products belonging to Category 1')
    pc1 = helper.Product_Category_1(df)
    st.table(pc1)
    
    # A Bar Graph showing count of Products belonging to Category 1
    st.subheader('A Bar Graph showing count of Products belonging to Category 1')
    fig = px.bar(df.Product_Category_1.value_counts(), color=['indigo','yellow','blue','green','red','black','violet','indigo', 'yellow', 'blue', 'green', 'red', 'black',
                                                'yellow', 'yellow', 'green', 'black', 'red', 'violet', 'blue',])
    st.plotly_chart(fig)
    
    # A Pie Chart showing count of Products belonging to Category 1
    st.subheader('A Pie Chart showing count of Products belonging to Category 1')
    fig = px.pie(values= df.Product_Category_1.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Product_Category_2 Products':
    st.title('Products belonging to Category 2')
    pc2 = helper.Product_Category_2(df)
    st.table(pc2)
    
    # A Bar Graph showing Products belonging to Category 2
    st.subheader('A Bar Graph showing count of Products belonging to Category 2')
    fig = px.bar(df.Product_Category_2.value_counts(), color=['indigo','yellow','blue','green','red','black','violet','indigo', 'yellow', 'blue', 'green', 'red', 'black',
                                                'yellow', 'yellow', 'green', 'black'])
    st.plotly_chart(fig)
    
    # A Pie Chart showing count of Products belonging to Category 2
    st.subheader('A Pie Chart showing count of Products belonging to Category 2')
    fig = px.pie(values= df.Product_Category_2.value_counts(), data_frame=df)
    st.plotly_chart(fig)

if user_menu == 'Product_Category_3 Products':
    st.title('Products belonging to Category 3')
    pc3 = helper.Product_Category_3(df)
    st.table(pc3)
    
    # A Bar Graph showing Products belonging to Category 3
    st.subheader('A Bar Graph showing count of Products belonging to Category 3')
    fig = px.bar(df.Product_Category_3.value_counts(), color=['indigo','yellow','blue','green','red','black','violet','indigo', 'yellow', 'blue', 'green',
                                                'yellow', 'blue', 'green', 'red'])
    st.plotly_chart(fig)
    
    # A Pie Chart showing count of Products belonging to Category 3
    st.subheader('A Pie Chart showing count of Products belonging to Category 3')
    fig = px.pie(values= df.Product_Category_3.value_counts(), data_frame=df)
    st.plotly_chart(fig)