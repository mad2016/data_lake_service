import pandas as pd


def split_nulls(df):
    null_rows = df[df.isnull().any(axis=1)]
    not_null_rows = pd.concat([df, null_rows, null_rows]).drop_duplicates(
        keep=False
    )
    return null_rows, not_null_rows
