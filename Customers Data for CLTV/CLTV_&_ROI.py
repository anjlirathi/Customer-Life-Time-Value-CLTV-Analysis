import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Anjli Rathi\Downloads\Projects\Git Projects\Python\CLTV Analysis\Customers Data for CLTV\customer_acquisition_data.csv')
df

#### Data Exploration
df.head(15)
df.tail(5)
df.sample(30)

df.shape
df.info()

df.describe()
df.describe().transpose()

#Distribution of numeric variables

fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12,4))
ax1.set_title('Distribution of Cost')
sns.histplot(df, x= 'cost' , kde=True, ax=ax1)
ax2.set_title('Distribution of Revenue')
sns.histplot(df, x= 'revenue', kde= True, ax=ax2)
plt.show()

sns.histplot(df, x= 'conversion_rate', kde = True)
plt.title('Distribution of Conversion_Rate')
plt.show()

#Distribution of categorical variables

sns.countplot(df, x='channel')
plt.title('Distribution of Channel')
plt.show()

#Grouping and Aggregating Data

#Grouping data
channel_groups = df.groupby('channel')

#Aggregating 'Cost' for each channel group

cost_by_channel = channel_groups['cost'].mean().reset_index()
sns.barplot(cost_by_channel, x='channel', y = 'cost')
plt.show()

#Aggregating 'Conversion_Rate' for each channel group

conversion_rate_by_channel = channel_groups['conversion_rate'].mean().reset_index()
sns.barplot(conversion_rate_by_channel, x='channel', y='conversion_rate')
plt.show()

#Aggregating 'Revenue' for each channel group

revenue_by_channel = channel_groups['revenue'].sum().reset_index()
fig, ax = plt.subplots(figsize= (8,6))
plt.pie(revenue_by_channel['revenue'], labels = revenue_by_channel['channel'], autopct='%1.1f%%')
plt.show()

#Return on Investment (ROI)

df['ROI'] = (df['revenue']-df['cost'])/ df['cost']
df['ROI']
df.head()

#ROI by Channel Analysis

roi_by_channel = df.groupby('channel')['ROI'].mean().reset_index()
roi_by_channel
sns.barplot(roi_by_channel, x='channel', y= 'ROI')
plt.show()

#ROI and Other Variables Analysis

# Computing the correlation matrix

corr = df[['ROI', 'cost','conversion_rate','revenue']].corr()
corr
sns.heatmap(corr, annot=True, cmap=sns.color_palette('Purples_d'))
plt.show()

#Customer Lifetime Value (CLTV)

df['CLTV'] = (df['revenue']-df['cost'])*df['conversion_rate']/df['cost']
df.head()

#Distribution of CLTV

sns.histplot(df, x='CLTV', kde= True, bins= 50)
plt.show()

#CLTV by Channel

cltv_by_channel = df.groupby('channel')['CLTV'].mean().reset_index()
cltv_by_channel
sns.barplot(cltv_by_channel, x='channel', y='CLTV')
plt.show()

# Selecting records where channel is referral or social media

select = df[df['channel'].isin(['referral','social media'])]
sns.catplot(select, x='channel', y='CLTV', kind='box')
plt.show()

#Average CLTV
avg_CLTV = df['CLTV'].mean()
avg_CLTV

#Calculate customer value

df['customer_value'] = ['High' if cltv > avg_CLTV else 'Low' for cltv in df['CLTV']]
df['customer_value']

sns.countplot(df, x= 'customer_value')
plt.xlabel('customer_value')
plt.ylabel('Count')
plt.title('Counts of Customer Value')
plt.show()

#Counts of Customer Value by Channel

sns.countplot(df, x='channel', hue= 'customer_value')
plt.xlabel('channel')
plt.ylabel('count')
plt.title('Counts of Customer Value by Channel')
plt.legend(title = 'customer_value')
plt.show()



