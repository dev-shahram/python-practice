import pandas as pd

data = {
    "name": ["Sharam", "ali", "ahmad", "khan"],
    "age": [20, 30, 35, 80],
    "class": ["A", "B", "C", "D"]
}

df = pd.DataFrame(data)

print(df)
print (df.describe())