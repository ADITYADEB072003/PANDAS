import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"],
     "sa":[24,"Rohitw","maleww"],
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
o=obj[["marketing","sales","sa"]]
for(row,rowSeries)in obj.iterrows():
    
    print("containing")
    print("\n")
    print(rowSeries["sales"])
import pandas as pd

d1={ 'p1': {'1': 700, '2': 975, '3': 970, '4': 900}, \

'p2': {'1': 490, '2': 460, '3': 570, '4': 590} }
d2={ 'p1': {'1': 1100, '2': 1275,'3': 1270,'4': 1400},\
'p2': {'1': 1400, '2': 1260, '3': 1500, '4': 1190}}
df1=pd.DataFrame(d1) 
df2=pd.DataFrame(d2)
print(df1)
print(df2)
print("BOOLEN OPERATION")
print("SUM")
print(df1.add(df2))
print("sub")
print(df1.sub(df2))
print("mul")
print(df1.mul(df2))
print("divide")
print(df1.div(df2))

import pandas as pd
import numpy as np
L1=[99,90,95,94,97]
L2=[94.0,94.0,89.0,np.nan,100]
L3=[92,92,91,99,99]
L4=[97.0,97.0,89.0,95.0,np.nan]
d={"A":L1,"B":L2,"C":L3,"D":L4}
ind=["acc","eco","eng","ip","math"]
df1=pd.DataFrame(d,index=ind)
print(df1)
print("MAx")
print(df1.max(axis=None,skipna=None,numeric_only=None))
print("MIN")
print(df1.min(axis=None,skipna=None,numeric_only=None))
print("mode")
print(df1.mode(axis=0,numeric_only=None))
print("mean")
print(df1.mean(axis=None,skipna=None,numeric_only=None))
print("median")
print(df1.median(axis=None,skipna=None,numeric_only=None))
print("count()")
print(df1.count(axis=1,numeric_only=None))
print("Sum")
print(df1.sum(axis=None,skipna=None,numeric_only=None,min_count=1))
