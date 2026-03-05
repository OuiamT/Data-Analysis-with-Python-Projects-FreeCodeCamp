# 🏥 Medical Data Visualizer:

A data analysis and visualization project exploring the relationship between **cardiac disease**, **body measurements** and **lifestyle choices** using Python.
This project is part of the [FreeCodeCamp – Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer) certification curriculum.

## 📋 Dataset Description:

Each row represents a **patient**. The dataset contains objective measurements, examination results, and self-reported lifestyle habits.

| Feature | Variable | Type | Values |
|---|---|---|---|
| Age | `age` | Objective | int (days) |
| Height | `height` | Objective | int (cm) |
| Weight | `weight` | Objective | float (kg) |
| Gender | `gender` | Objective | categorical code |
| Systolic blood pressure | `ap_hi` | Examination | int |
| Diastolic blood pressure | `ap_lo` | Examination | int |
| Cholesterol | `cholesterol` | Examination | 1: normal, 2: above normal, 3: well above normal |
| Glucose | `gluc` | Examination | 1: normal, 2: above normal, 3: well above normal |
| Smoking | `smoke` | Subjective | binary |
| Alcohol intake | `alco` | Subjective | binary |
| Physical activity | `active` | Subjective | binary |
| Cardiovascular disease | `cardio` | Target | binary |

## 🔍 What the Notebook Does:

### 1. Data Loading & Feature Engineering
- Loads the dataset from `medical_examination.csv`
- Calculates **BMI** and adds an `overweight` column (`1` = overweight, `0` = not)
- Normalizes `cholesterol` and `gluc` to binary values (`0` = normal, `1` = abouve normal)

### 2. Categorical Plot (`draw_cat_plot`)
- Reshapes data using `pd.melt()` to long format
- Draws a **count plot** split by cardiovascular disease status (`cardio`)
- Shows the distribution of: `cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`

### 3. Correlation Heatmap (`draw_heat_map`)
- Computes correlation between all numeric features using `DataFrame.corr()`
- Displays a **heatmap** using Seaborn to reveal relationships between variables

## 📁 Project Structure:
```
Medical_Data_Visualizer/
│
├── main.ipynb                  # Main analysis notebook
├── medical_examination.csv     # Dataset
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files and folders ignored by Git
└── README.md                   # Project documentation
```