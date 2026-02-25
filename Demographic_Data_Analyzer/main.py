import pandas as pd
import numpy as np


def load_merge_data():
    """
    Load, clean, and merge the Adult Census Income dataset from UCI ML Repository.

    Source: https://archive.ics.uci.edu/dataset/2/adult

    The dataset is split into two files:
        - adult.data : training set (~32,561 rows)
        - adult.test : test set (~16,281 rows)
    """
    names_of_columns = ["age", "workclass","fnlwgt","education",
                        "education-num","marital-status","occupation",
                        "relationship","race","sex","capital-gain",
                        "capital-loss","hours-per-week","native-country","income"]
# Load the first dataset.
    df1 = pd.read_csv("adult.data", 
                    skipinitialspace=True, names=names_of_columns, na_values="?")

# Load the seconde dataset.
    df2 = pd.read_csv("adult.test",
                    skiprows=1, names=names_of_columns, na_values="?")
    df2["income"] = df2["income"].str.replace(".", "")

# Merge and return the final DataFrame.
    return pd.concat((df1, df2), ignore_index=True).dropna(ignore_index=True)

df = load_merge_data()
