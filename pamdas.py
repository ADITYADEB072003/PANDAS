import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"],
     "sa":[24,"Rohitw","maleww"],
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
o=obj.iat[0,2]
print(o)


import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"],
     "sa":[24,"Rohitw","maleww"],
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
o=obj[["marketing","sales","sa"]]
print(o)

import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"]
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
print(obj)
print(obj.index)
print(obj.size)
print(obj.shape[0])
print(obj.shape[1])


import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"]
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
print(obj)
print(obj.dtypes)
print("columns")
print(obj.axes[1])
print("rows")
print(obj.axes[0])
print(obj.values)

import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"]
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
print(obj)
print(obj.dtypes)
print("columns")
print(obj.axes[1])
print("rows")
print(obj.axes[0])
print(obj.values)

import pandas as pd
yr={"Target":[56000,70000,75000,60000],
    "sales":[58000,68000,78000,61000]}
obj=pd.DataFrame(yr,index=["zoneA","zoneB","zoneC","zoneD"])
o=obj.loc[:,"order"]=[6000,6700,6200,6000]
p=obj.assign(o=[1,2,3,4])
l=obj.loc["zoneE",:]=[50000,45000,5000]
print(obj)
print(p)

import pandas as pd
yr={"Target":[56000,70000,75000,60000],
    "sales":[58000,68000,78000,61000]}
obj=pd.DataFrame(yr,index=["zoneA","zoneB","zoneC","zoneD"])
o=obj.loc[:,"order"]=[6000,6700,6200,6000]
p=obj.assign(o=[1,2,3,4])
l=obj.loc["zoneE",:]=[50000,45000,5000]
del obj['sales']
w=obj.drop(['zoneE'])
print(obj)
print(w)

import pandas as pd
d={
    "marketing":[25,"neha","female"],
     "sales":[24,"Rohit","male"],
     "sa":[27,"Rohitw","maleww"],
    
}
obj=pd.DataFrame(d,index=["age","name","sex"])
o=obj.rename(index={"age":"a","name":"b","sex":"s"},columns=({"marketing":"m","sales":"s","sa":"f"}))
print(o)

import pandas as pd
yr={"Target":[56000,70000,75000,60000],
    "sales":[58000,68000,78000,61000]}
obj=pd.DataFrame(yr,index=["zoneA","zoneB","zoneC","zoneD"])
o=obj.iat[0,0]=9000
print(obj)

