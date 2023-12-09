import pandas as pd
data1= {'ID':[1,2], 'Name':['Wilsom','Hillson']}
df1 = pd.DataFrame(data1)
print(df1)
data2 = {'ID':[3,4], 'Name':['Rahul','Aditya']}
df2 = pd.DataFrame(data2)
print(df2)
df = pd.concat([df1,df2])
print(df)
