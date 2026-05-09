import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONFIG

# ---------------------------
# EXTRACT
# ---------------------------
print("Reading CSV...")
# df = pd.read_csv("../data/sample_retail_sales.csv")
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sample_retail_sales.csv")

df = pd.read_csv(DATA_PATH)


# ---------------------------
# TRANSFORM
# ---------------------------
print("Cleaning data...")

# Remove duplicates
df = df.drop_duplicates(subset="order_id")

# Handle nulls
df = df.dropna(subset=["order_id", "order_date", "sales"])

df["customer_name"].fillna("Unknown", inplace=True)

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

# Numeric conversions
df["quantity"] = pd.to_numeric(df["quantity"])
df["unit_price"] = pd.to_numeric(df["unit_price"])
df["sales"] = pd.to_numeric(df["sales"])

# Standardize text
df["category"] = df["category"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()

# Derived column
df["month"] = df["order_date"].dt.to_period("M").astype(str)

print("Transformation complete")

# ---------------------------
# LOAD
# ---------------------------
print("Loading into PostgreSQL...")

engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("ETL completed successfully!")
