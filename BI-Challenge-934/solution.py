# import packages
import openpyxl
import pandas as pd

df = pd.read_excel(r'C:\Users\conif\Documents\Repos\excel-python-challenges\BI-Challenge-934\Excel_Challenge_934.xlsx', sheet_name='data')
df

# # df = xl("A2:D27", headers=True)
# df = df.groupby(['EmployeeID','ProjectID'])['Hours'].sum().reset_index()
# df.sort_values(by=['ProjectID', 'Hours'], ascending=[True, False], inplace=True)
# df['Rank'] = df.groupby('ProjectID')['Hours'].rank('first', ascending=False)
# df.sort_values(by=['ProjectID', 'Rank'], inplace=True)
# df = df[df['Rank']<3].reset_index()
# df = df.groupby(['ProjectID']).agg({'EmployeeID': list}).reset_index()
# # delimiter = ','
# df['Top 2']=df['EmployeeID'].apply(lambda x : '.'.join(x))
# # df['EmployeeID'] = [', '.join(x) for x in df['EmployeeID']]
# df.drop(['EmployeeID'], axis=1, inplace=True )
# df