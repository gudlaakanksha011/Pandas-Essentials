# -*- coding: utf-8 -*-
"""pandas_Basics.ipynb

Original file is located at
    https://colab.research.google.com/drive/1vWhbneJlhkboyu60k0rbNIoH957Y2MIH
"""

import pandas as pd
a = pd.Series([10,20,30] , index=['a','b','c'])
print(a)
print(type(a))
print(a[0:2])

import numpy as np
a = np.array([[10,20,30],[40,50,60]])
a1 = pd.DataFrame(a, index=['x','y'], columns =['a','b','c'])
print(a1)
print(type(a1))
print(a1.loc['x'])
print(a1['a'])
print(a1[:1])

a = {"day":['mon','tues','wed','thurs','fri','sat','sun'],"dayno":[1,2,3,4,5,6,7],"pricing": [0.1,0.3,0.5,0.6,0.2,0.4,0.7]}
a1 = pd.DataFrame(a)
print("Dataframe:\n",a1)
print(a1['day'])
print(a1['dayno'])
print(a1.head(3)) # prints first 3
print(a1.tail(3)) # prints last 3
print(a1.sample(4)) # prints random 4
a1.info()  # it will quickly access the dataframe and gives the inormation abour dataframe
a1.describe() # it will give the descriptive statics of dataframe like mean, count,median,etc,.

data = pd.read_csv("/content/student (1).csv",encoding='latin1')
print(type(data))
print(data.head(10)) #gets first 10
print(data.dtypes)
print(data.info())
# Drop a column
data.drop(['Sex'], axis =1, inplace =True)
print(data.info())

import pandas as pd
# Writing a dataframe to a csv file
data.to_csv("Students_modified.csv", index = None)
# selecting rows & columns
df1 = pd.read_csv("Students_modified.csv", index_col = "Id" ) # here it will take index as Id
print(df1.loc[5007,:]) # retrieves the row with Id "5007"
df1 = pd.read_csv("Students_modified.csv", index_col = "Student_Age")
print(f"sample:\n",df1.sample(4))
print(f"first 6 records:\n",df1.head(6))
print(f"last 2 records:\n",df1.tail(2))
print(f"location info of 18, 19:\n",df1.loc[[18,19],["Id","Grade"]]) # here it takes student age as index and returns the original index of 18, 19 and their grades
# Accessing specific elements
df1 = pd.read_csv("Students_modified.csv", index_col = "Id")
print(f"Specific details of Id 5007:\n",df1.loc[5001,["Student_Age","High_School_Type","Unnamed: 0","Scholarship"]])

df1 = pd.read_csv("/content/student (1).csv",encoding='latin1')
df1.sample(10)
df1.replace(["Female","Male"],["F","M"], inplace = True)
print(df1.sample(10))

import pandas as pd
# updating a column in a Dataframe
df1 = pd.read_csv("Students_modified.csv", index_col = "Id" )
df1["Changed_Student_Age"] = df1.Student_Age + 1
print(df1.Changed_Student_Age)
df1[["Student_Age","Changed_Student_Age"]].describe()

# functions
def add_1hr(row):
  return row["Weekly_Study_Hours"] + 1;
df1["Weekly_Study_Hours_after_increase"] = df1.apply(add_1hr,axis =1)
df1.head()

# lambda functions
df1["Weekly_Study_Hours_2nd_increase"] = df1.apply(lambda add_1hr: add_1hr [ "Weekly_Study_Hours"] +1, axis=1)
df1.head()

"""# Data Cleaning"""

import pandas as pd
df1= pd.DataFrame([[10,None,30,50],[30,None,50,None],[11,12,13,14]])
print(df1)
print(df1.isna()) # check whether there is any missing value or none and it indicates it with NaN
df1.info()
print(df1.isna().sum(axis=0)) # returns the boolean dataframe indicating how many values are missing in each column
print(df1.isnull().sum(axis =0)) # returns the boolean dataframe indicating how many values are missing in each column
# Handling missing Values
df1.dropna(axis =1, thresh =3) # removes missing values in dataframe and thresh is a parameter where column drops if a column has 3 or more non-null values, it will be kept.
print(df1)
df1.fillna(25, inplace = True) # it replaces the missing values
print(df1)

# Removing Duplicates
df2= pd.DataFrame([[10,20,30,40],[10,20,30,40],[11,12,13,14],[10,20,30,40]])
df2.duplicated()
df2.drop_duplicates(inplace = True) # it removes duplicate rows in dataframe
print(df2)
df2.reset_index(drop = True, inplace = True) # here it resets the index in serialization
print(df2)

# verifying the uniqueness of a column
df1= pd.read_csv("Students_modified.csv")
df1["Id"].count() # returns the total count
df1["Id"].unique().size # returns the unique count without duplicates

"""# Data Aggregations"""

df1= pd.read_csv("/content/sample_dataset.csv",encoding ='latin1')
print(df1.sample(10))
print(df1["Transaction Amount"].describe())
print(df1["Transaction Amount"].sum())

# GroupBy Aggregation
print(df1[["Category","Transaction Amount"]].groupby("Category").sum("Transaction Amount"))
print(df1[["Category","Transaction Amount"]].groupby("Category").agg({"Transaction Amount": ['mean','min','max','sum']}).sort_values(by="Category",ascending = True))

