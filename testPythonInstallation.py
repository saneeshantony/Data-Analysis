# checking python installation and git working...
import pandas as pd
import numpy as np

data = {"Name": ["Saneesh", "Antony", "John", "Alice"],
        "ID": [987, 654, 120, 450],
        "Score": [88, 76,30, 85]}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# basic statistics
mean_id = df["ID"].mean()
mean_score = df["Score"].mean()

print("\nMean ID =", mean_id)
print("Mean Score =", mean_score)

# add new column
df["Passed"] = df["Score"] >= 50

print("\nUpdated DataFrame:")
print(df)