# checking python installation and git working...
import pandas as pd
import numpy as np

data = {"Name":["Saneesh","Antony"], "ID":[987,654]}
df=pd.DataFrame(data)

print(df)
mean = df["ID"].mean()
# mean = (df.mean(numeric_only=True))
print("mean =", mean)


