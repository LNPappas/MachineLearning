import pandas as pd 

af = pd.read_csv('african_econ_crises.csv')
a = af.head()
# print(a, '\n')

b = af['country'].nunique()
# print(b, '\n')

c = af['country'].unique()
# print(c, '\n')

d = af.sort_values('inflation_annual_cpi', ascending=False).head(1)['country']
# print(d, '\n')

f = af[(af['country']=='Kenya')&(af['systemic_crisis']==1)]['year'].min()
# print(f, '\n')

g = af[af['systemic_crisis']==1].groupby('country').count()['systemic_crisis']
# print(g, '\n')

h = len(af[(af['country']=='Zimbabwe') & (af['sovereign_external_debt_default']==1)])
# print(h, '\n')

i = af[af['country']=='Algeria'].sort_values('exch_usd', ascending=False).head(1)['year']
print(i, '\n')