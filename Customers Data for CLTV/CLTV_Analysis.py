## Customer life time value analysis

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

data = pd.read_csv(r'C:\Users\Anjli Rathi\Downloads\Projects\Git Projects\Python\CLTV Analysis\Customers Data for CLTV\customer_acquisition_data.csv')
data

data.shape

data.info()

data.describe().transpose()

data.columns

data['CLTV'] = (data['revenue']/data['conversion_rate']) - data['cost']
print(data['CLTV'])

data.head(10).transpose()

cltv_by_channel = data.groupby('channel')['CLTV'].mean()
cltv_by_channel

most_profitable_channels = cltv_by_channel.nlargest(3)
print(most_profitable_channels)

#Calculate the Average Purchase Value:

data['revenue'].sum()
data['customer_id'].nunique()

data['Avg Purchase Value'] = data['revenue']/data['customer_id'].nunique()
print(data['Avg Purchase Value'])

#Calculate the Purchase Frequency:

data['Purchase Frequency'] = data.groupby('customer_id')['customer_id'].transform('count')/data['customer_id'].nunique()
print(data['Purchase Frequency'])

#Calculate the Customer Lifespan:

data['Customer Lifespan'] = data.groupby('customer_id')['customer_id'].cumcount()/data.groupby('customer_id')['customer_id'].transform('count')
print(data['Customer Lifespan'])

#Calculate the CLTV:

data['CLTV'] = (data['Avg Purchase Value']*data['Purchase Frequency']) * data['Customer Lifespan']
print(data['CLTV'])

#Aggregate CLTV by channel:
cltv_by_channel = data.groupby('channel')['CLTV'].sum()
cltv_by_channel

data.head().transpose()

data.drop('customer_id', axis=1, inplace=True)

data.columns

data.dtypes

#Data Visualization

sns.histplot(data['revenue'], color = 'r')
plt.show()

columns = ['cost', 'conversion_rate', 'revenue', 'CLTV','Avg Purchase Value', 'Purchase Frequency', 'Customer Lifespan']

# Create a correlation matrix using the selected columns
correlation_matrix = data[columns].corr()
correlation_matrix

# Generate the heatmap
sns.heatmap(correlation_matrix, annote = True, cmap = 'coolwarm')

# Add a title
plt.title('Correlation Heatmap')

# Display the plot
plt.show()

plt.figure(figsize=(16,7))
sns.jointplot(x= data['cost'], y= data['CLTV'],color ='r')

plt.show()


