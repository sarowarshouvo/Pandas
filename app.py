import pandas as pd
## Loading data

df=pd.read_csv('pokemon_data.csv')
print(df)
# print(df.head(3))
# print(df.tail(3))
# df_xlsx=pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))
# df_text=pd.read_csv('pokemon_data.txt',delimiter='\t')
# print(df_text.head(4))

##  Reading Data

## Print every col name
# print(df.columns)
##  Each col
# print(df[['Name','Type 1','HP']][0:5])
##  Each row (iloc)
# print(df.iloc[0:4])
##  Specific Location(R,C)
# print(df.iloc[2,9])
##  Iterating each rows using for
# for index,row in df.iterrows():
#     print(index,row['HP'])
## Loc (based on texual infos)
# print(df.loc[df['Type 1'] =="Fire"])

##  Sorting/Describing  Data
# print(df.describe())
# print(df.sort_values(['Type 1','Speed'],ascending=[1,0]))

##  Making Chnages to data
# df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
# df=df.drop(columns=['Total'])
# print(df)
df['Total']=df.iloc[:,4:10].sum(axis=1)
print(df.head(4))
# cols=list(df.columns)
# print(cols)
# df=df[cols[0:2]+ [cols[-1]]+ cols[2:12]]
# print(df)