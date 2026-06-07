import pandas as pd

data = pd.read_csv("data.csv")

data.columns = data.columns.str.strip()
print(data.columns)

print("Average Marks:", data["Marks"].mean())
print("Highest Marks:", data["Marks"].max())
print("Lowest Marks:", data["Marks"].min())

print("\nTop Student:")
print(data.loc[data["Marks"].idxmax()])