import pandas as pd
#Charge the dataset
df = pd.read_csv("dataset.csv")
print(df.head())
print("\nDimensions of the dataset:")
print(df.shape)

print("\nInformation about the dataset:")
print(df.info())

print("\nmissing values in the dataset:")
print(df.isnull().sum())

print("\nDistribution of the forms:")
print(df["forme_cible"].value_counts())

# Separate features and target variable
x = df[
    "nombre_cotes",
    "cote_a",
    "cote_b",
    "perimetre",
    "surface"
]

y = df["forme_cible"]