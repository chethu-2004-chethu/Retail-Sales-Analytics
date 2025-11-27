#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import mysql.connector

# 1. Load CSV
df = pd.read_csv(r"C:\Users\ck341\Contacts\ANACONDA\retail_sales_dataset.csv")

# 2. Convert date (DD-MM-YYYY → YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'])

# 3. Clean Data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# 4. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9900122713",
    database="retailsalesdb"
)
cursor = conn.cursor()

# 5. Insert cleaned data into SQL table
for _, row in df.iterrows():
    sql = """
        INSERT INTO factsales
        (TransactionID, Date, CustomerID, Gender, Age, 
         ProductCategory, Quantity, PricePerUnit, TotalAmount)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    
    values = (
        row['Transaction ID'],
        row['Date'],
        row['Customer ID'],
        row['Gender'],
        row['Age'],
        row['Product Category'],
        row['Quantity'],
        row['Price per Unit'],
        row['Total Amount']
    )
    
    cursor.execute(sql, values)

conn.commit()
conn.close()

print("Data Loaded Successfully!")



# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




