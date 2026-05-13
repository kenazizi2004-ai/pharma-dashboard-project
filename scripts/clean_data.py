import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/pharma_data.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["success_rate"] = df["success_rate"].fillna(df["success_rate"].mean())
df["side_effect_rate"] = df["side_effect_rate"].fillna(df["side_effect_rate"].mean())

# Create risk score metric
df["risk_score"] = df["side_effect_rate"] / df["success_rate"]

# Save cleaned dataset
df.to_csv("data/processed/cleaned_pharma_data.csv", index=False)

print("✅ Cleaned dataset saved to data/processed/")