# transfrom data
df1[["Category","Transaction Amount"]].groupby("Category").agg({"Transaction Amount": ['mean','min','max','sum']}).transform(lambda x: x["Transaction Amount"]-x["Transaction Amount"].mean())

# pivot table and aggregation
print(df1[["Gender","Category","Transaction Amount"]].groupby(["Gender","Category"]).agg(total_amount=('Transaction Amount','sum')))
df1[["Gender","Category","Transaction Amount"]].pivot_table(index="Category", columns="Gender",aggfunc=['mean','sum'])

df1 = pd.read_csv("Students_modified.csv")
print(df1.sample(10))
df1[["Student_Age","High_School_Type","Reading"]].pivot_table(index="Student_Age", columns ="High_School_Type",aggfunc=["count"])

"""# Data Concatenation"""

import pandas as pd
df1 = pd.read_csv("sample_dataset.csv")
print(df1.sample(10))
print(f"Name count:",df1["Name"].count())
df2= df1[df1["Gender"]=="F"]
print(f"Customer Id count:",df2["Customer ID"].count())
df3= pd.concat([df1,df2],axis = 0)
print(f"Customer Id count after concat:",df3["Customer ID"].count())
print(f"Duplicate count:",df3[df3.duplicated()].count())
df4= pd.concat([df1,df2],axis =1, join = "inner")
print(f"DF4",df4)
print("========")
print(f"DF4 count:",df4.count())
print("========")
print(df4[["Customer ID","Name","Gender"]].sample(10))
print(f"Head samples:\n",df4.head(10))
print(f"reindex of samples:\n",df4.reindex(df1.index).head())

"""# Data Merging similar to join in SQL"""

df = pd.read_csv("sample_dataset.csv")
print(df.head())
print(df["Gender"]=="F")
df1=df[df["Gender"]=="F"]
print(f"female filtered rows:\n",df1.head()) # it returns of female Gender rows
print(f"Count of df1:\n",df1.count())
print("===================================================")
df2=df[df["Category"]=="Cosmetic"]
print(f"first samples of df2:\n",df2.head()) # it returns only cosmetic
print(f"count of df2:\n",df2.count())
print("===================================================")
df3=pd.merge(df1,df2,how="right",on="Customer ID")
"""df3 will contain all the cosmetic transactions from df2.
For each of these cosmetic transactions, if the Customer ID also exists in df1
(meaning it's a female customer who made a cosmetic purchase),
the corresponding details from df1 (like Gender, Birthdate, etc.) will be included.
If a cosmetic transaction was made by a customer whose Customer ID is not found in df1 (i.e., a male customer),
then the columns that originated from df1 will show NaN for that row."""
#print(f"first samples of df3:\n",df3.head())
print(f"right join Count of df3:\n",df3["Customer ID"].count())
df3=pd.merge(df1,df2,how="left",on="Customer ID")
#print(f"first samples of df3:\n",df3.head())
print(f"left join Count of df3:\n",df3["Customer ID"].count())
df3=pd.merge(df1,df2,how="inner",on="Customer ID")
#print(f"first samples of df3:\n",df3.head())
print(f"inner join Count of df3:\n",df3["Customer ID"].count())
df3=pd.merge(df1,df2,how="outer",on="Customer ID")
#print(f"first samples of df3:\n",df3.head())
print(f"outer join Count of df3:\n",df3["Customer ID"].count())

"""# Join (Joining based on Index)"""

left = pd.DataFrame({"A":["A0","A1","A2"],"B":["B0","B1","B2"]}, index=["K0","k1","k2"])
right =pd.DataFrame({"C":["C0","C1","C2"],"D":["D0","D1","D2"]}, index=["K0","k2","K3"])
df1= left.join(right,how='right')
print(left)
print("===========")
print(right)
print("===========")
print(df1)
print("===========")
df2= left.join(right,how='left')
print(df2)
print("===========")
df3= left.join(right,how='inner')
print(df3)
print("===========")
df4= left.join(right,how='outer')
print(df4)
print("===========")
df5= left.join(right,how='cross')
print(df5)

"""# Compare DateFrames"""

import pandas as pd
df1 = pd.DataFrame({"A":[10,20,30],"B":[40,50,60]})
df2 = pd.DataFrame({"A":[10,32,31],"B":[40,50,60]})
print(df1)
print("=========")
print(df2)
df1.compare(df2)

"""# Transform Dataframes"""

import pandas as pd
import numpy as np
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns =['a','b','c'])
df + 10
print(df +10)

# applying transform function
print(df)
df1=df.transform(func= lambda x: x+10)
print(df1)

result = df.transform(func = ['sqrt'])
result

"""# Pivot Tables"""

df = pd.DataFrame({"Student Names": ["Geethika","Rahul","Veena","Prabhu","Sita"],
                   "Category":["Offline","Online","Online","Offline","Offline"],
                   "Gender":["Female","Male","Female","Male","Female"],
                   "Courses":["c","Python","Java","Hadoop","Sql"],
                   "Fees":[10000, 23000,20000,30000,12000],
                   "Discount":[1100,500,700,650,740]})
print(df)
p_table = pd.pivot_table(df, index =["Gender"], columns =["Category","Courses"],values = ["Fees"],aggfunc='mean')
p_table