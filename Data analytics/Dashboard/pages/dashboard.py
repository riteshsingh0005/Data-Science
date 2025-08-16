import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
st.subheader('Titanic Data Analysis Insight and Visualization')
st.markdown('Get all the insight as stats and visulas of Titanic data in this application')

st.subheader('Datasets')

df = sns.load_dataset('titanic')
st.dataframe(df)

#filters
st.sidebar.header("Filter")

gender= st.sidebar.multiselect('Gender',
                               options= df['sex'].unique(),
                               default= df ['sex'].unique())

pclass= st.sidebar.multiselect('Passanger Class',
                               options= df['pclass'].unique(),
                               default= df ['pclass'].unique())

min_age , max_age = st.sidebar.slider('Age',
                                      min_value= int(df['age'].min()),
                                      max_value= int(df['age'].max()),
                                      value= (int(df['age'].min()), int (df['age'].max())))

filtered_data = df[
    (df['sex'].isin(gender))&
    (df['pclass'].isin(pclass))&
    (df['age']>=min_age)&
    (df['age']<= max_age)
]
st.dataframe(filtered_data)
st.subheader('Visual of Insight')

#Age Distribution

fig = px.histogram(filtered_data, x='age', title='Age Distribution', color='embarked')
st.plotly_chart(fig)
st.markdown("This graph shows the distribution of age of the people of the titanic ship")

fig= px.box( filtered_data , x='pclass', y='age', color='survived', title='Age wise Fare')
st.plotly_chart(fig)