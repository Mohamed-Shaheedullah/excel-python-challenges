# %% [markdown]
# ## Excel_Challenge_930 - Start Stop RunTime

# %% [markdown]
# ### Problem from Excel BI Challenge account on LinkedIn

# %% [markdown]
# ### Solution author : M R Shaheedullah

# %% [markdown]
# 

# %%
# import libraries
import pandas as pd
import datetime

# %%
# load data
df = pd.read_csv("Excel_Challenge_930 - Start Stop RunTime.csv", parse_dates=['EventTime'])
df

# %%
# sort dataframe
df = df.sort_values(by=["Machine", "EventTime"], ascending = [True, True])
df = df.reset_index(drop=True)

# %%
all_machines=[]   # create list of machines 
all_machines = df['Machine'].unique().tolist()
# create a dfframe with the max dates for each machine 
all_max = df.groupby('Machine')['EventTime'].max().reset_index()
new_rows_list=[]  # create a list that is to hold new rows (as dicts)
stop_list = []  # create a list to hold index position where new ro is to be added

# %%
for i, row in df.iterrows():
    for m in all_machines:
        # find max eventtime for this machine
        max_dt_df = all_max[all_max['Machine']==m]
        # return eventtime
        current_max = max_dt_df.loc[max_dt_df['Machine']==m, 'EventTime']
        # if the current row is equal to max for this machine and eventtype is 'Start'
        # a new row with eventtype 'Stop' needs to be added (with eventtime 18:00)
        if (row['EventTime']==current_max.iloc[0]) & (row['EventType'] == 'Start'):
        # current date as string
            current_date = pd.to_datetime(row['EventTime']).strftime('%Y-%m-%d')
            new_row = {'Machine': m, 'EventTime': current_date + " 18:00", 'EventType': 'Stop'}
            new_rows_list.append(new_row)
            stop_list.append(i)
            

# %%
df = pd.concat([df, pd.DataFrame(new_rows_list)], ignore_index=True)
df

# %%
# move the new rows to the positions in the stop list
for my_index in reversed(stop_list):
    row_to_move = df.iloc[[len(df)-1]]  # Using double brackets keeps it as a DataFrame
    df_remaining = df.drop(df.index[len(df)-1])
    target_pos = my_index + 1
    df = pd.concat([df_remaining.iloc[:target_pos], row_to_move, df_remaining.iloc[target_pos:]])

# %%
df = df.reset_index(drop=True)
df['EventTime'] = pd.to_datetime(df['EventTime'])
df = df.sort_values(by=['Machine', 'EventType', 'EventTime'])
# This returns ONLY the 'Stop' rows, no NaNs created
df1 = df[df['EventType'] == 'Stop'].reset_index(drop=True)
df = df[df['EventType'] != 'Stop'].reset_index(drop=True)
df

# %%
df
#Merge 
# Joins df2 to df1 using their indices
# This adds '_left' and '_right' to the overlapping columns
df_merged = df.join(df1, lsuffix='_left', rsuffix='_right')

df_merged = df_merged.rename(columns={'Machine_left': 'Machine', 'EventTime_left':'StartTime', 'EventTime_right' : 'StopTime' })
df_merged = df_merged.drop(['Machine_right', 'EventType_left', 'EventType_right'], axis=1)
df_merged
df_merged['RunMinutes'] = (df_merged['StopTime'] - df_merged['StartTime']) /  pd.Timedelta(minutes=1)

df_merged


