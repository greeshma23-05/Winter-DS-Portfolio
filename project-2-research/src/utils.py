import numpy as np
import pandas as pd

def add_enrollment_per_1000(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["enrollment_per_1000"] = (df["college_enrollment_total"] / df["population"]) * 1000
    return df

def clean_analysis_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["crime_rate", "college_enrollment_total", "population"])
    df = df[(df["crime_rate"] >= 0) & (df["population"] > 0)]
    return df

def make_classification_target(df: pd.DataFrame):
    if "enrollment_per_1000" not in df.columns:
        raise KeyError("enrollment_per_1000 not found. Run add_enrollment_per_1000(df) first.")
    threshold = df["enrollment_per_1000"].median()
    out = df.copy()
    out["low_enrollment"] = (out["enrollment_per_1000"] < threshold).astype(int)
    return out, threshold

