import pandas as pd 

df_one = pd.DataFrame({'k1':['A','A','B','B','C','C'],
                        'col1':[100,200,300,300,400,500],
                        'col2':['NY','CA','WA','WA','AK','NV']})

u = df_one['col2'].unique()
print(u, '\n')
u1 = df_one['col2'].nunique()
print(u1, '\n')
u2 = df_one['col2'].value_counts()
print(u2, '\n')

df_one['x10'] = df_one['col1']*10
print(df_one, '\n')

def grab(state):
    return state[0]

df_one['FIRST'] = df_one['col2'].apply(grab)
print(df_one, '\n')

def comp(state):
    if state[0] == 'W':
        return 'Washington'
    elif state[0] == 'N':
        return 'New York'
    else:
        return state

df_one['NAME'] = df_one['col2'].apply(comp)
print(df_one, '\n')

my_map = {'A':1, 'B':2, 'C':3}

df_one['k2'] = df_one['k1'].map(my_map)
print(df_one, '\n')

print("max element of col1: ", df_one['col1'].max())
print("index of max element of col1: ",df_one['col1'].idxmax())

print(df_one.columns)
df_one = df_one.sort_values('x10', ascending=False)
print(df_one, '\n')
df_one.columns = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN']
print(df_one, '\n')

# to join dataframes use pd.concat([df_one, df_two, axis=0])
# axis=0 to join by rows, axis=1 to join by columns.