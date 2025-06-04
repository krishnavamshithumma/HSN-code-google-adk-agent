import pandas as pd

def load_hsn_data(path="/home/vamsi/Desktop/settyl_assignment/data/HSN_Master_Data.csv"):
    df = pd.read_csv(path, dtype=str)
    df['HSNCode'] = df['HSNCode'].astype(str).str.strip()
    df['Description'] = df['Description'].str.strip()
    return df
