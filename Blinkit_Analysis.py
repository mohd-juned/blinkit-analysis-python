#!/usr/bin/env python
# coding: utf-8

# # Blinket Analysis

# ### Import Libraries

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Import Raw Data 

# In[84]:


df = pd.read_csv("C:/datas/blinkit_data.csv")


# ### Sample Data 

# In[85]:


df.head(5)


# In[86]:


df.tail(5)


# ### Data Size
# 

# In[87]:


print("Size of Dataset:" , df.shape )


# ### Field Info
# 

# In[88]:


df.columns


# In[89]:


df.dtypes


# ### Cleaning Dataset

# In[90]:


df["Item Fat Content"] = df["Item Fat Content"].replace({"LF" : "Low Fat", "low fat" : "Low Fat", "reg" : "Regular"})


# In[91]:


print(df["Item Fat Content"].unique())


# ## Business Requirements

# ### KPI's Requirements

# In[92]:


# Total sales
Total_sales = df["Sales"].sum()
print(f"Total Sales: ${Total_sales:,.1f}")

# Average sales
Average_sales = df["Sales"].mean()
print(f"Average Sales: ${Average_sales:,.1f}")

# Number of Items
Number_of_Items = df["Sales"].count()
print(f"Number of Items: {Number_of_Items:,.0f}")

# Average Rating
Average_Rating = df["Rating"].mean()
print(f"Average Rating: {Average_Rating:,.1f}")



# ### Charts Requirements

# ####  Total Sales by Fat Content

# In[93]:


total_sales_by_fat = df.groupby("Item Fat Content")["Sales"].sum()
plt.pie(total_sales_by_fat, labels= total_sales_by_fat.index,  autopct= "%1.1f%%", startangle= 90, explode=(0.05,0.0))
plt.axis("equal")
plt.title("Total Sales by Fat Content")
plt.show()


# ####   Total Sales by Item Type

# In[94]:


total_sales_by_item = df.groupby("Item Type")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
bars= plt.bar(total_sales_by_item.index,total_sales_by_item)
plt.xticks(rotation= -90)
plt.xlabel("Item Type")
plt.ylabel("Sales")   
plt.title("Total Sales by Item Type")
plt.tight_layout()

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
      f"{bar.get_height():,.0f}" , ha= "center", va= "bottom", fontsize=8)
plt.show()


# ####    Fat Content by Outlet for Total Sales

# In[95]:


plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Outlet Location Type", y="Sales", hue="Item Fat Content", estimator=sum)
plt.title("Fat Content by Outlet For Total Sales")
plt.legend(title="Item Fat Content", loc= "upper left")


# ####    Total Sales by Outlet Establishment
# 

# In[96]:


sales_by_year= df.groupby("Outlet Establishment Year")["Sales"].sum()
plt.figure(figsize=(10,5))

plt.title("Total Sales by Outlet Establishment")
plt.plot(sales_by_year.index, sales_by_year.values, marker="o", linestyle = "-")

for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x,y, f"{y:,.0f}", ha="center", va="bottom", fontsize=8)

plt.xlabel("Outlet Establishment Year")
plt.ylabel("Sales")
plt.show()


# ####     Sales by Outlet Size
# 

# In[97]:


sales_by_size= df.groupby("Outlet Size")["Sales"].sum()
plt.pie(sales_by_size, labels=sales_by_size.index, startangle=90, autopct="%1.1f%%", explode=(0.0,0.05,0.0 ) )
plt.legend()
plt.axis("equal")
plt.title("Sales by Outlet Size")
plt.show()


# ####    Sales by Outlet Location:
# 
# 

# In[110]:


sales_by_location= df.groupby("Outlet Location Type")["Sales"].sum() 

pbar=plt.barh(sales_by_location.index, sales_by_location)

plt.title("Sales by Outlet Location") 
plt.xlabel("sales")
plt.ylabel("Outlet Location Type")

plt.figure(figsize=(8,5))


plt.show()


# In[ ]:




