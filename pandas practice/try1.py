
import pandas as pd
df = pd.DataFrame({'a':[1,2,3,5,5], 'b':[6,7,8,8,10], 'C':[11,11,13,14,15]})
df.to_csv('pandas practice/tr.csv' , index = True )