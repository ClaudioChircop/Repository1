import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from scipy.stats import zscore



st.title('My Amazing App 😔')

#file_path = 'https://raw.githubusercontent.com/aaubs/ds-master/main/apps/M1-attrition-streamlit/HR-Employee-Attrition-synth.csv'
#data = pd.read_csv(file_path)

#option = st.sidebar.selectbox("How would you like to group the data?", ("Gender","Department"))

#st.table(data.groupby(['Attrition',option])['MonthlyIncome'].mean())


df = pd.read_csv('micro_world_139countries.csv', encoding='latin-1')

df = df[['age','anydigpayment','female','mobileowner','educ','internetaccess']] #We only want to focus on some columns so we slice the data

df = df.dropna() #Dropping null/missing values

df = df.rename(columns={'anydigpayment': 'Digital_Payment', 'female': 'Gender', 'mobileowner': 'Mobile_Owner', 'educ': 'Education', 'internetaccess': 'Internet_Access'})

df['Gender'] = df['Gender'].replace({1: 'Female', 2: 'Male'}) #Assigning values to the data within columns (Example 1 = Female 2 = Male)

df['Digital_Payment'] = df['Digital_Payment'].replace({1: 'Yes', 0: 'No'})

df['Mobile_Owner'] = df['Mobile_Owner'].replace({1: 'Yes', 2: 'No', 3: 'Dont know', 4: 'Refused to answer'})

df['Education'] = df['Education'].replace({1: 'Primary school or less', 2: 'Secondary school', 3: 'Tertiary education or more', 4: 'Dont Know', 5: 'Refused to answer'})

df['Internet_Access'] = df['Internet_Access'].replace({1: 'Yes', 2: 'No', 3: 'Dont know', 4: 'Refused to answer'})

df['age_group'] = pd.cut(df['age'], bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, np.inf], #Categorising ages within age groups via Binning
                               labels=['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79','80-89','90+']) #Labels created for the age groups
st.write(df.head())


plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='age_group', palette="viridis")
plt.title('Distribution of Binned Age')

st.pyplot(plt)
