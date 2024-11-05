import pandas as pd
import numpy as np
df= pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\CreditcardFraud\250k Medicines Usage, Side Effects and Substitutes\Medicines.csv")
df.head()
df.columns
df.shape
missing_vals = df.isnull().sum() / len(df)
missing_vals
missing_more_15 = missing_vals[missing_vals > 0.15]
missing_more_15
list(missing_more_15.index)
missing_vals[missing_vals <= 0.15]
df1 = df.drop(list(missing_more_15.index) , axis = 'columns')
df1.head()
df1 = df1.drop_duplicates()
df1['name'] = df1['name'].str.lower()
df1['name'] = df1['name'].str.strip()
df1['name'].value_counts()
df1.isnull().sum()
df1['use0'] = df1['use0'].str.lower()
df1['use0'] = df1['use0'].str.strip()
df1['use0'].value_counts()
top_treatments = list(df1['use0'].value_counts().head(15).index)
top_treatments
df1['use0'].value_counts().head(15).sum()

df1.shape[0] - df1['use0'].value_counts().head(15).sum()

def filter_high_uses(x):
    return x in top_treatments
df2 = df1[df1['use0'].apply(filter_high_uses)]
df2.head()
df2.isnull().sum()
df3 = df2.dropna()
df3.head()
df2.shape[0] - df3.shape[0]
df3.shape
df3.isnull().sum()
df3.head()
df4 = df3.drop('id' , axis = 'columns')
df4 = df4.applymap(lambda x : x.lower())
df4 = df4.applymap(lambda x : x.strip())
df4.head()
list(df4.columns)
for col in list(df4.columns):
    print(col , len(df4[col].unique()))
df4['Habit Forming'].value_counts().plot.bar()    
df4['sideEffect0'].value_counts()    
df4['sideEffect0'].value_counts().head(10).plot.bar()    
df4['sideEffect1'].value_counts().head(10).plot.bar()    
df4['sideEffect2'].value_counts().head(10).plot.bar()    
df4.head()    

substitute0_sideeffects = {}
for sub,sideffect in df4.groupby('substitute0')['sideEffect0']:
    #print('Substtitute' , sub)
    #print('Sideeffect' , sideffect)
    substitute0_sideeffects[sub] = sideffect

#print(substitute0_sideeffects)
st0_sideeffects = pd.DataFrame(substitute0_sideeffects).fillna(0)
st0_sideeffects 
st0_sideeffects.columns   
st0_sideeffects = st0_sideeffects.drop_duplicates()
st0_sideeffects.shape
st0_sideeffects['zycin 500mg injection'].unique()

st0_sideeffects['lcfex tablet'].unique()

df4.head()
df4['Therapeutic Class'].unique()

df4['Therapeutic Class'].value_counts()  
df4['Habit Forming'].value_counts()

df4.groupby('Therapeutic Class')['Habit Forming'].value_counts()    
df4.groupby('Therapeutic Class')['Habit Forming'].value_counts().unstack().fillna(0)
df4.groupby('Therapeutic Class')['Habit Forming'].value_counts().unstack().fillna(0).plot.bar()    
df4.head()
X = df4.drop(['Therapeutic Class','Habit Forming'] , axis = 1)
Y = df4['Therapeutic Class']
df4.head()    

all_sideeffects = []
for i in range(0,len(df4)):
    sideeffects = list(df4.iloc[i , 6:9])
    sideeffects = sorted(sideeffects)
    all_sideeffects.append(sideeffects)
df4.insert(9,'All Sideeffects' , all_sideeffects)
df4.head()    
df5 = df4.drop(['sideEffect0','sideEffect1','sideEffect2'] , axis = 1)
df5.head()    
    
df5['All Sideeffects'] = df5['All Sideeffects'].astype(str)
df5['All Sideeffects'].nunique()
232
count_all_sideeffects = df5['All Sideeffects'].value_counts()
count_all_sideeffects  
count_all_sideeffects[count_all_sideeffects > 100]    
all_subs = []
for i in range(0,len(df4)):
    subs = list(df4.iloc[i ,1: 6])
    subs = sorted(subs)
    all_subs.append(subs)    
df5.insert(6 , 'All Substitutes' , all_subs)
df5.head()

df6 = df5.drop(['substitute0','substitute1','substitute2',
                'substitute3','substitute4','All Substitute'] , axis=1)

df6.head()
df6['All Substitutes'] = df6['All Substitutes'].astype(str)
df6['All Substitutes'].nunique()

df6.shape

count_all_subs = df6['All Substitutes'].value_counts()
count_all_subs   
    
count_all_subs[count_all_subs > 100] 