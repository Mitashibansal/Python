import pandas as pd 
import numpy as np
def mult(a,b):
  return a*b
d={'A':[2,3,4],'B':[4,5,6],'C':[8,6,7]}
df=pd.DataFrame(d)
print(df)
print("*After Multiplication Function*")
print(df.pipe(mult,4))

import pandas as pd 
import numpy as np
d={'A':[2,3,4],'B':[4,5,6],'C':[8,6,7]}
df=pd.DataFrame(d)
print(df)
print(" axis= 0 default(column wise); axis =0 column wise ; default axis = 1(Row wise")
print(df.apply(np.sum),df.apply(np.sum,axis = 0),df.apply(np.sum,axis = 1))

import pandas as pd 
import numpy as np
d={'A':[2,3,4],'B':[4,5,6],'C':[8,6,7]}
df=pd.DataFrame(d)
print(df)
print(df.apply(lambda x:x.max()-x.min()))
print("mean",df.apply(np.mean))
