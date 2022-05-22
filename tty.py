# import re
# s = '(((1+2)-(3+4))*((5+6)+(7-8)))'
# err0 = '(4*3*2)'
# print(bool(re.findall('[\+\-\*\/][0-9][\+\-\*\/]+',s)))
# print(bool(re.findall('[\+\-\*\/][0-9][\+\-\*\/]+',err0)))
import pandas as pd
df=pd.read_csv('Expression.csv')
print(df.shape)
print(df.tail(1).values.tolist())
