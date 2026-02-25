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
    df1 = pd.read_csv(r"C:\Users\Python\Project Python\Data-Analysis-with-Python-Projects-FreeCodeCamp\Demographic_Data_Analyzer\adult.data", 
                    skipinitialspace=True, names=names_of_columns, na_values="?")

# Load the seconde dataset.
    df2 = pd.read_csv(r"C:\Users\Python\Project Python\Data-Analysis-with-Python-Projects-FreeCodeCamp\Demographic_Data_Analyzer\adult.test",
                    skiprows=1, names=names_of_columns, na_values="?")
    df2["income"] = df2["income"].str.replace(".", "")

# Merge and return the final DataFrame.
    return pd.concat((df1, df2), ignore_index=True).dropna(ignore_index=True)


def analysis_data(df):
    # How many people of each race are represented in this dataset? This should be a 
    # Pandas series with race names as the index labels. (race column)
    people_each_race = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df.groupby("sex")["age"].mean().loc["Male"]

    # What is the percentage of people who have a Bachelor's degree?
    subset_people_Bachelors_degree = df[df["education"] == "Bachelors"]
    its_percentage_Bch_Dg = len(subset_people_Bachelors_degree) / len(df) * 100

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advance_education = np.logical_or(df["education"] == "Bachelors", df["education"] == "Masters",df["education"] == "Doctorate")
    subset_advance_education = df[advance_education]
    make_more_50K = subset_advance_education[subset_advance_education["income"]==">50K"]
    perc_AdvEd_m50K = len(make_more_50K) / len(subset_advance_education) * 100

    # What percentage of people without advanced education make more than 50K?
    not_advance_educ = df[~advance_education]
    make_more_50K = not_advance_educ[not_advance_educ["income"]==">50K"]
    perc_not_AdvEd_m50K = len(make_more_50K) / len(not_advance_educ) * 100

    # What is the minimum number of hours a person works per week?
    min_hours_works_per_week = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    peoples_work_less_hours = df[df["hours-per-week"] == min_hours_works_per_week]
    make_more_50K = peoples_work_less_hours[peoples_work_less_hours["income"]==">50K"]
    perc = len(make_more_50K) / len(peoples_work_less_hours) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    make_m50K_salary = df[(df["income"]==">50K") & (df["native-country"]=="India")]
    occupation = make_m50K_salary["occupation"].value_counts().idxmax()

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    countries = df["native-country"].value_counts()
    take_more_50K = df[df["income"] == ">50K"]["native-country"].value_counts()
    countries_perc = (take_more_50K / countries) * 100
    
    return {
        "The people numbers of each race are represented" : people_each_race,
        "The average age of men" : round(average_age_men),
        "The percentage of people who have a Bachelor's degree" : f"{its_percentage_Bch_Dg:.2f}%",
        "The percentage of people with advanced education make more than 50K":f"{perc_AdvEd_m50K:.2f}%",
        "The percentage of people without advanced education make more than 50K":f"{perc_not_AdvEd_m50K:.2f}%",
        "The minimum number of hours a person works per week": str(min_hours_works_per_week)+"h",
        "The percentage of the people work the minimum nbr of hours have a salary of >50K":f"{perc:.2f}%",
        "The most popular occupation earn >50K in India": occupation,
        "The country has the highest percentage": countries_perc.idxmax(),
    }

    
for key, value in analysis_data(load_merge_data()).items():
    print(f"{key} is/are: {value}")
