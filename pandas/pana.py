import pandas as pd

data = {
    "name": ["Sharam", "ali", "ahmad", "khan"],
    "age": [25, 30, 35, 90],
    "class": ["A", "B", "C", "D"]
}

df = pd.DataFrame(data)

print(df)