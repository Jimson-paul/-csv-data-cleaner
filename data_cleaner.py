
import pandas as pd

df = pd.read_csv("Book1.csv")

df.columns = df.columns.str.strip()

df.dropna(how='all', inplace=True)

df['AGE'] = df['AGE'].fillna(df['AGE'].mean())
df['NAME'] = df['NAME'].fillna("Unknown")
df['CITY'] = df['CITY'].fillna("Unknown")

df.drop_duplicates(inplace=True)

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved as 'cleaned_data.csv'")
from google.colab import files
files.download("cleaned_data.csv")

with open("README.md", "w") as f:
    f.write(readme)
